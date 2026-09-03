---
marp: true
author: Jason Lau
size: 16:9
theme: dracula
paginate: true
transition: fade
class:
- lead
header: "python-dotenv"
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
    .fa-twitter { color: aqua; }
    .fa-mastodon { color: purple; }
    .fa-linkedin { color: blue; }
    .fa-triangle-exclamation
    .fa-window-maximize { color: skyblue; }
    .fa-arrow-alt-circle-right {color: #8be9fd }
    @import 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.3.0/css/all.min.css'
---

# <br><br><br><br>python-dotenv

![bg right width:50%](https://raw.githubusercontent.com/JasonL888/.claude/refs/heads/main/skills/marp_gen/assets/logo.png)

<!--
⏱️ Slide Timing: 1 min

- Welcome and frame the session: how to keep secrets and config out of your source code
- Promise: by the end, everyone will have loaded a real API key from a `.env` file into a script
- Bridge: start with what goes wrong when config is hardcoded
-->

---

# The Problem: Config Baked Into Code
- API keys, passwords, and database URLs get typed straight into `.py` files
- That value is now identical in every environment — dev, staging, production
- `git push` sends it to GitHub, your teammates, and anyone who clones the repo
- Real leaked-key incidents happen constantly — bots scan public GitHub repos for exactly this

<!--
⏱️ Slide Timing: 3 min

- Ask: has anyone ever committed a password or API key by accident?
  - It happens to experienced engineers too — it's a process problem, not a carelessness problem
- Emphasize the scanning-bots point — leaked keys get found and abused within minutes on public repos
- Bridge: show exactly how this plays out vs. the fix
❓ Ask: "If you accidentally committed a real API key, would deleting the file fix it?"
-->

---

# Hardcoded vs. `.env`-Based Config

![center width:1100](Images/dotenv_hardcoded_vs_env.png)

<!--
⏱️ Slide Timing: 5 min

- Left panel: the key lives inside `config.py`, so every `git commit` carries it into permanent history
  - Deleting the line in a later commit does NOT remove it — it's still readable in old commits
- Right panel: the key lives in a `.env` file that's excluded from git entirely by `.gitignore`
  - `load_dotenv()` reads it into the process at runtime; the code never contains the actual value
- This is the one-slide summary of "why dotenv exists" — refer back to it if questions come up later
-->

---

# What `python-dotenv` Does
- Reads `KEY=value` lines from a `.env` file in your project
- Loads each one into `os.environ` — the same place OS-level environment variables live
- Your application code just calls `os.getenv("KEY")` — it never knows or cares where the value came from
- Works identically whether the value came from `.env` locally or a real env var in production

<!--
⏱️ Slide Timing: 3 min

- Key mental model: dotenv doesn't invent a new config system — it simulates environment variables locally
- This is why the same `os.getenv()` call works unchanged when you deploy to a server that sets real env vars
- Bridge: show the flow visually before the demo
-->

---

# How It Flows

![center width:1100](Images/dotenv_flow.png)

<!--
⏱️ Slide Timing: 3 min

- Walk left to right: the `.env` file is just plain text sitting in your project folder
- `load_dotenv()` parses it once and copies every key into `os.environ`
- From that point on, `os.getenv("API_KEY")` behaves exactly like reading a real environment variable
-->

---

# Installation

```bash
# uv-managed project
uv add python-dotenv

# plain venv + pip
pip install python-dotenv
```

- `uv add` — adds `python-dotenv` to `pyproject.toml` and `uv.lock`
- `pip install` — installs into whatever venv is currently activated
- Either way: one dependency, no configuration required to get started

<!--
⏱️ Slide Timing: 1 min

- Keep this short — it's a single command either way
- Use `uv add` in projects that already use `uv`; use `pip install` inside an activated `venv` otherwise
- Reinforce the habit from the venv session: `pip install` only works as expected once a venv is activated
-->

---

# Demo: Create and Load a `.env`

```bash
# 1. Create a .env file in your project root
echo 'API_KEY=demo123' > .env
```

```python
# 2. Load it at the top of your script
from dotenv import load_dotenv
load_dotenv()

# 3. Read the value like any environment variable
import os
print(os.getenv("API_KEY"))   # -> demo123
```

<!--
⏱️ Slide Timing: 4 min

- Live-type this rather than just showing the slide
- Point out `load_dotenv()` must run before the `os.getenv()` call — order matters
- Have students run this on their own machine, confirm they see `demo123` printed
-->

---

# Demo: Missing Keys and Defaults

```python
# Safe: returns None (or your default) if the key is missing
os.getenv("MISSING_KEY")            # -> None
os.getenv("MISSING_KEY", "fallback")  # -> "fallback"

# Unsafe: raises KeyError if the key is missing
os.environ["MISSING_KEY"]
```

- Prefer `os.getenv()` with a sensible default for optional config
- Use `os.environ[...]` only when a missing value should hard-fail the program

<!--
⏱️ Slide Timing: 3 min

- Have students try both lines against a key that doesn't exist in their `.env`
- Discuss when a hard failure is actually the right behavior — e.g. a required production secret
-->

---

# `.gitignore` and `.env.example`

```gitignore
# .gitignore
.env
```

```bash
# .env.example — committed, no real values
API_KEY=your-api-key-here
DATABASE_URL=postgresql://user:pass@localhost/db
```

- `.env` never gets committed — it holds real secrets
- `.env.example` **does** get committed — it documents what variables a teammate needs to set

<!--
⏱️ Slide Timing: 3 min

- This pairing solves the "how do I know what to put in .env" problem for a new teammate cloning the repo
- Good habit: whenever you add a new variable to your own `.env`, add the placeholder to `.env.example` too
-->

---

# Precedence & Gotchas
- **Real environment variables win** — `.env` never overrides an already-set OS env var, unless you pass `override=True`
- **Everything loads as a string** — `os.getenv("PORT")` returns `"8000"`, not `8000`; cast manually with `int(...)`
- **Order matters** — call `load_dotenv()` before any code that reads the variables
- **Path resolution** — `load_dotenv()` searches upward from the current directory by default; pass a path explicitly if needed

<!--
⏱️ Slide Timing: 3 min

- The string-typing gotcha is the most common bug — a numeric-looking env var is still a string until you cast it
- The precedence rule is deliberate: it lets a hosting platform's real env vars override local `.env` values safely
- Mention `find_dotenv()` for cases where the working directory isn't predictable (e.g. running from a subfolder)
-->

---

# Cheat Sheet

| Action | Code |
|---|---|
| Install | `uv add python-dotenv` or `pip install python-dotenv` |
| Load `.env` | `from dotenv import load_dotenv; load_dotenv()` |
| Read a value | `os.getenv("KEY")` |
| Read with default | `os.getenv("KEY", "default")` |
| Cast to int/bool | `int(os.getenv("PORT", "8000"))` |
| Ignore `.env` in git | add `.env` to `.gitignore` |
| Document variables | commit `.env.example` |

<!--
⏱️ Slide Timing: 2 min

- Suggest students screenshot this slide — it's the reference they'll reach for in every future project
-->

---

# References

| Topic | Source |
|-------|--------|
| **`python-dotenv` documentation** | Kostrzewa, T. & contributors. (2026). [python-dotenv](https://github.com/theskumar/python-dotenv). GitHub. |
| **`python-dotenv` on PyPI** | Python Packaging Index. (2026). [python-dotenv](https://pypi.org/project/python-dotenv/). PyPI. |
| **The Twelve-Factor App — Config** | Wiggins, A. (2011–2017). [III. Config](https://12factor.net/config). The Twelve-Factor App. |

<!--
⏱️ Slide Timing: 1 min

- Highest priority to bookmark: the Twelve-Factor App "Config" page — it's the design rationale this whole pattern implements
-->

---

# <br><br>Recap & Practice

- Config and secrets belong in `.env`, not in source code
- `load_dotenv()` + `os.getenv()` is the whole API you need for most projects
- **Before you write a single line of code on your next assignment: add a `.env` and a `.env.example`**

<!--
⏱️ Slide Timing: 2 min

- Close the loop back to the opening problem: this is the fix for secrets ending up in git history
- Practice prompt: have students add `.env` + `.env.example` to their current project right now, before leaving class
-->
