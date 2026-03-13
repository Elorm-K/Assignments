# UX Personas — *It's My Life* Digital Autobiography App

**Based on:** Milestone 1 interview data (P1–P7) | 2 stakeholder types | 4 coded themes

---

## Persona Structure — Field Justifications

| Field | Why It's Included |
|---|---|
| **Name + Snapshot** | Humanizes the archetype; prevents designing in abstractions (Cooper, 1999) |
| **Goals** | Defines what success looks like from the user's perspective |
| **Needs / Motivations** | Captures what the interface must provide for the user to engage |
| **Pain Points** | Maps to interview evidence; surfaces where the current app fails |
| **Constraints** | Grounds the persona in real-world limits (time, device, access, environment) |
| **Success Criteria** | "It's working if…" — makes goals testable against wireframes |
| **Evidence** | Ties each persona directly to Milestone 1 interview data |

---

## Persona 1 — Dorothy "Dot" Harmon

**Snapshot:** A 74-year-old retired teacher who wants to record her life stories by voice, alone, without waiting for family to help her navigate technology.

**Goals**
- Record voice memories independently, without needing someone present to assist
- Leave a meaningful, permanent life story for her grandchildren
- Use the app without typing — physical limitations make keyboard entry painful
- Complete a recording in a single session without losing progress

**Needs / Motivations**
- A voice-first interface where recording is reachable in 1–2 clicks from the home screen
- Reliable auto-save so she never loses a recording due to inactivity or accidental closure
- No mandatory account creation or login that blocks access before she can try anything
- In-app help that doesn't require calling someone or waiting for a visit
- Consistency — if a button was in one place last time, it must be there next time

**Pain Points / Breakdown Scenario**
- Hands hurt after extended writing, making typing-heavy workflows a hard barrier
- Technology failures leave her stuck for days with no one to ask: any error state with no clear recovery path means she stops and doesn't return
- Multi-step flows cause drop-off: if recording a memory requires navigating more than 2 screens, she abandons the task
- Unfamiliar UI patterns (modal overlays, tooltips that disappear, unlabeled icons) create confusion she can't self-resolve
- Distrust of AI means any unexpected "AI has improved your text" message would feel like a violation, not a feature

**Constraints**
- **Device:** No personal laptop; relies on borrowed family computer during infrequent visits
- **Environment:** Uses the app intermittently — sessions are short and unpredictable
- **Social context:** Limited tech support access; family visits only a few times per month
- **Physical:** Hand pain limits typing; voice is the only sustainable input method long-term
- **Policy:** Uncomfortable with anything that feels like "posting to the internet"

**Success Criteria — "It's working if…"**
- She can press Record, speak her story, and press Save in under 3 minutes with no assistance
- She can re-open the app weeks later and find her recording exactly where she left it
- She never encounters an error message she doesn't understand
- She completes her first memory without asking anyone for help

**Evidence**

| # | Participant | Stakeholder Type | Type | Evidence |
|---|---|---|---|---|
| 1 | P7 | Older Adult | Quote | *"I don't really journal since my hands hurt after writing for a period of time."* |
| 2 | P7 | Older Adult | Quote | *"I don't get visits more than a few times each month so I don't want to have to wait a week or so to ask for help."* |
| 3 | P7 | Older Adult | Quote | *"I just want it to be straightforward, technology can be so irritating and then it doesn't want to work right half the time."* |
| 4 | P7 | Older Adult | Quote | *"Voice recordings would be better since I can talk all day long."* |

**Linked Theme:** Theme 1 — Simplicity and Ease of Use *(minimal steps, intuitive navigation, quick actions)*

---

## Persona 2 — Gloria Reyes

**Snapshot:** A 67-year-old retired administrator with over 15,000 digital photos who needs help organizing and safely archiving her memories — in her own voice, not AI's.

**Goals**
- Sort and browse her large photo library by date without scrolling through years manually
- Add captions and context to selected photos without the interface becoming cluttered
- Export her finished archive to a USB drive or hard drive as a permanent physical backup
- Preserve her written stories exactly as she wrote them — no AI alterations

**Needs / Motivations**
- Chronological or event-based auto-sorting for large photo imports
- A simple tagging or folder system that doesn't require technical knowledge to set up
- Explicit local export functionality (USB / hard drive), not just cloud storage
- Clear confirmation that her files are saved and secure after upload
- Opt-out AI settings that are visible and easy to find, not buried in a settings menu

**Pain Points / Breakdown Scenario**
- Scrolling back through years of photos to find a single image creates cognitive overload and causes her to disengage
- No clear organization system means content accumulates without structure, making the archive feel unmanageable over time
- If the app has no physical export path, she sees it as an incomplete solution — cloud-only storage doesn't meet her mental model of "safe"
- AI making edits she didn't request would feel like a loss of control over her own story
- Unclear save states (no confirmation message, spinner with no resolution) erode trust in the app's reliability

**Constraints**
- **Device:** Home desktop computer; not mobile-first
- **Time:** Willing to invest time in setup, but each session must feel like it made visible progress
- **Access:** Moderate tech comfort — can manage file uploads but won't troubleshoot independently
- **Policy:** Strong ownership mindset around personal content; expects the app to respect that
- **Environment:** Uses the app alone, at home, on her own schedule

**Success Criteria — "It's working if…"**
- She can upload a batch of photos and see them sorted by date automatically
- She can find any specific photo in under 30 seconds using date or event filters
- She can export a curated set to a USB drive in 3 steps or fewer
- Her written text appears exactly as she typed it — no AI edits applied without her action

**Evidence**

| # | Participant | Stakeholder Type | Type | Evidence |
|---|---|---|---|---|
| 1 | P6 | Older Adult | Quote | *"I have 15k photos and would love to put the ones that matter in a safe place."* |
| 2 | P5 | Older Adult | Quote | *"I feel it is overwhelming when I am searching and have to go back many years to find the image."* |
| 3 | P6 | Older Adult | Quote | *"I want to keep my own narrative. I don't want AI modifying the tone of my words."* |
| 4 | P6 | Older Adult | Quote | *"Can I send it to a hard drive or a USB."* |

**Linked Themes:** Theme 4 — Organization and Search Features; Theme 3 — AI Integration Preferences *(narrative ownership, control levels)*

---

## Persona 3 — Sandra Okafor

**Snapshot:** A 52-year-old school administrator who acts as the tech gatekeeper for her aging parent — she won't let the app into her household until she trusts its privacy, security, and respect for authentic voice.

**Goals**
- Evaluate and approve the app's security before setting it up for her parent
- Ensure sensitive family documents (birth certificates, records) are stored safely
- Protect her parent's written voice from being overwritten or "corrected" by AI
- Act as the ongoing support person while her parent uses the app independently

**Needs / Motivations**
- Visible security features (2FA, encryption, privacy policy) on the landing or onboarding screen — not buried in a footer
- AI features that are explicitly opt-in, labeled, and reversible
- A calm, professional visual design that communicates trustworthiness
- Confirmation dialogs when uploading sensitive documents that state how and where the file is stored
- The ability to set up an account on her parent's behalf without creating a confusing dual-ownership situation

**Pain Points / Breakdown Scenario**
- Security information that's hard to find or absent causes her to abandon setup immediately
- Aggressive or alarming UI elements (e.g., a flashing red export button) signal poor design judgment and reduce trust in the entire product
- Any AI feature that activates without explicit user initiation (e.g., auto-rewriting a saved story) would lead her to remove the app
- Privacy policy written in dense legal language reads as a red flag, not a formality
- If she can't recover the archive to a new device in case of hardware failure, the archive feels fragile

**Constraints**
- **Social context:** Decision-maker for a less tech-literate dependent; her approval is the adoption gateway
- **Time:** Evaluates the app in one sitting — proceeds or doesn't
- **Policy:** Professionally conditioned to think about institutional liability and data protection
- **Access:** Moderate-high tech literacy, but evaluating for someone with low literacy
- **Environment:** Sets up and monitors the app on behalf of another user

**Success Criteria — "It's working if…"**
- She can locate the privacy policy, data storage explanation, and security settings within 2 minutes of first opening the app
- She can confirm that uploaded documents are encrypted and not shared with third parties
- Her parent's stories remain exactly as written after any AI interaction
- She can recover or transfer the archive if the primary device fails

**Evidence**

| # | Participant | Stakeholder Type | Type | Evidence |
|---|---|---|---|---|
| 1 | P3 | Family User | Quote | *"Privacy policy, security policy, and 2-factor authentication in case there were to be a leak."* |
| 2 | P3 | Family User | Quote | *"Please get rid of the red export button that flashes; it's very aggressive."* |
| 3 | P3 | Family User | Quote | *"I don't want AI. I'd only use it if it could give me a summary of selected memoirs, trips, or photos and tell me what happened."* |
| 4 | P2 | Family User | Quote | *"It is no longer your story."* (referring to AI editing) |

**Linked Themes:** Theme 2 — Security and Privacy Concerns; Theme 3 — AI Integration Preferences *(control levels, narrative ownership)*

---

## Persona 4 — Marcus Chen

**Snapshot:** A 48-year-old financial analyst who won't recommend or adopt any app until it answers his infrastructure questions: where does the data live, what happens if the device dies, and how is it protected?

**Goals**
- Upload sensitive family documents with confidence they're backed up and recoverable
- Understand the app's data storage model before committing any content to it
- Access the family archive across more than one device
- Act as the household evaluator before recommending the app to older relatives

**Needs / Motivations**
- Plain-language explanation of where data is stored (local vs. cloud) and how it's backed up, visible during or before onboarding
- Automatic or prompted backup functionality with a clear success state
- Cross-device access, or at minimum a manual export path that doesn't require technical steps
- Visible save confirmation every time content is added — no ambiguous spinner states
- A clear security posture: encryption at rest, no third-party data sharing without consent

**Pain Points / Breakdown Scenario**
- If the app gives no indication of how saving works, he uploads one test file and stops — he won't risk real documents on an app that doesn't explain its own behavior
- No backup system is a disqualifying issue: a single hardware failure could wipe everything
- Lack of cross-device access conflicts with his existing workflow
- Unclear data ownership terms in a privacy policy cause him to investigate further or abandon
- An app that doesn't answer infrastructure questions upfront costs him time he won't spend

**Constraints**
- **Device:** Desktop primary; expects phone access as secondary
- **Time:** Evaluates in a single focused session; doesn't return for a second look if first impression fails
- **Access:** High tech literacy — expects modern UX standards around save states and data confirmation
- **Policy:** Professionally sensitive to data liability and breach risk
- **Social context:** Acts as tech proxy and recommender for less technically-literate family members

**Success Criteria — "It's working if…"**
- He can answer "where is my data stored and how is it backed up?" within 2 minutes without contacting support
- Every file upload shows an explicit confirmation: what was saved, when, and where
- He can recover the full archive on a new device if the original is lost
- He recommends the app to his in-laws without reservation

**Evidence**

| # | Participant | Stakeholder Type | Type | Evidence |
|---|---|---|---|---|
| 1 | P1 | Family User | Quote | *"Will I lose my birth certificate uploads if I lose my computer or if it dies?"* |
| 2 | P1 | Family User | Quote | *"Is there a cloud back-up? Is it synced?"* |
| 3 | P1 | Family User | Quote | *"What's the likelihood that there's a security breach?"* |
| 4 | P1 | Family User | Quote | *"How can I sync it with my phone? Is it multi-platform?"* |

**Linked Theme:** Theme 2 — Security and Privacy Concerns *(data protection, secured storage, breach risks)*

---

## Persona 5 — Jordan Rivera

**Snapshot:** A 35-year-old project manager and family tech champion who wants to use every tool the app offers to build a rich archive fast — and then hand it off to her grandmother to browse.

**Goals**
- Build a well-organized family archive efficiently using AI tools and batch operations
- Set up a view that older relatives can navigate without needing a login or tech literacy
- Use AI-assisted writing and captioning to handle volume without sacrificing quality
- Establish a folder and tagging structure the whole family can contribute to over time

**Needs / Motivations**
- Batch upload and bulk-tagging so she's not processing one photo at a time
- AI caption suggestions, writing prompts, and auto-grouping by date or event
- A shareable read-only view link so grandparents can browse without accounts
- Keyboard shortcuts and power-user affordances that don't clutter the simple view for others
- An interface that doesn't remove features in the name of simplicity

**Pain Points / Breakdown Scenario**
- Forced one-at-a-time workflows for large photo sets make the app impractical at scale
- AI tools buried in menus or requiring too many activation steps defeat their purpose
- A view-only mode that requires account creation is a dealbreaker for older relatives she's trying to reach
- Lack of structure (no folders, no tags, no search) makes the archive unusable as it grows
- An app so simplified it removes needed features gets used reluctantly and not recommended

**Constraints**
- **Time:** High productivity expectations — expects meaningful output from a 30-minute session
- **Device:** Desktop and mobile; expects feature parity or graceful degradation on both
- **Social context:** Acts as proxy user, setup lead, and tech support for older relatives
- **Access:** Very high tech literacy; evaluates tools with professional rigor
- **Environment:** Uses the app in focused bursts — a dedicated session every week or two

**Success Criteria — "It's working if…"**
- She can upload, sort, and caption 50+ photos in a single 30-minute session
- Her grandmother can open a shared link and browse photos without creating an account
- AI suggestions appear as optional, editable prompts — not auto-applied changes
- The archive is still browsable and organized 2 years and 500 entries later

**Evidence**

| # | Participant | Stakeholder Type | Type | Evidence |
|---|---|---|---|---|
| 1 | P4 | Family User | Quote | *"The more tools you have to work with, the better."* |
| 2 | P4 | Family User | Quote | *"Something quick I can click on one button without having to do extra steps."* |
| 3 | P4 | Family User | Observation | Only participant who expressed excitement about AI features rather than caution — represents the pro-AI minority design must also serve |
| 4 | P2 | Family User | Quote | *"Probably an hour but that's a lot."* (on time willing to spend scrapbooking) — confirms efficiency tools are essential even for engaged users |

**Linked Themes:** Theme 1 — Simplicity and Ease of Use; Theme 3 — AI Integration Preferences *(excitement, summary utility, tool depth)*

---

## Quick Reference

| # | Persona | Stakeholder Type | Primary Theme | Key Tension |
|---|---|---|---|---|
| 1 | Dorothy "Dot" Harmon | Older Adult | Simplicity | Independence vs. tech complexity |
| 2 | Gloria Reyes | Older Adult | Organization + AI Control | Volume vs. overwhelm |
| 3 | Sandra Okafor | Family User | Security + AI Skepticism | Adoption gatekeeping |
| 4 | Marcus Chen | Family User | Security + Data Safety | Trust before commitment |
| 5 | Jordan Rivera | Family User | Simplicity + AI Enthusiasm | Power use vs. accessible design |
