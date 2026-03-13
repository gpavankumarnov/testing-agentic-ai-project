from flask import Flask, jsonify, request
from api.weather_service import WeatherService
from utils.data_processor import DataProcessor
from services.database_manager import DatabaseManager
import os

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(
        {
            "message": "Bug Testing API",
            "endpoints": {
                "/weather/<city>": "Test weather API (will fail with invalid key)",
                "/forecast/<city>": "Test forecast API - BUG: Missing error handling",
                "/average-age": "Test average age calculation - BUG: Division by zero",
                "/users": "Test database without connection - BUG: AttributeError",
                "/users-working": "Test database with proper connection (working)",
            },
        }
    )


@app.route("/weather/<city>", methods=["GET"])
def get_weather(city):
    try:
        service = WeatherService(api_key="INVALID_API_KEY")
        result = service.get_weather(city)
        return jsonify({"success": True, "data": result})
    except Exception as e:
        return (
            jsonify({"success": False, "error": str(e), "type": type(e).__name__}),
            500,
        )


@app.route("/forecast/<city>")
def get_forecast(city):
    try:
        service = WeatherService(api_key="INVALID_API_KEY")
        result = service.get_forecast(city)
        return jsonify({"success": True, "data": result})
    except Exception as e:
        return (
            jsonify(
                {
                    "success": False,
                    "error": str(e),
                    "type": type(e).__name__,
                    "bug": "Missing error handling in get_forecast method",
                }
            ),
            500,
        )


@app.route("/average-age", methods=["GET"])
def get_average_age():
    try:
        processor = DataProcessor()
        avg = processor.get_average_age()
        return jsonify({"success": True, "average_age": avg})
    except ZeroDivisionError as e:
        return (
            jsonify(
                {
                    "success": False,
                    "error": str(e),
                    "type": "ZeroDivisionError",
                    "bug": "Division by zero when data list is empty",
                }
            ),
            500,
        )


@app.route("/users", methods=["GET"])
def get_users_buggy():
    try:
        db = DatabaseManager("test.db")
        users = db.get_all_users()
        return jsonify({"success": True, "users": users})
    except AttributeError as e:
        return (
            jsonify(
                {
                    "success": False,
                    "error": str(e),
                    "type": "AttributeError",
                    "bug": "Connection not established before calling get_all_users",
                }
            ),
            500,
        )


@app.route("/users-working", methods=["GET"])
def get_users_working():
    try:
        db = DatabaseManager("test.db")
        db.connect()
        db.create_users_table()

        user_id = db.insert_user("testuser", "test@example.com")
        users = db.get_all_users()
        db.close()

        return jsonify({"success": True, "users": users})
    except Exception as e:
        return (
            jsonify({"success": False, "error": str(e), "type": type(e).__name__}),
            500,
        )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
