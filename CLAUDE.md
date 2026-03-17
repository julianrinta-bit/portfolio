# Julian Rinta Portfolio

Single-page portfolio site. One HTML file (`index.html`), no build tools, no framework.

**Stack:** Vanilla HTML/CSS/JS. Fonts from Fontshare (Clash Display, Satoshi) and Google Fonts (JetBrains Mono).

**Aesthetic direction:** Jaguar/Maserati — dark editorial, luxury with power. Acid green (`#c8ff2e`) accent on near-black. No Inter, no purple gradients, no symmetric generic layouts.

---

## DESIGN SKILLS — MANDATORY WORKFLOW

Before writing any CSS or HTML, ALWAYS run:

### MANDATORY ON ALL DESIGN WORK:

1. **ui-ux-pro-max** — Run the design system generator first:
   ```bash
   python3 ~/.claude/plugins/cache/ui-ux-pro-max-skill/ui-ux-pro-max/2.0.1/src/ui-ux-pro-max/scripts/search.py \
     "<project description>" --design-system -p "<project name>"
   ```

2. **frontend-design** (Anthropic official) — Read before implementing.
   BANNED: Inter, Roboto, Arial, Space Grotesk, purple gradients, symmetric generic layouts.

3. **wcag-accessibility-audit** — Run at the end as a quality gate.
   Minimum contrast 4.5:1. No exceptions.

### ACTIVATE BY TASK TYPE:

**Complex redesign or component system:**
- LibreUIUX-Claude-Code (67 specialized agents)

**Interactions, hover states, animations, flip cards:**
- elite-frontend-ux (transitions 150–300ms, prefers-reduced-motion, focus states)

**Improving an existing version:**
- Design Auditor (score /100, 17 professional rules)

**UX flow decisions or information architecture:**
- ux-design wondelai (Norman, Cialdini, user psychology)

### GOLDEN RULE:
Never generate design without running ui-ux-pro-max first. It's like building without blueprints.

### FULL CATALOG OF INSTALLED DESIGN SKILLS:

| Skill | Purpose |
|-------|---------|
| ui-ux-pro-max | 50+ styles, 97 palettes, 57 font pairings, design system generator |
| frontend-design (Anthropic official) | Motion, typography, spatial composition, anti-AI-slop |
| ux-design (wondelai) | UX psychology, Norman principles, Cialdini persuasion |
| bencium-innovative-ux-designer | Bold creative, experimental typography |
| distinctive-frontend | Anti-AI-slop checklist, Cyberpunk/Brutalist/Nordic themes |
| LibreUIUX-Claude-Code | 67 specialized UI/UX agents (design-mastery, brand-systems) |
| elite-frontend-ux | Precision interaction design |
| Design Auditor (bencium) | Quality gate, score /100, 17 professional audit rules |
| wcag-accessibility-audit | WCAG 2.2 compliance, contrast, landmarks, focus states |
| web-design-guidelines (Vercel) | 100+ UI/UX rules, performance, accessibility |
