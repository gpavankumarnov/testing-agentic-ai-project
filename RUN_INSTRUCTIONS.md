# How to Run the Bug Testing API

## Setup

1. Install dependencies:
```bash
source venv/bin/activate
uv pip install -r requirements.txt
```

## Run the Flask App

```bash
python3 app.py
```

The server will start on `http://localhost:5000`

## Test the API Endpoints

### 1. Home Page (List all endpoints)
```bash
curl http://localhost:5000/
```

### 2. Test Weather API (handles errors correctly)
```bash
curl http://localhost:5000/weather/London
```
Expected: Returns `null` gracefully

### 3. **BUG 1: Forecast API - Missing Error Handling**
```bash
curl http://localhost:5000/forecast/London
```
Expected: **500 Error** - KeyError because response isn't checked before accessing JSON

### 4. **BUG 2: Average Age - Division by Zero**
```bash
curl http://localhost:5000/average-age
```
Expected: **500 Error** - ZeroDivisionError when data list is empty

### 5. **BUG 3: Database - Missing Connection Check**
```bash
curl http://localhost:5000/users
```
Expected: **500 Error** - AttributeError because connection is None

### 6. Working Database Example (for comparison)
```bash
curl http://localhost:5000/users-working
```
Expected: **200 Success** - Shows how it works when connection is established

## Expected Bugs Summary

1. **`/forecast/<city>`** - Missing error handling for API failures
2. **`/average-age`** - Division by zero when no data exists
3. **`/users`** - AttributeError when connection not established

These bugs are perfect for testing your multi-agent-github-issue-fixer!
