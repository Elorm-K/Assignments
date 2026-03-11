"""
Generates presentation_slides.pptx from the CHI '25 paper slide content.
Upload the output to Google Drive and open with Google Slides.
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt
import copy

# ── Colour palette ──────────────────────────────────────────────────────────
NAVY   = RGBColor(0x1a, 0x2f, 0x5e)
DARK   = RGBColor(0x2c, 0x3e, 0x50)
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT  = RGBColor(0xEC, 0xF0, 0xF1)
GREY   = RGBColor(0x7f, 0x8c, 0x8d)
ACCENT = RGBColor(0xE7, 0x4C, 0x3C)   # red for "presenter" label

SLIDE_W = Inches(13.33)
SLIDE_H = Inches(7.5)

prs = Presentation()
prs.slide_width  = SLIDE_W
prs.slide_height = SLIDE_H

blank_layout = prs.slide_layouts[6]   # completely blank


# ── Helper functions ─────────────────────────────────────────────────────────

def add_rect(slide, left, top, width, height, fill_color=None, line_color=None):
    shape = slide.shapes.add_shape(1, left, top, width, height)  # MSO_SHAPE_TYPE.RECTANGLE
    if fill_color:
        shape.fill.solid()
        shape.fill.fore_color.rgb = fill_color
    else:
        shape.fill.background()
    if line_color:
        shape.line.color.rgb = line_color
    else:
        shape.line.fill.background()
    return shape


def add_textbox(slide, text, left, top, width, height,
                font_size=20, bold=False, color=DARK,
                align=PP_ALIGN.LEFT, wrap=True, italic=False):
    txBox = slide.shapes.add_textbox(left, top, width, height)
    txBox.word_wrap = wrap
    tf = txBox.text_frame
    tf.word_wrap = wrap
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(font_size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    return txBox


def header_bar(slide, title, subtitle=None):
    """Dark navy header bar across the top."""
    bar = add_rect(slide, 0, 0, SLIDE_W, Inches(1.25), fill_color=NAVY)
    add_textbox(slide, title,
                Inches(0.35), Inches(0.15), Inches(12.5), Inches(0.75),
                font_size=28, bold=True, color=WHITE)
    if subtitle:
        add_textbox(slide, subtitle,
                    Inches(0.35), Inches(0.82), Inches(12.5), Inches(0.4),
                    font_size=16, color=LIGHT)


def body_area():
    """Returns (left, top, width, height) for the main content area."""
    return Inches(0.35), Inches(1.4), Inches(12.6), Inches(5.8)


def bullet_block(slide, items, left, top, width, height,
                 font_size=19, indent=False, color=DARK):
    txBox = slide.shapes.add_textbox(left, top, width, height)
    txBox.word_wrap = True
    tf = txBox.text_frame
    tf.word_wrap = True
    first = True
    for item in items:
        if first:
            p = tf.paragraphs[0]
            first = False
        else:
            p = tf.add_paragraph()
        p.space_before = Pt(4)
        run = p.add_run()
        run.text = item
        run.font.size = Pt(font_size)
        run.font.color.rgb = color
        if indent:
            p.level = 1


def add_table(slide, headers, rows, left, top, width, height,
              header_color=NAVY, font_size=17):
    cols = len(headers)
    table = slide.shapes.add_table(len(rows) + 1, cols,
                                   left, top, width, height).table
    col_width = width // cols
    for i, _ in enumerate(headers):
        table.columns[i].width = col_width

    # Header row
    for ci, h in enumerate(headers):
        cell = table.cell(0, ci)
        cell.fill.solid()
        cell.fill.fore_color.rgb = header_color
        p = cell.text_frame.paragraphs[0]
        run = p.add_run()
        run.text = h
        run.font.bold = True
        run.font.size = Pt(font_size)
        run.font.color.rgb = WHITE
        p.alignment = PP_ALIGN.CENTER

    # Data rows
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            cell = table.cell(ri + 1, ci)
            if (ri % 2) == 0:
                cell.fill.solid()
                cell.fill.fore_color.rgb = LIGHT
            else:
                cell.fill.solid()
                cell.fill.fore_color.rgb = WHITE
            p = cell.text_frame.paragraphs[0]
            run = p.add_run()
            run.text = val
            run.font.size = Pt(font_size)
            run.font.color.rgb = DARK
    return table


def page_number(slide, n):
    add_textbox(slide, str(n),
                Inches(12.8), Inches(7.1), Inches(0.4), Inches(0.3),
                font_size=12, color=GREY, align=PP_ALIGN.RIGHT)


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 1 — Title & Citation
# ═══════════════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_rect(sl, 0, 0, SLIDE_W, SLIDE_H, fill_color=NAVY)
add_rect(sl, Inches(0.3), Inches(1.2), Inches(12.7), Inches(4.5),
         fill_color=WHITE)

add_textbox(sl,
    "Generative AI Uses and Risks for\nKnowledge Workers in a Science Organization",
    Inches(0.6), Inches(1.4), Inches(12.1), Inches(1.8),
    font_size=30, bold=True, color=NAVY, wrap=True)

add_textbox(sl,
    "Kelly B. Wagman  ·  Matthew T. Dearing  ·  Marshini Chetty",
    Inches(0.6), Inches(3.1), Inches(12.1), Inches(0.5),
    font_size=18, color=DARK)

add_textbox(sl,
    "University of Chicago  &  Argonne National Laboratory",
    Inches(0.6), Inches(3.55), Inches(12.1), Inches(0.4),
    font_size=16, italic=True, color=GREY)

add_textbox(sl,
    "CHI '25  ·  Yokohama, Japan  ·  April 26–May 1, 2025\nDOI: 10.1145/3706598.3713827",
    Inches(0.6), Inches(4.05), Inches(12.1), Inches(0.7),
    font_size=16, color=DARK)

add_textbox(sl,
    "Presented by: [Your Name]  ·  [Date]",
    Inches(0.6), Inches(6.9), Inches(12.1), Inches(0.4),
    font_size=14, italic=True, color=LIGHT)
page_number(sl, 1)


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 2 — Research Problem
# ═══════════════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
header_bar(sl, "Why This Paper?")
L, T, W, H = body_area()

add_textbox(sl, "The gap:", L, T, W, Inches(0.35),
            font_size=20, bold=True, color=NAVY)
add_textbox(sl,
    "Prior work studied GenAI in science OR in professional knowledge work — "
    "never both, and never with real adoption data from a single organization.",
    L, T + Inches(0.35), W, Inches(0.6), font_size=19)

add_textbox(sl, "What makes science organizations unique:", L, T + Inches(1.1), W,
            Inches(0.35), font_size=20, bold=True, color=NAVY)
bullet_block(sl, [
    "•  Knowledge specialists (scientists) and operations workers (IT, HR, safety) share the same org",
    "•  Sensitive data: classified, pre-publication research, PII",
    "•  Academic publishing norms create distinct ethical stakes",
], L, T + Inches(1.45), W, Inches(1.4))

add_textbox(sl, "The question:", L, T + Inches(2.95), W, Inches(0.35),
            font_size=20, bold=True, color=NAVY)

q_box = add_rect(sl, L, T + Inches(3.3), W, Inches(0.9),
                 fill_color=LIGHT)
add_textbox(sl,
    "Can a science organization safely and effectively adopt generative AI "
    "across all its workers — not just researchers?",
    L + Inches(0.15), T + Inches(3.4), W - Inches(0.3), Inches(0.7),
    font_size=19, italic=True, color=NAVY)
page_number(sl, 2)


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 3 — RQs & Contributions
# ═══════════════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
header_bar(sl, "What They Set Out to Do")
L, T, W, H = body_area()

add_textbox(sl, "RQ1:", L, T, Inches(0.7), Inches(0.35),
            font_size=19, bold=True, color=NAVY)
add_textbox(sl,
    "How are Science and Operations workers using — and envisioning — "
    "generative AI to support their work?",
    L + Inches(0.75), T, W - Inches(0.75), Inches(0.55), font_size=19)

add_textbox(sl, "RQ2:", L, T + Inches(0.65), Inches(0.7), Inches(0.35),
            font_size=19, bold=True, color=NAVY)
add_textbox(sl,
    "What risks (privacy, security, ethics) exist for GenAI at a national lab?",
    L + Inches(0.75), T + Inches(0.65), W - Inches(0.75), Inches(0.4),
    font_size=19)

add_textbox(sl, "Five contributions:", L, T + Inches(1.3), W, Inches(0.35),
            font_size=20, bold=True, color=NAVY)
bullet_block(sl, [
    "1.  Novel Argo usage data from an org-wide GenAI deployment",
    "2.  Use case taxonomy: copilot vs. workflow agent",
    "3.  Risk perspectives from both Science and Operations roles",
    "4.  Design recommendations for organizational copilots and agents",
    "5.  Future HCI research directions for science organizations",
], L, T + Inches(1.65), W, Inches(2.5))
page_number(sl, 3)


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 4 — Study Design
# ═══════════════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
header_bar(sl, "How They Studied It",
           "Argonne National Laboratory  ·  Jan–Aug 2024")
L, T, W, H = body_area()

add_table(sl,
    ["Source", "What", "When"],
    [
        ["Argo telemetry",
         "Monthly unique users, token counts — no query content stored",
         "Jan–Aug 2024"],
        ["Survey (N=66)",
         "Qualtrics; 15 task-frequency items + open-ended responses",
         "Apr–Jun 2024"],
        ["Interviews (N=22)",
         "Semi-structured; 30 min; Zoom; thematic analysis (MAXQDA)",
         "Apr–Jul 2024"],
    ],
    L, T, W, Inches(2.1), font_size=18)

add_textbox(sl, "About Argo:", L, T + Inches(2.3), W, Inches(0.35),
            font_size=19, bold=True, color=NAVY)
bullet_block(sl, [
    "•  Private GPT-3.5 Turbo instance — VPN-only access",
    "•  No query content shared with OpenAI",
    "•  No chat history stored between sessions",
    "•  Upgraded to GPT-4 Turbo after data collection completed",
], L, T + Inches(2.65), W, Inches(1.6))
page_number(sl, 4)


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 5 — Participants
# ═══════════════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
header_bar(sl, "Who Was Studied")
L, T, W, H = body_area()

add_table(sl,
    ["", "Survey (N=66)", "Interviews (N=22)"],
    [
        ["Science / Operations", "48% Science · 47% Ops", "55% Science · 45% Ops"],
        ["Top roles", "Scientists, SW Engineers, IT, Ops Managers",
         "Scientists, Cybersecurity, IT, Ops Managers"],
        ["Gender", "67% male · 18% female", "Skewed male"],
        ["Race / Ethnicity", "70% white", "Skewed white"],
        ["Education", "32% doctoral · 30% master's", "Mostly doctoral (Science)"],
    ],
    L, T, W, Inches(2.6), font_size=17)

add_rect(sl, L, T + Inches(2.8), W, Inches(0.75), fill_color=RGBColor(0xFF, 0xF3, 0xCD))
add_textbox(sl,
    "⚠  Important: Participants self-selected — they are early adopters already "
    "familiar with GenAI. Findings may not reflect the majority of employees.",
    L + Inches(0.15), T + Inches(2.85), W - Inches(0.3), Inches(0.65),
    font_size=17, color=RGBColor(0x7D, 0x60, 0x08))
page_number(sl, 5)


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 6 — Figure 1: Argo Usage
# ═══════════════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
header_bar(sl, "Key Figure 1: Argo Adoption — Growing but Still Small",
           "Reproduced from Figure 1, Wagman et al. (2025)")
L, T, W, H = body_area()

add_table(sl,
    ["Month (2024)", "Science Users", "Operations Users"],
    [
        ["January",  "135", "107"],
        ["February", "101",  "62"],
        ["March",    "111",  "68"],
        ["April",    "113",  "89"],
        ["May",      "130", "123"],
        ["June",     "190", "117"],
        ["July",     "169", "136"],
        ["August",   "256 ▲", "191 ▲"],
    ],
    L, T, Inches(7), Inches(3.5), font_size=18)

add_textbox(sl, "Two things are both true:", L + Inches(7.3), T, Inches(5.1),
            Inches(0.4), font_size=19, bold=True, color=NAVY)
bullet_block(sl, [
    "✓  Clear upward trend: ~19.2% average monthly growth in unique users",
    "",
    "✗  Monthly users never exceeded 10% of all lab employees",
    "    → Use is still largely experimental",
], L + Inches(7.3), T + Inches(0.4), Inches(5.1), Inches(2.5), font_size=18)
page_number(sl, 6)


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 7 — Copilot Use Cases (Table 5 top)
# ═══════════════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
header_bar(sl, "Finding 1: Copilot Use Cases",
           "From Table 5 (Employee Copilot section) — Wagman et al. (2025)")
L, T, W, H = body_area()

add_table(sl,
    ["Use Case", "Science Examples", "Operations Examples"],
    [
        ["Writing structured\ncode / text",
         "Academic paper intros, grants, reports, emails, code",
         "Reports, emails, code"],
        ["Extracting insights from\nlarge unstructured text",
         "Scientific literature; lab rules & regulations",
         "Public data sources; team surveys; meeting transcripts; lab regulations"],
    ],
    L, T, W, Inches(2.2), font_size=17)

add_textbox(sl,
    "Key finding: Science and Operations needs are largely similar for copilot-style tasks",
    L, T + Inches(2.35), W, Inches(0.4), font_size=18, bold=True, color=NAVY)

add_rect(sl, L, T + Inches(2.85), W, Inches(0.9), fill_color=LIGHT)
add_textbox(sl,
    '"Who wants to write these things? But if you take an incident debriefing and ask the '
    'system to write a report based on that... it did a really nice job."  — P2, Operations',
    L + Inches(0.15), T + Inches(2.9), W - Inches(0.3), Inches(0.8),
    font_size=17, italic=True, color=DARK)

add_textbox(sl,
    "Blocker for envisioned uses: hallucinations prevent trust in extracting insights from unverified sources",
    L, T + Inches(3.9), W, Inches(0.4), font_size=17, color=ACCENT)
page_number(sl, 7)


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 8 — Workflow Agent Use Cases (Table 5 bottom)
# ═══════════════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
header_bar(sl, "Finding 2: Workflow Agent Use Cases",
           "From Table 5 (Workflow Agent section) — Wagman et al. (2025)")
L, T, W, H = body_area()

add_table(sl,
    ["Use Case", "Science Examples", "Operations Examples"],
    [
        ["Initial steps toward\nautomation",
         "Operating scientific instruments; automating data analysis pipelines",
         "Automating instrument safety checks"],
        ["Fully automated\nworkflows",
         '"AI scientist": generate hypotheses → run simulations → revise → repeat',
         "Complex project management: Gantt charts, task prioritization, long-term planning"],
    ],
    L, T, W, Inches(2.2), font_size=17)

add_textbox(sl,
    "Key finding: Science and Operations diverge here — workflows are domain-specific and highly customized",
    L, T + Inches(2.35), W, Inches(0.4), font_size=18, bold=True, color=NAVY)

add_rect(sl, L, T + Inches(2.85), W, Inches(0.9), fill_color=LIGHT)
add_textbox(sl,
    '"I would never have been able to write the code without significant time investment, '
    'and the fact that I could produce a working app in a couple of days was impressive to me."'
    '  — P1, Operations (no formal SE training)',
    L + Inches(0.15), T + Inches(2.9), W - Inches(0.3), Inches(0.8),
    font_size=17, italic=True, color=DARK)
page_number(sl, 8)


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 9 — Risks & Concerns
# ═══════════════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
header_bar(sl, "Finding 3: Risks and Concerns")
L, T, W, H = body_area()

add_table(sl,
    ["Concern", "Survey %", "What It Means"],
    [
        ["Reliability / hallucinations", "44%",
         "LLMs not trustworthy for technical/scientific facts; no citations"],
        ["Privacy & security", "42%",
         "Unpublished research, classified data, PII cannot go into commercial LLMs"],
        ["Overreliance", "21%",
         "Others may trust outputs without checking"],
        ["Academic publishing", "20%",
         "Unclear where to draw the line on AI-assisted writing; accountability gaps"],
        ["Job impacts", "5% (survey)*",
         "Concern focused on less-technical roles (Communications, IT)"],
    ],
    L, T, W, Inches(3.0), font_size=17)

add_rect(sl, L, T + Inches(3.15), W, Inches(0.55), fill_color=RGBColor(0xD5, 0xF5, 0xE3))
add_textbox(sl,
    "✓  Also important: 33% had NO ethics concerns at work — presenting only the concerns would misrepresent the data",
    L + Inches(0.15), T + Inches(3.2), W - Inches(0.3), Inches(0.45),
    font_size=16, color=RGBColor(0x1E, 0x8B, 0x4C))

add_textbox(sl, "* Higher prominence in interviews than survey suggests question wording matters",
            L, T + Inches(3.8), W, Inches(0.3), font_size=14, italic=True, color=GREY)
page_number(sl, 9)


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 10 — What Is Compelling
# ═══════════════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
header_bar(sl, "What I Find Compelling", "Presenter's perspective")
add_rect(sl, Inches(0.15), Inches(1.2), Inches(0.18), Inches(6.1),
         fill_color=NAVY)
L, T, W, H = body_area()

items = [
    ("1.  Triangulation is a genuine strength",
     "Behavioral data (Argo telemetry) + self-report (survey) + qualitative (interviews) is rare in HCI "
     "studies of AI adoption. Each data source checks the others."),
    ("2.  The copilot / workflow agent distinction is actionable",
     "It maps directly onto a real organizational decision: one shared chatbot vs. "
     "custom domain automation. The paper's answer: both, but designed differently."),
    ("3.  The Science–Operations similarity finding is counterintuitive",
     "Most assume scientists and admin staff would want completely different tools. "
     "Copilot needs overlap — a shared org-wide tool is defensible."),
    ("4.  P1's story is the most compelling evidence",
     "One Operations employee (no SE background) built a working safety instrument "
     "app in days. A concrete, verifiable productivity claim — not a stated preference."),
]

y = T
for title, body in items:
    add_textbox(sl, title, L, y, W, Inches(0.35), font_size=18,
                bold=True, color=NAVY)
    add_textbox(sl, body, L, y + Inches(0.35), W, Inches(0.5),
                font_size=17, color=DARK)
    y += Inches(1.05)
page_number(sl, 10)


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 11 — What I Don't Buy + Figure 3
# ═══════════════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
header_bar(sl, "What I Don't Buy", "Presenter's critique — evidence-grounded")
L, T, W, H = body_area()

# Figure 3 on the right
add_textbox(sl, "Figure 3 — Wagman et al. (2025)",
            Inches(8.8), T, Inches(4.3), Inches(0.35),
            font_size=15, italic=True, color=GREY)
add_table(sl,
    ["Response", "%"],
    [
        ["Strongly agree",        "7.6%"],
        ["Agree",                 "21.2%"],
        ["Neither / nor",         "21.2%"],
        ["Disagree",              "34.8%"],
        ["Strongly disagree",     "15.2%"],
    ],
    Inches(8.8), T + Inches(0.4), Inches(4.3), Inches(2.0), font_size=16)

add_textbox(sl,
    "Only 28.8% say LLMs are essential — yet 94% are familiar and 82% used ChatGPT.",
    Inches(8.8), T + Inches(2.55), Inches(4.3), Inches(0.6),
    font_size=15, bold=True, color=ACCENT)
add_textbox(sl, '"LLMs have become an essential part of my workflow"',
            Inches(8.8), T + Inches(3.2), Inches(4.3), Inches(0.4),
            font_size=14, italic=True, color=GREY)

# Left: critique bullets
bullet_block(sl, [
    "1.  Early-adopter bias — self-selected participants; non-adopters' views absent",
    "",
    "2.  Single org — Argonne's classified-data concerns are atypically high",
    "     May not transfer to universities or private labs",
    "",
    "3.  Science / Operations binary is too coarse — a software engineer and a",
    "     climate scientist have very different needs; within-group variation unexplored",
    "",
    "4.  Argo undercounts total GenAI use — telemetry misses ChatGPT/Claude/Gemini",
], L, T, Inches(8.2), Inches(4.0), font_size=17)
page_number(sl, 11)


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 12 — What Would I Do Next
# ═══════════════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
header_bar(sl, "What Would I Do Next?", "Presenter's perspective")
L, T, W, H = body_area()

items = [
    ("1.  Longitudinal follow-up at the same lab",
     "Argo was upgraded to GPT-4 after data collection. Would reliability concerns "
     "drop? Would the 28.8% 'essential workflow' figure grow?"),
    ("2.  Multi-organization comparison",
     "University lab vs. national lab vs. private biotech — what's generalizable "
     "vs. context-specific across different data-sensitivity regimes?"),
    ("3.  Study the non-adopters",
     "The 70%+ of employees who did not use Argo are invisible. "
     "Are they unaware? Skeptical? Blocked? These users matter most for policy."),
    ("4.  Audit actual output quality",
     "Participants reported productivity gains. Do AI-assisted emails, reports, "
     "and code hold up under expert review? Self-report and quality can diverge."),
]

y = T
for title, body in items:
    add_textbox(sl, title, L, y, W, Inches(0.35), font_size=18,
                bold=True, color=NAVY)
    add_textbox(sl, body, L, y + Inches(0.35), W, Inches(0.5),
                font_size=17, color=DARK)
    y += Inches(1.05)
page_number(sl, 12)


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 13 — Engagement
# ═══════════════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_rect(sl, 0, 0, SLIDE_W, SLIDE_H, fill_color=NAVY)

add_textbox(sl, "Let's Talk About It",
            Inches(0.5), Inches(0.4), Inches(12.3), Inches(0.7),
            font_size=34, bold=True, color=WHITE)

add_rect(sl, Inches(0.4), Inches(1.3), Inches(12.5), Inches(2.5),
         fill_color=WHITE)
add_textbox(sl,
    "If your department deployed its own private GenAI tool tomorrow — "
    "same interface as ChatGPT, but your data never leaves the organization —\n\n"
    "what's the first task you'd hand off to it,\n"
    "and what's one thing you'd never let it touch?",
    Inches(0.7), Inches(1.5), Inches(12.0), Inches(2.1),
    font_size=22, color=NAVY, wrap=True)

add_textbox(sl, "No right answer — just be honest about where your own line is and why.",
            Inches(0.5), Inches(4.0), Inches(12.3), Inches(0.45),
            font_size=18, italic=True, color=LIGHT)

add_textbox(sl, "Follow-up if the conversation runs:",
            Inches(0.5), Inches(4.65), Inches(12.3), Inches(0.35),
            font_size=17, bold=True, color=WHITE)
add_textbox(sl,
    "The scientists in this study were writing paper introductions with ChatGPT "
    "but hesitant to let it touch their actual data.\n"
    "Does that match how you think about it — or do you draw the line somewhere different?",
    Inches(0.5), Inches(5.05), Inches(12.3), Inches(1.1),
    font_size=17, italic=True, color=LIGHT)
page_number(sl, 13)


# ── Save ────────────────────────────────────────────────────────────────────
out = "/Users/cyril/Documents/ClaudeC/Assignments/presentation_slides.pptx"
prs.save(out)
print(f"Saved → {out}")
