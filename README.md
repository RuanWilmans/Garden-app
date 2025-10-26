# Task 15-008 — Git Workflows (Final Submission)

This folder contains everything required for your submission. It includes both a Python and a JavaScript implementation of **Garden Advice**, a simple static page to exercise Git Issues, Branching and Pull Requests.

## How to reproduce the workflow (exactly as the brief requires)
1. **Create repo**: On GitHub, create a **public** repository named **`garden-app`**. (Requirement 1)
2. **Upload**: Add either `garden_advice.py` or the trio `index.html` + `garden_advice.js` to the repo. (Requirement 2)
3. **Clone**:
   ```bash
   git clone https://github.com/<username>/garden-app.git
   cd garden-app
   ```
4. **Create 2 issues** (Requirement 5). Suggested examples (also saved in `issues.md`):
   - Issue 1: *Refactor into functions + mapping and add input validation*.
   - Issue 2: *Replace hardcoded values with interactive inputs (prompt/select) and add docs*.
5. **Issue workflow** (Requirement 6 & 7). For each issue:
   ```bash
   git pull origin main
   git checkout -b feature/<short-name>   # e.g., feature/refactor
   # make changes …
   git add .
   git commit -m "Implement <short-name> (closes #<issue-number>)"
   git push origin feature/<short-name>
   # On GitHub → Open Pull Request to main → Merge
   ```
6. When both PRs are merged, **close the issues** (they auto-close if you used `closes #n`).
7. Put your repository URL in **repo.txt**. (Requirement 8)

> Tip: The `index.html` is optional for the task, but included so you can demonstrate the JS version working instantly in a browser.

## Files in this submission
- `garden_advice.py` – Interactive, modular Python version
- `garden_advice.js` – Interactive, modular JS module
- `index.html` – Clean one-page UI for the JS version
- `issues.md` – Ready-to-copy issue texts
- `pull_request_templates.md` – Suggested PR titles/descriptions
- `repo.txt` – Paste your GitHub repository link here
- `screenshots/issue1.png`, `issue2.png`, `pr1.png`, `pr2.png`, `merged.png` – placeholders to replace after you complete the Git workflow on GitHub

## How to run locally
- **Python**: `python3 garden_advice.py`
- **JavaScript**: open `index.html` in a browser

All code is formatted, commented, and ready for a clean review.
