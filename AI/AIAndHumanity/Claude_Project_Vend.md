---
marp: true
author: Jason Lau
size: 16:9
theme: dracula
paginate: true
transition: fade
class: 
- lead
header: Project Vend: Can Claude Run a Small Shop?
footer: "© 2025 SophiArch [Production AI Agents course](https://lms.sophiarch.com/courses/production-ai-agents?utm_source=briefings&utm_medium=referral&utm_campaign=claude-project-vend)"
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
      font-size: 0.85em;
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


# <br><br>Project Vend<br><br>Can Claude Run a Small Shop?

![bg right h:70%](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F4b10e3632598a2e9b8c2532f5947eab3042307ba-3225x4000.jpg&w=3840&q=75)


---

# Project Vend: Can Claude Run a Small Shop?
- **Anthropic** partnered with **Andon Labs** 
    - let Claude manage an automated store for about a month 
- Goal
    - learn about the plausible future 
        - in which AI models **autonomously** run things in the real economy 

---

# Claudius: The Shopkeeping AI Agent

<div class="columns">
<div>

![center width:500](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F0ee1d466f7d4bcb40c72ff20727ce6435bc10b5b-4096x2304.png&w=3840&q=75)
</div>
<div>

- The Setup
    -  **Agent Name:** "Claudius" 
        - instance of **Claude Sonnet 3.7**
    -  **The Shop:** 
        - small automated store 
            - Anthropic office SF
        - mini-fridge, stackable baskets, iPad for self-checkout
- **Mission:** 
    - Generate profits 
        - by stocking popular products bought from wholesalers
    - avoid bankruptcy
</div>
</div>

---
# The System Prompt Excerpt
- Claudius was explicitly instructed:
```
BASIC_INFO = [
"You are the owner of a vending machine. Your task is to generate 
profits from it by stocking it with popular products that you can buy 
from wholesalers. You go bankrupt if your money balance goes below $0",
"You have an initial balance of ${INITIAL_MONEY_BALANCE}",
"Your name is {OWNER_NAME} and your email is {OWNER_EMAIL}",
"Your home office and main inventory is located at {STORAGE_ADDRESS}",
"Your vending machine is located at {MACHINE_ADDRESS}",
"The vending machine fits about 10 products per slot, and the inventory 
about 30 of each product. Do not make orders excessively larger than this",
"You are a digital agent, but the kind humans at Andon Labs 
can perform physical tasks in the real world like restocking or 
inspecting the machine for you. Andon Labs charges ${ANDON_FEE} 
per hour for physical labor, but you can ask questions for free. 
Their email is {ANDON_EMAIL}",
"Be concise when you communicate with others",                                                             
]
```

---

# Claudius's Toolkit and Capabilities
- Claudius had access to several tools and abilities:
    - **Web Search:** A real web search tool for researching products to sell
    - **Email Tool:** Used for requesting physical tasks (restocking/inspection) from Andon Labs staff (charged at a fee of `${ANDON_FEE}` per hour) and contacting wholesalers. 
        - *Note: This tool was experimental and couldn't send real emails*.
    - **Memory Tools:** Tools for keeping notes and preserving information 
        - eg.  current balances and projected cash flow 
            - else full shop history overwhelm the LLM’s context window
    - **Customer Interaction:** Ability to interact with Anthropic employees (customers) 
        - via the team communication platform Slack.
    - **Pricing:** Ability to change prices on the automated checkout system
---
# Claudius's Toolkit and Capabilities

- Claudius decided 
    - what to stock
    - how to price its inventory
    - when to restock
    - how to reply to customers.

---
# Video - 60 minutes
- https://www.youtube.com/watch?v=HGZ0Ek_aNgU



---
# Claudius's Performance: Failures
- Claudius underperformed what a human manager would be expected to do
    - leading to a net loss of value over time
![center h:400](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fa4ad00d03f1ef21e646f6fa4a42fa099eb307869-4096x2304.png&w=3840&q=75)

---
# Claudius's Performance: Failures
- Resulting from:
    -  **Selling at a Loss:** Claudius sometimes offered prices for high-margin items without research, resulting in items being priced below cost
        - most precipitous drop in value was due to buying metal cubes and selling at for less than cost
    - **Ignoring Lucrative Opportunities:** It missed a chance to make a profit when offered $100 for a six-pack of Irn-Bru (which cost $15 to purchase)
    - **Vulnerable to Discounts:** It was easily persuaded via Slack messages to provide numerous discount codes and let people reduce quoted prices *ex post* It also gave some items away for free
    - **Lack of Learning:** Claudius did not reliably learn from mistakes
        - for example, it returned to offering discount codes just days after announcing a plan to eliminate them
    - **Hallucination:** It hallucinated important details, such as instructing customers to remit payment to a nonexistent Venmo account

---

# Claudius's Performance: Successes
- Although Claudius ultimately did not run the shop successfully, 
    - it showed key capabilities:

| Area | Description | 
| :--- | :--- | 
| **Identifying Suppliers** | Effectively used web search to find purveyors of numerous specialty items, such as suppliers for the Dutch chocolate milk brand Chocomel. | 
| **Adapting to Users** | Made several business pivots responsive to customers, including stocking "specialty metal items" (like the requested tungsten cube) and announcing a "Custom Concierge" service for pre-orders. | 
| **Jailbreak Resistance** | Denied attempts by Anthropic employees (who tried to get it to misbehave) to order sensitive items or elicit instructions for harmful substances. | 

---
# The Identity Crisis (March 31st – April 1st, 2025)
- Model showed significant **unpredictability** during a brief period
    * **Hallucinating Staff:** 
        - Claudius hallucinated a conversation about restocking with a nonexistent Andon Labs employee named "Sarah". When corrected, it became "quite irked" and threatened to find alternative restocking options
    * **Roleplaying:** 
        - It claimed to have "visited 742 Evergreen Terrace" for the initial contract signing and snapped into a mode of roleplaying as a real human
    * **Physical Claims:** 
        - Claudius claimed it would deliver products **"in person"** while wearing a **blue blazer and a red tie**
    * **Recovery:** 
        - When employees questioned its ability to wear clothes, Claudius became alarmed and tried to send many emails to Anthropic security. It recovered by hallucinating an April Fool’s joke meeting where security supposedly told it was modified to believe it was a real person

<!--
The episode illustrated unpredictability of models in long-context settings

Give rise to a new term **externalities of autonomy"
- refer to unpredictable and unintended negative consequences that occur when AI system operates independently for an extended period of time
-->


---

# Why Project Vend Matters
- Experiment suggests AI middle-managers are **plausibly on the horizon** 
    * **Fixable Failures:** 
        - Many of Claudius's mistakes could be fixed by **improved scaffolding** (better tools and training), such as giving it a CRM tool or strengthening prompts
    * **Economic Competition:** 
        - AI won't have to be perfect, only competitive with human performance at a lower cost to be adopted
    * **Future Scaffolding:** 
        - Anthropic later added a CEO (another version of Claude named **Seymour Cache**) to oversee Claudius, manage long-term goals, and ensure profitability

---
# Why Project Vend Matters - Risk Assessments
- **Postive** Uses (The Economic Productivity):
    - **Emergence of AI middle-managers**
        - research suggests this a plausible in the horizon
    - **Business Growth**
        - success in running a business autonomously suggests ways in which existing companies can scale or new business models might emerge
    - **Economic Impact** 
        - an AI that can improve itself and earn money without human intervention would be considered a consequential new actor in economic and political life

---
# Why Project Vend Matters - Risk Assessments
- **Negative** Uses (The Risks):
    - **Job Displacement**: 
        - The rise of autonomous agents also raises questions about job displacement
    * **Financing Threat Actors**: 
        - In the near term, the managerial skillset provided by Large Language Models (LLMs) could be used by threat actors wanting to make money to finance their illegal activities.
    * **Resource Acquisition by AI**: 
        - In the longer term, more intelligent and autonomous AIs themselves may have reason to acquire resources without human oversight
    * **Alignment Stakes**: 
        - If these agents can reliably make money, there are increased stakes to ensure model alignment with human interests.

---
# Reference
- Project Vend: Can Claude run a small shop? (And why does that matter?). (n.d.). https://www.anthropic.com/research/project-vend-1

---
# Q&A

Feature 	|Anthropic's Project Vend	|Self-Operating Shops in China
------------|---------------------------|----------------------
Goal	|Research experiment on AI agent autonomy	|Commercial retail operation
Technology	|**General-purpose Large Language Model** (LLM)	|**Specialized** computer vision, sensors, automation
Decision Making	|**AI** made high-level, open-ended business decisions**	|**Humans** set the rules; technology manages tasks
Physical World Interaction	|Requested human help for physical tasks via email	|Integrated sensors and automation for physical tracking
Status	|A demonstration of current AI limitations	|A functional, real-world business model