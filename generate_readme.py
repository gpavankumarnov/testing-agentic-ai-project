import os

def read_file_safe(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

def get_requirements():
    content = read_file_safe("requirements.txt")
    return content if content else "No dependencies listed"

def get_project_structure():
    structure = []
    for root, dirs, files in os.walk("."):
        if ".git" in root or ".github" in root:
            continue
        level = root.replace(".", "").count(os.sep)
        indent = "  " * level
        structure.append(f"{indent}{os.path.basename(root)}/")
        subindent = "  " * (level + 1)
        for f in files:
            structure.append(f"{subindent}{f}")
    return "\n".join(structure)

def generate_readme():
    requirements = get_requirements()
    structure = get_project_structure()

    content = f"""
# Testing Agentic AI Project

## Description
Auto-generated README for your agentic AI system.

## Features
- Multi-agent workflow
- GitHub issue fixing
- PR automation

## Project Structure

{structure}

## Installation

pip install -r requirements.txt

## Dependencies

{requirements}

## Usage

python app.py

## Automation
This README is auto-generated via GitHub Actions.
"""

    # Avoid unnecessary commits
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
