// Garden Advice – Interactive, modular version
// Replaces hardcoded values with prompts / form inputs and uses a lookup object.

const ADVICE_MAP = {
  summer: {
    flower: "Water regularly, mulch lightly, and provide midday shade.",
    vegetable: "Irrigate deeply 2–3x per week; check for pests daily.",
    succulent: "Reduce watering; ensure excellent drainage."
  },
  winter: {
    flower: "Protect tender blooms with frost cloth; avoid heavy pruning.",
    vegetable: "Use row covers; water in the morning to reduce frost risk.",
    succulent: "Keep dry; only water if soil is completely dry for weeks."
  },
  spring: {
    flower: "Feed with a balanced fertiliser and deadhead spent blooms.",
    vegetable: "Prepare beds with compost; sow cool-season crops first.",
    succulent: "Resume light watering; gradually increase sun exposure."
  },
  autumn: {
    flower: "Cut back perennials; add compost to improve soil for winter.",
    vegetable: "Plant garlic and brassicas; clear spent summer crops.",
    succulent: "Move pots under cover before first frost."
  }
};

function normalise(v) {
  return (v || "").toString().trim().toLowerCase();
}

export function getAdvice(season, plantType) {
  const s = normalise(season);
  const p = normalise(plantType);
  if (ADVICE_MAP[s] && ADVICE_MAP[s][p]) return ADVICE_MAP[s][p];
  if (!ADVICE_MAP[s]) return `Unknown season '${season}'. Try: ${Object.keys(ADVICE_MAP).join(", ")}.`;
  return `Unknown plant type '${plantType}' for '${season}'. Try: ${Object.keys(ADVICE_MAP[s]).join(", ")}.`;
}

// Hook up a basic UI if present
document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("#advice-form");
  const out = document.querySelector("#advice-output");
  if (!form || !out) return;
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const season = form.season.value;
    const plant = form.plant.value;
    out.textContent = getAdvice(season, plant);
  });
});
