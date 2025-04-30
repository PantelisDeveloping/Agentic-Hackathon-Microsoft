from typing import List, Dict, Any
from datetime import datetime, timedelta
from langchain.agents import Tool, AgentExecutor, LLMSingleActionAgent
from langchain.prompts import StringPromptTemplate
from langchain.chains import LLMChain
from langchain.schema import AgentAction, AgentFinish
from langchain.chat_models import ChatOpenAI
from pydantic import BaseModel

class Intervention(BaseModel):
    type: str
    duration: int  # in minutes
    priority: float
    description: str
    scheduled_time: datetime
    conditions: Dict[str, Any]

class InterventionPlanner:
    def __init__(self, openai_api_key: str):
        self.llm = ChatOpenAI(
            temperature=0,
            model_name="gpt-4",
            openai_api_key=openai_api_key
        )
        self.tools = self._setup_tools()
        self.agent = self._setup_agent()

    def _setup_tools(self) -> List[Tool]:
        return [
            Tool(
                name="check_calendar",
                func=self._check_calendar,
                description="Check user's calendar for availability at a specific time"
            ),
            Tool(
                name="get_current_state",
                func=self._get_current_state,
                description="Get the user's current cognitive state"
            ),
            Tool(
                name="simulate_intervention",
                func=self._simulate_intervention,
                description="Simulate the impact of an intervention on the user's cognitive state"
            ),
            Tool(
                name="check_wearable_data",
                func=self._check_wearable_data,
                description="Check data from wearables (HRV, sleep, activity)"
            )
        ]

    def _setup_agent(self) -> AgentExecutor:
        template = """You are an AI cognitive coach planning interventions for optimal mental performance.
        Your goal is to schedule appropriate interventions based on the user's current state, goals, and schedule.

        Available tools:
        {tools}

        Use the following format:
        Question: the input question you must answer
        Thought: you should always think about what to do
        Action: the action to take, should be one of [{tool_names}]
        Action Input: the input to the action
        Observation: the result of the action
        ... (this Thought/Action/Action Input/Observation can repeat N times)
        Thought: I now know the final answer
        Final Answer: the final answer to the original input question

        Begin!

        Question: {input}
        {agent_scratchpad}"""

        prompt = StringPromptTemplate(
            template=template,
            tools=self.tools,
            input_variables=["input", "agent_scratchpad"]
        )

        llm_chain = LLMChain(llm=self.llm, prompt=prompt)
        tool_names = [tool.name for tool in self.tools]
        agent = LLMSingleActionAgent(
            llm_chain=llm_chain,
            allowed_tools=tool_names,
            stop=["\nObservation:"],
            handle_parsing_errors=True
        )

        return AgentExecutor.from_agent_and_tools(
            agent=agent,
            tools=self.tools,
            verbose=True
        )

    async def plan_interventions(self, 
                               current_time: datetime,
                               goals: List[Dict[str, Any]],
                               time_window_hours: int = 24) -> List[Intervention]:
        """Plan interventions for the next time window"""
        prompt = f"""Plan interventions for the next {time_window_hours} hours.
        Current time: {current_time}
        User goals: {goals}
        
        Consider:
        1. Optimal timing based on circadian rhythms
        2. Current cognitive state and stress levels
        3. Calendar availability
        4. Wearable data
        5. Previous intervention effectiveness
        
        Return a list of interventions with specific times and durations."""

        response = await self.agent.arun(prompt)
        return self._parse_interventions(response)

    def _parse_interventions(self, response: str) -> List[Intervention]:
        # This is a simplified parser - in production, you'd want more robust parsing
        interventions = []
        for line in response.split('\n'):
            if 'Intervention:' in line:
                parts = line.split('|')
                if len(parts) >= 4:
                    intervention = Intervention(
                        type=parts[0].split(':')[1].strip(),
                        duration=int(parts[1].strip()),
                        priority=float(parts[2].strip()),
                        description=parts[3].strip(),
                        scheduled_time=datetime.now() + timedelta(hours=1),  # Simplified
                        conditions={}
                    )
                    interventions.append(intervention)
        return interventions

    # Tool implementations
    def _check_calendar(self, time: str) -> bool:
        # In production, integrate with calendar API
        return True

    def _get_current_state(self, _: str) -> Dict[str, float]:
        # In production, get from digital twin
        return {
            "focus": 0.7,
            "stress": 0.3,
            "energy": 0.6
        }

    def _simulate_intervention(self, intervention: str) -> Dict[str, float]:
        # In production, use digital twin simulation
        return {
            "focus_impact": 0.3,
            "stress_impact": -0.2,
            "energy_impact": 0.4
        }

    def _check_wearable_data(self, _: str) -> Dict[str, float]:
        # In production, integrate with wearable APIs
        return {
            "hrv": 65,
            "sleep_quality": 0.8,
            "activity_level": 0.6
        } 