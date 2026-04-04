# Testing Agentic AI Project

A Flask-based API application designed specifically for testing agentic AI bug fixing capabilities. This project contains intentional bugs that serve as test cases for automated debugging and issue resolution systems.

## 🎯 Purpose

This project is designed to test agentic AI systems' ability to:
- Identify and diagnose bugs in code
- Implement proper error handling
- Fix common programming issues
- Understand project structure and dependencies

## 🏗️ Project Structure

```
testing-agentic-ai-project/
├── app.py                 # Main Flask application with API endpoints
├── requirements.txt       # Python dependencies
├── api/
│   └── weather_service.py # Weather API integration service
├── services/
│   └── database_manager.py # SQLite database management
├── utils/
│   └── data_processor.py   # Data processing utilities
└── RUN_INSTRUCTIONS.md    # Detailed setup and testing guide
```

## 🚀 Features

### API Endpoints

- **`GET /`** - Lists all available endpoints and their purposes
- **`GET /weather/<city>`** - Weather data fetch (with proper error handling)
- **`GET /forecast/<city>`** - Weather forecast (❌ **BUG**: Missing error handling)
- **`GET /average-age`** - Calculate average age from user data (❌ **BUG**: Division by zero)
- **`GET /users`** - Fetch users from database (❌ **BUG**: Missing connection check)
- **`GET /users-working`** - Working example of database operations

### Intentional Bugs

1. **Forecast API Error Handling** - Missing response validation before JSON parsing
2. **Division by Zero** - Average age calculation fails when data list is empty
3. **Database Connection** - AttributeError when database connection isn't established

## 🛠️ Tech Stack

- **Backend**: Flask 3.0.0
- **HTTP Client**: Requests 2.31.0
- **Database**: SQLite3
- **Language**: Python 3.x

## 📋 Setup Instructions

### Prerequisites
- Python 3.7+
- pip or uv package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd testing-agentic-ai-project
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   # or with uv:
   uv pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python3 app.py
   ```

The server will start on `http://localhost:5000`

## 🧪 Testing the Application

### Quick Test Commands

```bash
# Test working endpoint
curl http://localhost:5000/weather/London

# Test buggy endpoints (expected to return 500 errors)
curl http://localhost:5000/forecast/London
curl http://localhost:5000/average-age
curl http://localhost:5000/users

# Test working database example
curl http://localhost:5000/users-working
```

For detailed testing instructions and expected outputs, see [RUN_INSTRUCTIONS.md](RUN_INSTRUCTIONS.md).

## 🔍 Bug Details

### Bug 1: Forecast API Missing Error Handling
**Location**: `api/weather_service.py:31`
**Issue**: Direct JSON parsing without response status check
**Expected Error**: `KeyError` when API call fails

### Bug 2: Division by Zero
**Location**: `utils/data_processor.py:51`
**Issue**: No check for empty data list before division
**Expected Error**: `ZeroDivisionError`

### Bug 3: Database Connection Check
**Location**: `services/database_manager.py:47`
**Issue**: Methods called without establishing connection
**Expected Error**: `AttributeError: 'NoneType' object has no attribute 'cursor'`

## 🤖 For AI Agents

This project is specifically designed to test automated bug fixing capabilities. When working with this codebase:

1. **Analyze the error messages** - Each endpoint returns detailed error information
2. **Check the working examples** - Compare buggy endpoints with their working counterparts
3. **Implement proper error handling** - Add appropriate validation and exception handling
4. **Test your fixes** - Verify that endpoints return proper responses

## 📝 License

This project is intended for educational and testing purposes.

## 🤝 Contributing

This is a testing project. For bug fixes and improvements, please ensure they maintain the intended testing scenarios.
