---
marp: true
theme: default
paginate: true
style: |
  section {
    font-size: 26px;
    padding: 40px;
  }
  h1 { color: #1a2f5e; font-size: 36px; }
  h2 { color: #2c3e50; font-size: 30px; }
  table { font-size: 20px; width: 100%; }
  th { background: #1a2f5e; color: white; }
  .presenter-note { color: #7f8c8d; font-style: italic; font-size: 20px; }
  code { font-size: 20px; }
---

<!-- Slide 1: Title & Citation -->
# Generative AI Uses and Risks for Knowledge Workers in a Science Organization

**Kelly B. Wagman · Matthew T. Dearing · Marshini Chetty**
University of Chicago & Argonne National Laboratory

CHI '25 — Yokohama, Japan, April 26–May 1, 2025
DOI: [10.1145/3706598.3713827](https://doi.org/10.1145/3706598.3713827)

---
*Presented by: [Your Name] · [Date]*

---

<!-- Slide 2: Research Problem -->
## Why This Paper?

**The gap:**
Prior work studied GenAI in science OR in professional knowledge work — never both, and never with real adoption data from a single organization

**What makes science organizations unique:**
- Knowledge specialists (scientists) *and* operations workers (IT, HR, safety) share the same org
- Sensitive data: classified, pre-publication research, PII
- Academic publishing norms create distinct ethical stakes

**The question:**
> Can a science organization safely and effectively adopt generative AI across *all* its workers — not just researchers?

---

<!-- Slide 3: Research Questions & Contributions -->
## What They Set Out to Do

**RQ1:** How are Science and Operations workers using — and envisioning — generative AI to support their work?

**RQ2:** What risks (privacy, security, ethics) exist for GenAI at a national lab?

**Five contributions:**
1. Novel Argo usage data from an org-wide GenAI deployment
2. Use case taxonomy: **copilot** vs. **workflow agent**
3. Risk perspectives from both Science and Operations roles
4. Design recommendations for organizational copilots and agents
5. Future HCI research directions for science organizations

---

<!-- Slide 4: Study Design -->
## How They Studied It

**Setting:** Argonne National Laboratory — a US national lab, thousands of employees, science + operations divisions

**Three data sources — collected in parallel (Jan–Aug 2024):**

| Source | What | When |
|--------|------|------|
| **Argo telemetry** | Monthly unique users, token counts — no query content stored | Jan–Aug 2024 |
| **Survey** | N=66 (filtered from 80); Qualtrics; 15 task frequency items + open-ended | Apr–Jun 2024 |
| **Interviews** | N=22 semi-structured; 30 min; Zoom; thematic analysis (MAXQDA) | Apr–Jul 2024 |

**Argo:** Private GPT-3.5 Turbo instance — VPN-only, no data shared with OpenAI, no chat history stored

---

<!-- Slide 5: Participants -->
## Who Was Studied

| | Survey (N=66) | Interviews (N=22) |
|--|--------------|-------------------|
| **Science** | 48% | 55% |
| **Operations** | 47% | 45% |
| **Top roles** | Scientists, Software Engineers, IT, Ops Managers | Scientists, Cybersecurity, IT, Ops Managers |
| **Gender** | 67% male, 18% female | Skewed male |
| **Race/Ethnicity** | 70% white | Skewed white |
| **Education** | 32% doctoral, 30% master's | Mostly doctoral (Science) |

⚠️ **Important:** Participants self-selected — they are **early adopters** already familiar with GenAI. The authors acknowledge this limits generalizability to non-adopters.

---

<!-- Slide 6: Figure 1 — Argo Usage Over Time -->
## Key Figure 1: Argo Adoption — Growing but Still Small

*Reproduced from Figure 1, Wagman et al. (2025)*

| Month | Science Users | Operations Users |
|-------|:-------------:|:----------------:|
| Jan 2024 | 135 | 107 |
| Feb 2024 | 101 | 62 |
| Mar 2024 | 111 | 68 |
| Apr 2024 | 113 | 89 |
| May 2024 | 130 | 123 |
| Jun 2024 | 190 | 117 |
| Jul 2024 | 169 | 136 |
| Aug 2024 | **256** | **191** |

**Two things are both true:**
- Clear upward trend: ~19.2% average monthly growth in unique users
- Monthly users **never exceeded 10% of all lab employees** → use is still experimental

---

<!-- Slide 7: Copilot Use Cases (Table 5 — top half) -->
## Finding 1: Copilot Use Cases

*Reproduced from Table 5 (Employee Copilot section), Wagman et al. (2025)*

| Use Case | Science Examples | Operations Examples |
|----------|-----------------|---------------------|
| **Writing structured code / text** | Academic paper intros, grants, reports, emails, code | Reports, emails, code |
| **Extracting insights from large unstructured text** | Scientific literature; lab rules & regulations | Public data sources; team surveys; meeting transcripts; lab regulations |

**Key finding:** Science and Operations needs are **largely similar** for copilot-style tasks

> *"Who wants to write these things? But if you take an incident debriefing and ask the system to write a report based on that... it did a really nice job."* — P2, Operations

**Blocker for envisioned uses:** Hallucinations prevent trust in extracting insights from unverified sources

---

<!-- Slide 8: Workflow Agent Use Cases (Table 5 — bottom half) -->
## Finding 2: Workflow Agent Use Cases

*Reproduced from Table 5 (Workflow Agent section), Wagman et al. (2025)*

| Use Case | Science Examples | Operations Examples |
|----------|-----------------|---------------------|
| **Initial steps toward automation** | Operating scientific instruments; automating data analysis pipelines | Automating instrument safety checks |
| **Fully automated workflows** | "AI scientist": generate hypotheses → run simulations → revise → repeat | Complex project management: Gantt charts, task prioritization, long-term planning |

**Key finding:** This is where Science and Operations **diverge** — workflows are domain-specific and highly customized

> *"I would never have been able to [write the code] without significant time investment, and the fact that I could produce a working app in a couple of days was impressive to me."* — P1, Operations (no formal SE training)

---

<!-- Slide 9: Risks & Concerns -->
## Finding 3: Risks and Concerns

| Concern | Survey % | What It Means |
|---------|:--------:|---------------|
| Reliability / hallucinations | **44%** | LLMs not trustworthy for technical/scientific facts; no citations |
| Privacy & security | **42%** | Unpublished research, classified data, PII cannot go into commercial LLMs |
| Overreliance | **21%** | Others (not themselves) may trust outputs without checking |
| Academic publishing | **20%** | Unclear where to draw the line on AI-assisted writing; who is accountable for errors? |
| Job impacts | **5%** (survey) | Higher in interviews — concern focused on less-technical roles (Communications, IT) |

⚠️ **Also important:** **33% had NO ethics concerns at work** — presenting only the concerns would misrepresent the distribution

---

<!-- Slide 10: What Is Compelling — Presenter's View -->
## What I Find Compelling *(Presenter's perspective)*

**1. Triangulation is a genuine strength**
Behavioral data (Argo telemetry) + self-report (survey) + qualitative (interviews) — rare in HCI studies of AI adoption. Each data source checks the others.

**2. The copilot / workflow agent distinction is actionable**
It maps directly onto a real organizational decision: "Should we deploy one shared chatbot, or fund teams to build custom automation?" The paper's answer: both, but differently designed.

**3. The Science–Operations similarity finding is counterintuitive and useful**
Most people assume scientists and admin staff would want completely different tools. The paper shows their copilot needs overlap significantly — a shared org-wide tool is defensible.

**4. P1's story (Operations, no SE background) is the most compelling evidence**
One person built a working safety instrument app in days with no formal training. This is a concrete, verifiable productivity claim — not a vague stated preference.

---

<!-- Slide 11: What I Don't Buy — Presenter's Critique -->
## What I Don't Buy *(Presenter's perspective)*

**Figure 3 from Wagman et al. (2025) — "LLMs as Essential Workflow":**

| Response | % |
|----------|:-:|
| Strongly agree | 7.6% |
| Agree | 21.2% |
| Neither agree nor disagree | 21.2% |
| **Disagree** | **34.8%** |
| **Strongly disagree** | **15.2%** |

Only **28.8%** say LLMs are essential — yet 94% are familiar and 82% have used ChatGPT. **That gap is the real story, and the paper doesn't fully explain it.**

**Four other critiques:**
- **Early-adopter bias:** Self-selected participants; non-adopters' views are absent
- **Single org:** Argonne's classified-data concerns are atypically high — may not transfer to universities or private labs
- **Science/Operations binary is too coarse:** A software engineer and a climate scientist have very different needs; within-group variation is unexplored
- **Argo undercounts total GenAI use:** Telemetry only captures one tool; the real adoption picture requires counting ChatGPT/Claude/Gemini use too

---

<!-- Slide 12: What Would I Do Next? -->
## What Would I Do Next? *(Presenter's perspective)*

**1. Longitudinal follow-up at the same lab**
Argo was upgraded to GPT-4 after data collection. Would reliability concerns drop? Would the 28.8% "essential workflow" figure grow? Re-surveying the same population would answer this.

**2. Multi-organization comparison**
University lab vs. national lab vs. private biotech — all science contexts, but different data sensitivity, publishing norms, and funding structures. What's generalizable vs. context-specific?

**3. Study the non-adopters**
The 70%+ of employees who did not use Argo each month are invisible in this dataset. Are they unaware? Skeptical? Blocked by workflow? These users matter most for organizational policy.

**4. Audit actual output quality**
Participants *reported* productivity gains. Do the AI-assisted emails, reports, and code products hold up under expert review? Self-report and output quality can diverge substantially.

---

<!-- Slide 13: Engagement Activity -->
## Let's Think Together

**Turn-and-talk (3 minutes):**

> Think of one task you do regularly — academic or professional.
> Is your current or imagined GenAI use for that task best described as a **copilot** (conversational, back-and-forth) or a **workflow agent** (autonomous, runs on its own)?
> What would have to change — technically *or* organizationally — for you to trust an agent with it?

*Share with a partner → 2–3 responses to the group*

---

**Backup discussion question** *(if the activity stalls):*

> The paper found 44% of respondents worried about hallucinations — yet 82% had already used ChatGPT anyway.
> What explains the gap between stated concern and actual behavior?
> Is it rational, or is it a form of risk normalization?
