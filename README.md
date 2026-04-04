
# Testing Agentic AI Project

## 📌 Overview
This project implements an **agentic AI workflow** that:
- Takes a GitHub repo URL
- Analyzes issues
- Uses multiple agents to fix problems
- Creates automated PRs

## 🧠 How It Works
- User inputs repo + issue
- Agents process code using embeddings (ChromaDB)
- System generates fixes
- PR is created automatically

## 📂 Project Structure
api/ -> weather_service.py
services/ -> database_manager.py
utils/ -> data_processor.py

## 🚀 Main Application Logic (app.py snippet)
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

## ⚙️ Installation
pip install -r requirements.txt

## 📦 Dependencies
requests==2.31.0
flask==3.0.0


## ▶️ Usage
python app.py

## 🤖 Automation
This README is auto-generated via GitHub Actions.
