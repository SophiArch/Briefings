---
marp: true
author: Jason Lau
size: 16:9
theme: dracula
paginate: true
transition: fade
class:
- lead
header: "Senior Engineers Need Junior Questions"
footer: "© 2026 SophiArch [lms.sophiarch.com](https://lms.sophiarch.com)"
style: |
    .columns {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 1rem;
    }
    section.lead h1 {
        text-align: center;
    }
    table {
        width: 100%;
    }
    theader {
        font-size: 0.7em;
        text-align: center;
    }
    tbody {
        font-size: 0.6em;
        text-align: left;
    }
    h1 {
        font-size: 1.35em;
    }
    li > strong {
        color: var(--dracula-orange);
    }
    li {
      font-size: 0.9em;
    }
    strong {
        color: var(--dracula-orange);
    }
    blockquote {
        font-size: 0.8em;
        font-style: italic;
    }
    img[alt~="center"] {
        display: block;
        margin: 0 auto;
    }
    .credit {
        font-size: 0.55em;
        text-align: center;
        color: var(--dracula-comment);
    }
    .fa-twitter { color: aqua; }
    .fa-mastodon { color: purple; }
    .fa-linkedin { color: blue; }
    .fa-triangle-exclamation
    .fa-window-maximize { color: skyblue; }
    .fa-arrow-alt-circle-right {color: #8be9fd }
    @import 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.3.0/css/all.min.css'
---

# <br><br><br>Senior Engineers Need Junior Questions

<div class="credit">

A summary of <a href="https://www.cio.com/article/4239726/your-senior-engineers-need-junior-questions-more-than-juniors-need-answers.html"><em>Your senior engineers need junior questions more than juniors need answers</em></a><br>by <strong>Nishant Virmani</strong>, CIO.com, 26 October 2026

</div>

![bg right width:50%](https://raw.githubusercontent.com/JasonL888/.claude/refs/heads/main/skills/marp_gen/assets/logo.png)

<!--
⏱️ Slide Timing: 1 min

- Summary of Nishant Virmani's CIO.com article (26 Oct 2026); title, argument and practices are his
- Topic: what AI assistants quietly take away from engineering teams
- Usual worry: juniors lose mentoring
- This briefing flips it: seniors, and the organisation, may lose more
-->

---

# A Quiet Drop in Interruptions

- Juniors now ask an **AI assistant first**, a senior only if that fails
- In one study, **about half** of 131 developers now ask AI what they once asked a teammate
- **6 in 10** said AI is easier to ask: no fear of looking foolish
- Fewer Slack pings, higher velocity: looks like a **win**
- AI also absorbs the trial and error juniors used to learn from

> Source: UBC & University of Zurich (2026), IEEE TSE study, via Virmani (2026) — see References

<!--
⏱️ Slide Timing: 2 min

- The fear figure matters most: the driver is social, not convenience
  - teams that punish "dumb questions" accelerate this
- Small sample (30 observed, 131 surveyed), so read it as a signal, not a census
- Nobody decided to stop asking seniors; it happened one private chat at a time
❓ Ask: "When did someone last ask you why your system works the way it does?"
-->

---

# Two Sides of the Balance Sheet

<div class="columns">
<div>

**What juniors lose** (widely discussed)

- Less mentoring
- Thinner context
- Shallower feel for production

</div>
<div>

**What seniors lose** (rarely discussed)

- Practice explaining the system
- Fresh eyes on confusing code
- A sharp, current mental model

</div>
</div>

- Senior loss stays hidden because it **looks like focus time**

<!--
⏱️ Slide Timing: 2 min

- The organisation pays seniors to hold the architecture together
  - so their loss is the costlier one
- From the inside, fewer interruptions feel like a pure gain
- The rest of the briefing unpacks the right-hand column
-->

---

# What a Naive Question Actually Did

| Job | What happened |
|---|---|
| **Passed on tacit memory** | Senior tells the story behind a design, e.g. why a service retries three times after a partner's rate-limit incident |
| **Audited for opacity** | Newcomer's confusion shows where the code no longer explains itself |
| **Kept the senior sharp** | Explaining out loud, under follow-up questions, exposes gaps and outdated assumptions |

- All three need a **human on the receiving end**

<!--
⏱️ Slide Timing: 3 min

- Job 1: the "why" behind a design almost never reaches the wiki
  - nobody writes a design doc after the fact unless it breaks again
- Job 2: after three years owning a service, its rough edges feel obvious
- Job 3 is the overlooked one: teachers know you learn by explaining
  - seniors used to get this workout dozens of times a quarter, for free
-->

---

# The Channel Disappears Without an Alarm

- These questions were never on a calendar or in Jira, so **nobody notices** they stopped
- One sprint: silence feels like focus time
- Several quarters: active command of the architecture **erodes**
- Code review only needs **recognition**; outages need **recall** across services
- Refactoring fell from **25% to under 10%** of changes; duplicated code rose **8×**

> Source: GitClear (2025), 211M lines of code analysed, as cited in Virmani (2026) — see References

<!--
⏱️ Slide Timing: 3 min

- Recognition: "that line looks wrong" when it's on screen
- Recall: "if this times out, what happens three services away?" from memory at 2 a.m.
- A junior asking "what if this times out?" used to force seniors to trace that path weekly
- Without the rehearsal, the first live trace happens during the outage
-->

---

# Why Velocity Dashboards Hide the Risk

| Dashboard shows | Underneath |
|---|---|
| Shorter pull request cycle times | Fewer people understand why the code is shaped this way |
| Ticket velocity going up | Juniors close tickets without learning the system |
| Seniors report fewer context switches | Seniors stop rehearsing the architecture |

- Standard metrics don't just miss the erosion, they **read it as progress**

<!--
⏱️ Slide Timing: 2 min

- Aimed at engineering leaders: your green dashboard can be a lagging liability
- Teams can coast on accumulated knowledge for months before it shows
- By the time it shows in a postmortem, the habit has been gone for quarters
-->

---

# Three Risks Building Up

- **Single point of failure:** design reasons stay in veterans' heads; shared ownership was really unshared memory
- **Less stable delivery:** every 25% rise in AI adoption linked to a **7.2% drop** in delivery stability
- **Debugging tax:** in a trial, developers learning a new library with AI scored lowest on **debugging**; seniors pick up the fixes later

> Source: Google DORA (2024); Shen & Tamkin (2026), Anthropic skill formation trial — see References

<!--
⏱️ Slide Timing: 4 min

- DORA shows a correlation, and says its data can't explain why
  - lost senior context is the author's explanation, not DORA's finding
- Stability covers failed changes and how long recovery takes
- Anthropic trial: 52 engineers on an unfamiliar library, so it's about learners, not seniors
- The junior still needs the senior, just later and more expensively
  - from upstream teaching to downstream code forensics
-->

---

# More Documentation Won't Fix It

- First instinct: write more wiki pages, index them into AI search
- That helps **readers** find context
- It doesn't make a veteran **defend trade-offs** or trace failures under questioning
- Banning AI for juniors isn't the answer either
- Optional meetings get cut the moment a deadline hits

> Documentation captures static answers; only live human friction keeps fluency sharp

<!--
⏱️ Slide Timing: 2 min

- The problem isn't missing information, it's missing practice
- Incentives matter: if directors are rewarded only on velocity, coaching loses to the sprint board
- So the fix has to be built into work that already happens
-->

---

# Rebuild the Channel on Purpose

| Moment | Practice |
|---|---|
| **Code review** | 10-minute live walkthrough for changes touching service boundaries, retries or state machines |
| **Between incidents** | Monthly whiteboard walkthrough of a critical workflow, no slides |
| **After an outage** | Service owner explains live how the failure spread, no pasted runbook or AI summary |
| **90-day check-in** | Can the new hire change a core workflow and explain its failure modes without escalating? |

<!--
⏱️ Slide Timing: 4 min

- Code review: junior explains what the code assumes; senior explains why the boundary exists
- Whiteboard: where the explanation stalls is where memory has already decayed
- Postmortem: unscripted explanation under peer questions is the real test of understanding
- 90 days: high early velocity but every structural change still routes to one veteran
  - AI is speeding up surface work while the core stays in one head
-->

---

# Counterpoints and Caveats

- **Fewer juniors to ask:** employment of developers aged 22–25 fell about **20%** from its late-2022 peak
- **AI amplifies, it doesn't decide:** DORA 2025 links AI to higher throughput; stability depends on team foundations
- **Usage style matters:** AI users who asked for explanations scored best; heavy delegators scored worst
- **Old channel had costs:** constant interruptions, and one senior answering everything is a single point of failure
- **Core claim untested:** no study yet measures senior fluency decaying

> Added by SophiArch, not from the original article. Sources: Brynjolfsson et al. (2025); DORA (2025); Shen & Tamkin (2026) — see References

<!--
⏱️ Slide Timing: 3 min

- The argument is plausible, but its statistics support nearby claims, not the central one
- Mechanism rests on learning-by-teaching research (the "protégé effect"), mostly from students
- If junior hiring keeps falling, the questions disappear whatever tools juniors use
- Practical upshot: teach juniors to ask AI "explain why", not just "write this"
❓ Ask: "Which of these counterpoints applies most to your team?"
-->

---

# Key Takeaways

- Junior questions were **free training for seniors**, not just help for juniors
- Their loss looks like focus time, so **no metric flags it**
- Risk shows up as single points of failure and **slower outage recovery**
- Fix: build **live explanation** into review, walkthroughs, postmortems and onboarding
- Stumbling when explaining your own system isn't lost skill; the **practice was automated away**

> Adapted from Nishant Virmani, CIO.com (2026) — read the full article via References

<!--
⏱️ Slide Timing: 2 min

- Keep AI assistants; put the human friction back deliberately
- One action for this week: pick a critical workflow and explain it on a whiteboard to a colleague
- Notice where you hesitate; that's where to start
-->

---

# References — Source and Cited Studies

| Topic | Source |
|---|---|
| **Source article** | Virmani, N. (2026, October 26). [*Your senior engineers need junior questions more than juniors need answers*](https://www.cio.com/article/4239726/your-senior-engineers-need-junior-questions-more-than-juniors-need-answers.html). CIO, First Person |
| **Help-seeking** | University of British Columbia & University of Zurich. (2026). [*From Disruptions to Discussions*](https://ieeexplore.ieee.org/document/11363384/). IEEE Transactions on Software Engineering |
| **Code quality** | GitClear. (2025). [*AI Copilot Code Quality: 2025 Research*](https://www.gitclear.com/ai_assistant_code_quality_2025_research). GitClear |
| **Delivery stability** | Google DORA. (2024). [*Accelerate State of DevOps Report 2024*](https://dora.dev/research/2024/dora-report/). Google Cloud |
| **Skill formation** | Shen, J. H., & Tamkin, A. (2026). [*How AI Impacts Skill Formation*](https://arxiv.org/abs/2601.20245). Anthropic. [Summary](https://www.anthropic.com/research/AI-assistance-coding-skills) |

<!--
⏱️ Slide Timing: 1 min

- Start with Nishant Virmani's article: this deck summarises it, and it links to the original sources
- DORA report is the one to bring to leadership: it ties AI adoption to stability numbers
- Anthropic study is worth reading if you mentor juniors who rely on AI
-->

---

# References — Further Reading

| Topic | Source |
|---|---|
| **AI and delivery, 2025** | Google DORA. (2025). [*State of AI-assisted Software Development 2025*](https://dora.dev/research/2025/dora-report/). Google Cloud |
| **Early-career jobs** | Brynjolfsson, E., Chandar, B., & Chen, R. (2025). [*Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence*](https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/). Stanford Digital Economy Lab |
| **Learning by teaching** | Chase, C. C., Chin, D. B., Oppezzo, M. A., & Schwartz, D. L. (2009). Teachable agents and the protégé effect. *Journal of Science Education and Technology*, 18(4), 334–352 |

<!--
⏱️ Slide Timing: 1 min

- These back the Counterpoints slide; none are cited in the original article
- DORA 2025 updates the 2024 finding the article relies on
- Canaries paper is the strongest data on the shrinking junior pipeline
-->
