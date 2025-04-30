# NeuroWeaver - AI Cognitive Enhancement Platform

A modern web application for cognitive state monitoring and enhancement using AI-powered interventions.

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
cd neuroweaver
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
neuroweaver/
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