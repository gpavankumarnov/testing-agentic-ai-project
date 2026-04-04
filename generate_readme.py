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
        # skip .git and workflows
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

## 📌 Description
This project demonstrates an **agentic AI workflow** that interacts with GitHub repositories,
analyzes issues, and automates fixes.

## 🚀 Features
- Multi-agent workflow
- GitHub issue analysis
- Automated PR creation
- Vector DB integration (ChromaDB)

## 📂 Project Structure
``` id="w6ah4p"
{structure}
