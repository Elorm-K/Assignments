"""
Generates presentation_slides.pptx — 8-slide restructured deck.
Upload to Google Drive → Open with Google Slides.
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

# ── Palette ──────────────────────────────────────────────────────────────────
NAVY   = RGBColor(0x1a, 0x2f, 0x5e)
DARK   = RGBColor(0x2c, 0x3e, 0x50)
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT  = RGBColor(0xEC, 0xF0, 0xF1)
GREY   = RGBColor(0x7f, 0x8c, 0x8d)
ACCENT = RGBColor(0xE7, 0x4C, 0x3C)
AMBER  = RGBColor(0xFF, 0xF3, 0xCD)
AMBER_T= RGBColor(0x7D, 0x60, 0x08)
GREEN  = RGBColor(0xD5, 0xF5, 0xE3)
GREEN_T= RGBColor(0x1E, 0x8B, 0x4C)

SLIDE_W = Inches(13.33)
SLIDE_H = Inches(7.5)

prs = Presentation()
prs.slide_width  = SLIDE_W
prs.slide_height = SLIDE_H
blank = prs.slide_layouts[6]


# ── Helpers ───────────────────────────────────────────────────────────────────
def rect(slide, l, t, w, h, fill=None, line=None):
    s = slide.shapes.add_shape(1, l, t, w, h)
    s.fill.solid() if fill else s.fill.background()
    if fill: s.fill.fore_color.rgb = fill
    s.line.fill.background() if not line else None
    if line: s.line.color.rgb = line
    return s

def tb(slide, text, l, t, w, h, size=19, bold=False, italic=False,
       color=DARK, align=PP_ALIGN.LEFT):
    box = slide.shapes.add_textbox(l, t, w, h)
    box.word_wrap = True
    tf = box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    r = p.add_run()
    r.text = text
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.italic = italic
    r.font.color.rgb = color
    return box

def bullets(slide, items, l, t, w, h, size=18, color=DARK):
    box = slide.shapes.add_textbox(l, t, w, h)
    box.word_wrap = True
    tf = box.text_frame
    tf.word_wrap = True
    first = True
    for item in items:
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.space_before = Pt(3)
        r = p.add_run()
        r.text = item
        r.font.size = Pt(size)
        r.font.color.rgb = color

def header(slide, title, sub=None):
    rect(slide, 0, 0, SLIDE_W, Inches(1.2), fill=NAVY)
    tb(slide, title, Inches(0.4), Inches(0.1), Inches(12.5), Inches(0.7),
       size=28, bold=True, color=WHITE)
    if sub:
        tb(slide, sub, Inches(0.4), Inches(0.78), Inches(12.5), Inches(0.38),
           size=15, italic=True, color=LIGHT)

def table(slide, headers, rows, l, t, w, h, hdr_color=NAVY, size=17):
    cols = len(headers)
    tbl = slide.shapes.add_table(len(rows)+1, cols, l, t, w, h).table
    cw = w // cols
    for i in range(cols): tbl.columns[i].width = cw
    for ci, h_text in enumerate(headers):
        cell = tbl.cell(0, ci)
        cell.fill.solid(); cell.fill.fore_color.rgb = hdr_color
        p = cell.text_frame.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
        r = p.add_run(); r.text = h_text
        r.font.bold = True; r.font.size = Pt(size); r.font.color.rgb = WHITE
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            cell = tbl.cell(ri+1, ci)
            cell.fill.solid()
            cell.fill.fore_color.rgb = LIGHT if ri % 2 == 0 else WHITE
            p = cell.text_frame.paragraphs[0]
            r = p.add_run(); r.text = val
            r.font.size = Pt(size); r.font.color.rgb = DARK
    return tbl

def pnum(slide, n):
    tb(slide, str(n), Inches(12.8), Inches(7.15), Inches(0.4), Inches(0.3),
       size=12, color=GREY, align=PP_ALIGN.RIGHT)

B = Inches(0.4)   # body left
BT = Inches(1.35) # body top
BW = Inches(12.5) # body width


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 1 — Title
# ═══════════════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
rect(sl, 0, 0, SLIDE_W, SLIDE_H, fill=NAVY)
rect(sl, Inches(0.35), Inches(1.1), Inches(12.6), Inches(5.0), fill=WHITE)

tb(sl,
   "Generative AI Uses and Risks for\nKnowledge Workers in a Science Organization",
   Inches(0.65), Inches(1.3), Inches(12.0), Inches(1.9),
   size=32, bold=True, color=NAVY)

tb(sl,
   "Kelly B. Wagman  ·  Matthew T. Dearing  ·  Marshini Chetty",
   Inches(0.65), Inches(3.15), Inches(12.0), Inches(0.5), size=19, color=DARK)

tb(sl,
   "University of Chicago  &  Argonne National Laboratory",
   Inches(0.65), Inches(3.6), Inches(12.0), Inches(0.4),
   size=16, italic=True, color=GREY)

tb(sl,
   "CHI '25  ·  Yokohama, Japan  ·  April 26–May 1, 2025",
   Inches(0.65), Inches(4.05), Inches(12.0), Inches(0.4), size=16, color=DARK)

tb(sl,
   "DOI: 10.1145/3706598.3713827",
   Inches(0.65), Inches(4.45), Inches(12.0), Inches(0.35),
   size=15, color=RGBColor(0x27, 0x6B, 0xC6))

tb(sl, "Presented by: [Your Name]  ·  [Date]",
   Inches(0.65), Inches(6.9), Inches(12.0), Inches(0.4),
   size=14, italic=True, color=LIGHT)
pnum(sl, 1)


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 2 — Why This Paper
# ═══════════════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
header(sl, "Why This Paper?", "Novelty & Research Questions")

# LEFT column — novelty
tb(sl, "What is novel:", B, BT, Inches(6.0), Inches(0.35),
   size=19, bold=True, color=NAVY)
bullets(sl, [
    "•  First study at the intersection of GenAI in science AND professional knowledge work",
    "•  Combines real usage data (telemetry) with survey and interviews — rare in HCI",
    "•  Includes both Science and Operations workers in a single organization",
    "•  Studies GenAI risks specific to a science context: classified data,",
    "    academic publishing integrity, pre-publication research",
], B, BT + Inches(0.38), Inches(6.0), Inches(2.2))

tb(sl, "The gap it fills:", B, BT + Inches(2.7), Inches(6.0), Inches(0.35),
   size=19, bold=True, color=NAVY)
rect(sl, B, BT + Inches(3.05), Inches(6.0), Inches(0.85), fill=LIGHT)
tb(sl,
   "Prior work studied GenAI for science tasks OR for professional workers —"
   " never both together, and never with organizational adoption data.",
   B + Inches(0.1), BT + Inches(3.1), Inches(5.8), Inches(0.75),
   size=17, italic=True, color=NAVY)

# RIGHT column — RQs
tb(sl, "Research Questions:", Inches(7.0), BT, Inches(5.9), Inches(0.35),
   size=19, bold=True, color=NAVY)

rect(sl, Inches(7.0), BT + Inches(0.38), Inches(5.9), Inches(1.25),
     fill=RGBColor(0xEA, 0xF2, 0xFF))
tb(sl, "RQ1",
   Inches(7.15), BT + Inches(0.45), Inches(0.55), Inches(0.35),
   size=16, bold=True, color=NAVY)
tb(sl,
   "How are Science and Operations workers using — and envisioning — "
   "generative AI to support their work?",
   Inches(7.7), BT + Inches(0.45), Inches(5.05), Inches(0.65), size=16)

rect(sl, Inches(7.0), BT + Inches(1.75), Inches(5.9), Inches(1.1),
     fill=RGBColor(0xEA, 0xF2, 0xFF))
tb(sl, "RQ2",
   Inches(7.15), BT + Inches(1.82), Inches(0.55), Inches(0.35),
   size=16, bold=True, color=NAVY)
tb(sl,
   "What risks (privacy, security, ethics) exist for using "
   "generative AI at a national lab?",
   Inches(7.7), BT + Inches(1.82), Inches(5.05), Inches(0.65), size=16)

tb(sl, "Five contributions:", Inches(7.0), BT + Inches(3.05), Inches(5.9),
   Inches(0.35), size=17, bold=True, color=NAVY)
bullets(sl, [
    "1.  Novel Argo usage data (org-wide GenAI deployment)",
    "2.  Copilot vs. workflow agent use-case taxonomy",
    "3.  Risk perspectives from Science & Operations",
    "4.  Design recommendations for organizations",
    "5.  Future HCI research directions",
], Inches(7.0), BT + Inches(3.42), Inches(5.9), Inches(2.0), size=16)
pnum(sl, 2)


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 3 — Methodology + copilot / agent definitions
# ═══════════════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
header(sl, "Methodology",
       "Argonne National Lab  ·  Jan–Aug 2024  ·  Survey + Interviews + Usage Data")

# Data sources table (top-left)
tb(sl, "Three data sources:", B, BT, Inches(7.5), Inches(0.35),
   size=18, bold=True, color=NAVY)
table(sl,
    ["Source", "N", "Period"],
    [
        ["Argo telemetry (metadata only — no query content)", "All users", "Jan–Aug 2024"],
        ["Survey (Qualtrics, 15 task items + open-ended)",   "N = 66",    "Apr–Jun 2024"],
        ["Semi-structured interviews (30 min, Zoom)",        "N = 22",    "Apr–Jul 2024"],
    ],
    B, BT + Inches(0.38), Inches(7.4), Inches(1.7), size=16)

# Copilot / workflow agent definitions (bottom-left)
tb(sl, "Two interaction modes — the paper's central framework:",
   B, BT + Inches(2.25), Inches(7.4), Inches(0.35),
   size=18, bold=True, color=NAVY)

rect(sl, B, BT + Inches(2.65), Inches(3.55), Inches(1.75),
     fill=RGBColor(0xD6, 0xEA, 0xFF))
tb(sl, "Copilot", B + Inches(0.1), BT + Inches(2.72),
   Inches(3.35), Inches(0.4), size=18, bold=True, color=NAVY)
tb(sl,
   "Conversational, back-and-forth with the user. AI responds in real time.\n"
   "Example: asking ChatGPT to rewrite an email or explain a piece of code.",
   B + Inches(0.1), BT + Inches(3.1), Inches(3.35), Inches(1.2), size=16)

rect(sl, B + Inches(3.75), BT + Inches(2.65), Inches(3.65), Inches(1.75),
     fill=RGBColor(0xD5, 0xF5, 0xE3))
tb(sl, "Workflow Agent", B + Inches(3.85), BT + Inches(2.72),
   Inches(3.45), Inches(0.4), size=18, bold=True, color=RGBColor(0x1E, 0x8B, 0x4C))
tb(sl,
   "Autonomous or semi-autonomous. AI performs a complex task on its own.\n"
   "Example: an agent that downloads instrument data, runs analysis, and produces a graph.",
   B + Inches(3.85), BT + Inches(3.1), Inches(3.45), Inches(1.2), size=16)

# Argo note (right panel)
rect(sl, Inches(8.0), BT, Inches(4.8), Inches(4.45),
     fill=RGBColor(0xF4, 0xF6, 0xF9))
tb(sl, "About Argo (the lab's private GenAI tool):",
   Inches(8.15), BT + Inches(0.08), Inches(4.5), Inches(0.4),
   size=17, bold=True, color=NAVY)
bullets(sl, [
    "•  Private GPT-3.5 Turbo instance",
    "•  VPN-only; no data shared with OpenAI",
    "•  No chat history stored",
    "•  Browser interface — like internal ChatGPT",
    "•  Upgraded to GPT-4 Turbo after study ended",
    "",
    "Participants (survey & interviews):",
    "•  ~48% Science  ·  ~47% Operations",
    "•  Early adopters — already familiar with GenAI",
    "•  67% male, 70% white (reflects lab population)",
], Inches(8.15), BT + Inches(0.52), Inches(4.5), Inches(3.8), size=16)
pnum(sl, 3)


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 4 — Key Results: Adoption + Copilot
# ═══════════════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
header(sl, "Key Results (1): Adoption & Copilot Use Cases",
       "Figure 1 + Table 5 (copilot section) — Wagman et al. (2025)")

# Figure 1 table (left)
tb(sl, "Argo adoption — growing but limited (Figure 1):",
   B, BT, Inches(5.8), Inches(0.35), size=17, bold=True, color=NAVY)
table(sl,
    ["Month", "Science", "Operations"],
    [
        ["Jan", "135", "107"], ["Feb", "101", "62"],
        ["Mar", "111", "68"],  ["Apr", "113", "89"],
        ["May", "130", "123"], ["Jun", "190", "117"],
        ["Jul", "169", "136"], ["Aug", "256 ▲", "191 ▲"],
    ],
    B, BT + Inches(0.38), Inches(5.8), Inches(3.3), size=15)

rect(sl, B, BT + Inches(3.8), Inches(5.8), Inches(0.65),
     fill=AMBER)
tb(sl,
   "⚠  Monthly users never exceeded 10% of all lab employees → use is still experimental",
   B + Inches(0.1), BT + Inches(3.85), Inches(5.6), Inches(0.55),
   size=15, color=AMBER_T)

# Copilot findings (right)
tb(sl, "Copilot use cases (Table 5 — top half):",
   Inches(6.5), BT, Inches(6.4), Inches(0.35), size=17, bold=True, color=NAVY)
table(sl,
    ["Use Case", "Science", "Operations"],
    [
        ["Writing structured\ntext / code",
         "Paper intros, grants, reports, emails, code",
         "Reports, emails, code"],
        ["Extracting insights\nfrom unstructured text",
         "Scientific literature; lab regulations",
         "Team surveys; meeting transcripts; org policies"],
    ],
    Inches(6.5), BT + Inches(0.38), Inches(6.4), Inches(2.0), size=15)

tb(sl, "Key finding:", Inches(6.5), BT + Inches(2.55), Inches(6.4), Inches(0.35),
   size=16, bold=True, color=NAVY)
tb(sl,
   "Science and Operations needs are largely similar for copilot-style tasks — "
   "a single shared tool is defensible.",
   Inches(6.5), BT + Inches(2.9), Inches(6.4), Inches(0.55), size=16)

rect(sl, Inches(6.5), BT + Inches(3.55), Inches(6.4), Inches(0.9), fill=LIGHT)
tb(sl,
   '"Who wants to write these things? But if you take an incident debriefing and '
   'ask the system to write a report... it did a really nice job."  — P2, Operations',
   Inches(6.6), BT + Inches(3.6), Inches(6.2), Inches(0.8),
   size=15, italic=True, color=DARK)
pnum(sl, 4)


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 5 — Key Results: Workflow Agents
# ═══════════════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
header(sl, "Key Results (2): Workflow Agent Use Cases",
       "Table 5 (workflow agent section) — Wagman et al. (2025)")

table(sl,
    ["Use Case", "Science Examples", "Operations Examples"],
    [
        ["Current: Initial steps\ntoward automation",
         "Operating scientific instruments;\nautomating data analysis pipelines",
         "Automating instrument safety checks;\nLLM-driven database queries"],
        ["Envisioned: Fully\nautomated workflows",
         '"AI scientist": generate hypotheses →\nrun simulations → revise → repeat',
         "Auto-generate Gantt charts from meeting\nslides; email organization; task prioritization"],
    ],
    B, BT, BW, Inches(2.5), size=17)

tb(sl, "Key finding:", B, BT + Inches(2.65), BW, Inches(0.35),
   size=18, bold=True, color=NAVY)
tb(sl,
   "Unlike copilot tasks, Science and Operations diverge here — "
   "workflows are highly domain-specific and cannot be served by a single shared tool.",
   B, BT + Inches(3.0), BW, Inches(0.55), size=17)

# Two quotes side by side
rect(sl, B, BT + Inches(3.7), Inches(6.0), Inches(1.6), fill=LIGHT)
tb(sl,
   '"I would never have been able to write the code without significant time '
   'investment, and the fact that I could produce a working app in a couple of '
   'days was impressive to me."\n— P1, Operations (no formal SE training)',
   B + Inches(0.1), BT + Inches(3.75), Inches(5.8), Inches(1.5),
   size=15, italic=True, color=DARK)

rect(sl, Inches(6.7), BT + Inches(3.7), Inches(6.2), Inches(1.6), fill=LIGHT)
tb(sl,
   '"Think about Photoshop — with these large language models, where you can '
   'interact with the chatbot and say: sharpen the image... researchers could '
   'ask the same of a scientific image."\n— P21, Scientist',
   Inches(6.8), BT + Inches(3.75), Inches(6.0), Inches(1.5),
   size=15, italic=True, color=DARK)
pnum(sl, 5)


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 6 — Risks & Concerns
# ═══════════════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
header(sl, "Risks and Concerns")

table(sl,
    ["Concern", "Survey %", "What It Means in Practice"],
    [
        ["Reliability / hallucinations", "44%",
         "LLMs give confident wrong answers; scientists need citable, verifiable sources"],
        ["Privacy & security", "42%",
         "Classified data, PII, and pre-publication research cannot go into commercial LLMs"],
        ["Overreliance", "21%",
         "Users — especially non-experts — may accept outputs without checking"],
        ["Academic publishing", "20%",
         "Unclear where to draw the line on AI-assisted writing; who is accountable for errors?"],
        ["Job impacts", "5% survey\n(higher in interviews)",
         "Concern concentrated on less-technical roles: Communications, IT"],
    ],
    B, BT, BW, Inches(3.35), size=17)

rect(sl, B, BT + Inches(3.5), BW, Inches(0.6), fill=GREEN)
tb(sl,
   "✓  Also important: 33% reported NO ethics concerns at work — "
   "showing only the concerns would misrepresent the distribution of opinion.",
   B + Inches(0.15), BT + Inches(3.55), BW - Inches(0.3), Inches(0.5),
   size=16, color=GREEN_T)

tb(sl,
   "Presenter's note: The privacy/security concern is likely amplified by Argonne's "
   "classified-data environment — it may not transfer equally to other science settings.",
   B, BT + Inches(4.25), BW, Inches(0.5), size=15, italic=True, color=GREY)
pnum(sl, 6)


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 7 — Limitations
# ═══════════════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
header(sl, "Limitations of the Study", "Presenter's critical perspective")

# Three big limitation boxes
lims = [
    ("Only one lab",
     NAVY,
     "Argonne is atypical: classified data, federal employment law, national-security mission. "
     "Concerns about privacy and security are likely higher here than at a university lab or "
     "private biotech. The findings may not generalize beyond similarly security-sensitive orgs."),
    ("No new users studied",
     RGBColor(0x8E, 0x44, 0xAD),
     "70%+ of employees never used Argo in a given month — yet they are invisible in this dataset. "
     "Interviews and surveys only captured enthusiastic early adopters. The barriers for "
     "non-adopters (awareness? skepticism? workflow friction?) are entirely unknown."),
    ("All participants had prior LLM experience",
     RGBColor(0xD3, 0x54, 0x00),
     "94% were already familiar with GenAI; 82% had used ChatGPT. This is not a sample "
     "of the average knowledge worker — it is a self-selected group already sold on the technology. "
     "Stated concerns may therefore be underestimates of what a broader rollout would surface."),
]

y = BT
for title, color, body in lims:
    rect(sl, B, y, BW, Inches(1.65), fill=LIGHT)
    tb(sl, title, B + Inches(0.15), y + Inches(0.1), BW - Inches(0.3), Inches(0.4),
       size=19, bold=True, color=color)
    tb(sl, body, B + Inches(0.15), y + Inches(0.5), BW - Inches(0.3), Inches(1.1),
       size=17, color=DARK)
    y += Inches(1.8)
pnum(sl, 7)


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 8 — Discussion Question
# ═══════════════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank)
rect(sl, 0, 0, SLIDE_W, SLIDE_H, fill=NAVY)

tb(sl, "Let's Talk About It",
   Inches(0.5), Inches(0.35), Inches(12.3), Inches(0.75),
   size=36, bold=True, color=WHITE)

rect(sl, Inches(0.4), Inches(1.25), Inches(12.5), Inches(2.85), fill=WHITE)
tb(sl,
   "If your department deployed its own private GenAI tool tomorrow —\n"
   "same interface as ChatGPT, but your data never leaves the organization —\n\n"
   "what's the first task you'd hand off to it,\n"
   "and what's one thing you'd never let it touch?",
   Inches(0.65), Inches(1.4), Inches(12.0), Inches(2.55),
   size=23, color=NAVY)

tb(sl, "No right answer — be honest about where your own line is and why.",
   Inches(0.5), Inches(4.25), Inches(12.3), Inches(0.45),
   size=18, italic=True, color=LIGHT)

rect(sl, Inches(0.4), Inches(4.85), Inches(12.5), Inches(1.5),
     fill=RGBColor(0x12, 0x22, 0x46))
tb(sl, "Follow-up if the conversation runs:",
   Inches(0.6), Inches(4.92), Inches(12.1), Inches(0.38),
   size=17, bold=True, color=WHITE)
tb(sl,
   "The scientists in this study were writing paper introductions with ChatGPT "
   "but hesitant to let it touch their actual data. "
   "Does that match how you think about it — or do you draw the line somewhere different?",
   Inches(0.6), Inches(5.3), Inches(12.1), Inches(0.95),
   size=17, italic=True, color=LIGHT)
pnum(sl, 8)


# ── Save ──────────────────────────────────────────────────────────────────────
out = "/Users/cyril/Documents/ClaudeC/Assignments/presentation_slides.pptx"
prs.save(out)
print(f"Saved → {out}  ({prs.slides.__len__()} slides)")
