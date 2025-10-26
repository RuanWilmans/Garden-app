# Suggested GitHub Issues

## Issue 1 — Refactor & Validation
**Summary**: Refactor the script into functions, replace nested ifs with a data mapping, and add validation/normalisation for inputs.  
**Acceptance Criteria**:
- A `get_advice(season, plant_type)` function exists.
- Advice is stored in a dictionary/object keyed by season → plant type.
- Invalid inputs produce helpful error messages.
- Code is documented with docstrings/comments.

## Issue 2 — Replace hardcoded values with interactivity & docs
**Summary**: Remove hardcoded values. In Python, use `input()`; in JS, use a form (or `prompt`) and update the page. Add a short README and inline comments.  
**Acceptance Criteria**:
- Python version uses `input()`.
- JS version uses a simple form with selects.
- README explains how to run both versions.
- Page is accessible and responsive.
