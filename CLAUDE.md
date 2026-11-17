# Julian Rinta Portfolio

Portafolio de una página. **La versión viva es `index-v3.html`, generada por `build.py`** desde
`data/*.json`; no se edita el HTML a mano. `index.html` es la versión anterior y es la que GitHub
Pages sirve todavía como portada.

**Stack:** HTML/CSS/JS a pelo, sin framework. Generador en Python. Tipos: Fraunces y JetBrains Mono (Google), Satoshi (Fontshare).

**Aesthetic direction (REESCRITA 2026-11-10, y la anterior está DEROGADA).** Papel cálido
(`#FBFAF7`), tinta casi negra (`#16140F`), editorial de periodismo de datos: The Pudding,
Bloomberg Graphics, Reuters Graphics. Tipografía Fraunces para titulares, Satoshi para texto,
JetBrains Mono para cifras. Un color por casa, apagado y con autoridad: TheSoul `#2B3A67`,
Bored Panda `#A8432B`, Hype On Media `#1F5F4B`. El color lo pone **el trabajo** (miniaturas,
banners de canal), nunca el fondo.

⛔ **PROHIBIDO el verde ácido `#c8ff2e` sobre casi negro, que es lo que decía esta línea hasta el
2026-11-10.** Esa instrucción produjo la versión que Julian describió como *"una pila de mierda que
parece hecha por IA"*, y neón-sobre-negro con monoespaciada es literalmente la firma visual del
slop. Siguen prohibidas Inter, Roboto, Arial, Space Grotesk y los degradados morados.

⛔ **LAS CIFRAS SALEN DEL EXPEDIENTE, NUNCA DEL SCRAPE.** `Channel_Portfolio_Reference.md` y
`Julian_Master_Profile.json` en el vault son la fuente de toda afirmación. Los JSON de
`_assets/work/` son una bajada de YouTube, no un inventario: cuentan mal los canales, mezclan
roles en dos idiomas e incluyen canales que no son suyos. **Sirven para las FOTOS y para nada
más.** Tres versiones seguidas se cayeron por ignorar esto.

⛔ **COMPUERTA DE FECHA.** Un canal cuya primera pieza es posterior a la salida de Julian de esa
casa NO entra, ni en una cifra ni en una imagen. Salidas: TheSoul `2017-07`, Bored Panda `2024-02`.
Son 15 de 39 los que caen.

⛔ **PRIMERA PERSONA.** Es su portafolio, no una ficha sobre él. Cero "he built", cero "after he
left".

⛔ **ANTES DE PUBLICAR, MIRAR LAS IMÁGENES.** `build.py` no está terminado hasta correr:
```bash
python3 ~/projects/tools/hoja-de-contactos/hoja.py --html index-v3.html
```
y abrir las láminas. Detalle y el porqué: skill `hypeon-imagery`, sección "Human eye QA".

⛔ **UN DATO BIEN MEDIDO PUEDE CONTAR LA HISTORIA CONTRARIA.** El 2026-11-10 se retiró un gráfico
exacto y verificado tres veces porque demostraba que el canal rendía igual sin él: en un
portafolio eso argumenta que es prescindible. Antes de publicar cualquier gráfico, la pregunta no
es sólo si es cierto, es **a favor de quién juega**.

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
