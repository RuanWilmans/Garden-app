"""
Garden Advice – Interactive, modular version

This script gives gardening advice based on season and plant type.
It replaces hardcoded values with user input, adds validation, and
uses functions + a data dictionary for clarity and extensibility.
"""

from typing import Dict

ADVICE_MAP: Dict[str, Dict[str, str]] = {
    "summer": {
        "flower": "Water regularly, mulch lightly, and provide midday shade.",
        "vegetable": "Irrigate deeply 2–3x per week; check for pests daily.",
        "succulent": "Reduce watering; ensure excellent drainage."
    },
    "winter": {
        "flower": "Protect tender blooms with frost cloth; avoid heavy pruning.",
        "vegetable": "Use row covers; water in the morning to reduce frost risk.",
        "succulent": "Keep dry; only water if soil is completely dry for weeks."
    },
    "spring": {
        "flower": "Feed with a balanced fertiliser and deadhead spent blooms.",
        "vegetable": "Prepare beds with compost; sow cool-season crops first.",
        "succulent": "Resume light watering; gradually increase sun exposure."
    },
    "autumn": {
        "flower": "Cut back perennials; add compost to improve soil for winter.",
        "vegetable": "Plant garlic and brassicas; clear spent summer crops.",
        "succulent": "Move pots under cover before first frost."
    }
}

def normalise(value: str) -> str:
    """Normalise and validate a user string (lowercase, trimmed)."""
    return (value or "").strip().lower()

def get_advice(season: str, plant_type: str) -> str:
    """Return advice string for given season and plant type, or a helpful fallback."""
    s = normalise(season)
    p = normalise(plant_type)
    if s in ADVICE_MAP and p in ADVICE_MAP[s]:
        return ADVICE_MAP[s][p]
    # Fallbacks
    if s not in ADVICE_MAP:
        valid_seasons = ", ".join(sorted(ADVICE_MAP.keys()))
        return f"Unknown season '{season}'. Try one of: {valid_seasons}."
    valid_plants = ", ".join(sorted(ADVICE_MAP[s].keys()))
    return f"Unknown plant type '{plant_type}' for season '{season}'. Try one of: {valid_plants}."

def main() -> None:
    print("Welcome to Garden Advice 🌿")
    season = input("Season (summer, winter, spring, autumn): ")
    plant_type = input("Plant type (flower, vegetable, succulent): ")
    print("\nAdvice:")
    print(get_advice(season, plant_type))

if __name__ == "__main__":
    main()
