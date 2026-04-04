import os

def read_file(path, max_chars=1000):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()[:max_chars]
    return ""

def get_requirements():
    return read_file("requirements.txt") or "No dependencies listed"

def list_dirs():
    structure = []
    for folder in ["api", "services", "utils"]:
        if os.path.exists(folder):
            files = os.listdir(folder)
            structure.append(f"{folder}/ -> {', '.join(files)}")
    return "\n".join(structure) if structure else "No structured folders found"

def summarize_app():
    content = read_file("app.py", 800)
    if not content:
        return "Main app logic not found"

    # naive summary (can upgrade later to LLM)
    lines = content.split("\n")[:20]
    return "\n".join(lines)

def generate_readme():
    requirements = get_requirements()
    structure = list_dirs()
    app_summary = summarize_app()

    content = f"""
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
{structure}

## 🚀 Main Application Logic (app.py snippet)
{app_summary}

## ⚙️ Installation
pip install -r requirements.txt

## 📦 Dependencies
{requirements}

## ▶️ Usage
python app.py

## 🤖 Automation
This README is auto-generated via GitHub Actions.
"""

    # avoid unnecessary commits
    if os.path.exists("README.md"):
        with open("README.md", "r", encoding="utf-8") as f:
            old = f.read()
        if old.strip() == content.strip():
            print("No changes in README")
            return

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

    print("README updated!")

if __name__ == "__main__":
    generate_readme()
