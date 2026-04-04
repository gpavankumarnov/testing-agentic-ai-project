name: Auto Generate README

on:
  push:
    branches: [main]

permissions:
  contents: write   # ✅ THIS FIXES YOUR ERROR

jobs:
  generate-readme:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repo
        uses: actions/checkout@v3

      - name: Debug repo structure
        run: ls -R

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.10"

      - name: Run README generator
        run: python generate_readme.py

      - name: Commit changes
        run: |
          git config --global user.name "github-actions[bot]"
          git config --global user.email "github-actions@github.com"
          git add README.md
          git diff --cached --quiet || git commit -m "Auto update README"
          git push
