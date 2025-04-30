from typing import Dict, List, Any
import numpy as np
from datetime import datetime, timedelta
from pydantic import BaseModel

class CognitiveState(BaseModel):
    focus_level: float
    stress_level: float
    energy_level: float
    memory_recall: float
    emotional_state: float
    timestamp: datetime

class DigitalTwin:
    def __init__(self):
        self.state_history: List[CognitiveState] = []
        self.simulation_parameters: Dict[str, Any] = {
            "base_focus_decay": 0.1,
            "stress_impact": 0.2,
            "energy_impact": 0.15,
            "memory_decay": 0.05,
            "emotional_stability": 0.3
        }

    def update_state(self, new_state: CognitiveState):
        """Update the digital twin's current state"""
        self.state_history.append(new_state)
        return self.predict_future_state()

    def predict_future_state(self, hours_ahead: int = 24) -> List[CognitiveState]:
        """Predict future cognitive states based on current state and patterns"""
        if not self.state_history:
            return []

        current_state = self.state_history[-1]
        predictions = []
        
        for hour in range(1, hours_ahead + 1):
            predicted_time = current_state.timestamp + timedelta(hours=hour)
            
            # Simple linear prediction model (can be replaced with more sophisticated ML)
            focus_prediction = max(0, min(1, 
                current_state.focus_level - 
                self.simulation_parameters["base_focus_decay"] * hour +
                np.random.normal(0, 0.1)
            ))
            
            stress_prediction = max(0, min(1,
                current_state.stress_level +
                self.simulation_parameters["stress_impact"] * np.random.normal(0, 0.1)
            ))
            
            energy_prediction = max(0, min(1,
                current_state.energy_level -
                self.simulation_parameters["energy_impact"] * hour +
                np.random.normal(0, 0.1)
            ))
            
            memory_prediction = max(0, min(1,
                current_state.memory_recall -
                self.simulation_parameters["memory_decay"] * hour +
                np.random.normal(0, 0.1)
            ))
            
            emotional_prediction = max(0, min(1,
                current_state.emotional_state +
                self.simulation_parameters["emotional_stability"] * np.random.normal(0, 0.1)
            ))

            predicted_state = CognitiveState(
                focus_level=focus_prediction,
                stress_level=stress_prediction,
                energy_level=energy_prediction,
                memory_recall=memory_prediction,
                emotional_state=emotional_prediction,
                timestamp=predicted_time
            )
            predictions.append(predicted_state)

        return predictions

    def simulate_intervention(self, intervention_type: str, duration: int) -> List[CognitiveState]:
        """Simulate the impact of a specific intervention"""
        if not self.state_history:
            return []

        current_state = self.state_history[-1]
        impact_factors = {
            "meditation": {
                "focus": 0.3,
                "stress": -0.4,
                "energy": 0.1,
                "memory": 0.1,
                "emotional": 0.2
            },
            "exercise": {
                "focus": 0.2,
                "stress": -0.3,
                "energy": 0.4,
                "memory": 0.2,
                "emotional": 0.3
            },
            "nap": {
                "focus": 0.4,
                "stress": -0.2,
                "energy": 0.6,
                "memory": 0.3,
                "emotional": 0.2
            }
        }

        if intervention_type not in impact_factors:
            raise ValueError(f"Unknown intervention type: {intervention_type}")

        impact = impact_factors[intervention_type]
        simulated_states = []

        for minute in range(duration):
            time_delta = timedelta(minutes=minute)
            simulated_time = current_state.timestamp + time_delta

            # Apply intervention impact with diminishing returns
            progress = minute / duration
            focus = current_state.focus_level + impact["focus"] * (1 - progress)
            stress = current_state.stress_level + impact["stress"] * (1 - progress)
            energy = current_state.energy_level + impact["energy"] * (1 - progress)
            memory = current_state.memory_recall + impact["memory"] * (1 - progress)
            emotional = current_state.emotional_state + impact["emotional"] * (1 - progress)

            # Add some noise
            noise = np.random.normal(0, 0.05, 5)
            focus = max(0, min(1, focus + noise[0]))
            stress = max(0, min(1, stress + noise[1]))
            energy = max(0, min(1, energy + noise[2]))
            memory = max(0, min(1, memory + noise[3]))
            emotional = max(0, min(1, emotional + noise[4]))

            simulated_state = CognitiveState(
                focus_level=focus,
                stress_level=stress,
                energy_level=energy,
                memory_recall=memory,
                emotional_state=emotional,
                timestamp=simulated_time
            )
            simulated_states.append(simulated_state)

        return simulated_states 