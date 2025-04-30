# NeuroX - AI Cognitive Enhancement Platform

#### 🌟 **Concept Overview**
NeuroX (NeuroX - NeuroWave AI) is an **agentic AI cognitive coach** that autonomously designs and adapts personalized brain-training programs by **interfacing with your digital life**, real-world activities, and biometric signals. It acts as a **self-directed mental optimization agent**, continuously learning about your cognitive patterns, habits, goals, and fatigue levels to optimize your mental performance and well-being.

![image](https://github.com/user-attachments/assets/d8f2662b-431c-479c-8552-fedf090b377a)

---

### 🔍 **Key Features**
1. **Dynamic Goal-Aware Planning**  
   Uses large language models and reinforcement learning to assess your long-term cognitive and emotional goals (e.g., “be more focused at work,” “improve memory recall,” “reduce anxiety”), and creates evolving mental training regimens.

2. **Multi-Modal Integration**  
   - Syncs with devices: smartwatches, EEG headbands, sleep trackers, calendars, browsers.
   - Collects behavioral and physiological data: focus levels, heart rate variability, screen time, and sleep quality.

3. **Agentic Autonomy**  
   - Acts independently to schedule micro-interventions throughout your day (e.g., 3-min breathwork, 15-min memory task, adjust lighting, suggest a walk).
   - Cancels or reschedules interventions based on real-time conditions (e.g., you're stressed or in a meeting).

4. **Cognitive Digital Twin Simulation**  
   Builds a simulated cognitive twin that tests out various routines, stressors, or supplements to predict their impact before making real-world suggestions.

5. **Conversational Metacognition Coach**  
   You can talk to NeuroX about why you’re procrastinating, why your focus dipped, or how your memory feels different—like a therapist meets productivity guru meets neuroscientist.

6. **Ethical Feedback Loop**  
   Allows the user to audit, tune, and override the agent's plans, with clear logs of reasoning, uncertainty, and evidence behind each action.

---

### 🚀 Use Cases
- Entrepreneurs, students, and knowledge workers who want to sustain peak mental performance.
- Individuals recovering from cognitive burnout or trauma.
- Professionals in high-stress fields like surgeons or pilots for real-time mental readiness feedback.

---

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- PostgreSQL
- Redis
- Node.js and npm (for frontend development)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd NeuroX
```

### 2. Set Up Python Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate
```

### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
```bash
# Copy the sample environment file
cp .env.example .env

# Edit .env with your actual configuration
# Replace placeholder values with your actual credentials
```

### 5. Set Up Database
```bash
# Initialize the database
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

### 6. Install Frontend Dependencies
```bash
cd frontend
npm install
```

### 7. Start the Application

#### Development Mode
1. Start the backend server:
```bash
# From the root directory
python app.py
```

2. Start the frontend development server:
```bash
# From the frontend directory
npm start
```

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000

#### Production Mode
```bash
# Build the frontend
cd frontend
npm run build

# Start the production server
python app.py --production
```

## Application Structure

```
NeuroX/
├── app.py                 # Main application entry point
├── config.py             # Configuration management
├── models/              # Database models
├── routes/              # API routes
├── services/            # Business logic
├── frontend/            # React frontend
│   ├── public/
│   └── src/
├── tests/               # Test files
└── requirements.txt     # Python dependencies
```

## API Documentation

Once the application is running, you can access the API documentation at:
http://localhost:5000/api/docs

## Testing

Run the test suite:
```bash
python -m pytest
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
