import os

def generate_readme():
    content = """# Testing Agentic AI Project

## Description
Auto-generated README.

## Installation
pip install -r requirements.txt

## Usage
python app.py
"""

    with open("README.md", "w") as f:
        f.write(content)

    print("README updated!")

if __name__ == "__main__":
    generate_readme()
