# Production-Ready AI Systems — Introduction & Security in GenAI

## 1. Main Goal of the Course

The **major objective** of this course/bootcamp is:

> **To understand how to build production-ready AI systems.**

The focus is not merely on building an AI application that works, but on building an AI application that is:

- Secure
- Observable
- Reliable
- Governed
- Evaluated
- Protected against attacks
- Suitable for enterprise/production environments

### Types of AI applications that may need to be built

In an industry environment, you may be asked to develop:

- **RAG systems**
- **Agentic AI applications**
- **AI agents**
- Simple LLM/chat applications
- AI-powered workflows

Building the basic application itself is relatively easy because frameworks such as:

- LangChain
- LangGraph
- LLM APIs
- Agentic AI frameworks

can simplify application development.

However:

> **Building an application ≠ building a production-ready AI system.**

A production system needs several additional layers around the core AI application.

---

# 2. What Does "Production-Ready AI System" Mean?

A production-ready AI system considers concerns beyond simply generating an answer.

Important components include:

### 1. Security
Protect the application, users, data, models, tools, and infrastructure from attacks and misuse.

### 2. Observability
Understand what is happening inside the AI system.

For example:

- What input was received?
- Which model was called?
- What tools were invoked?
- How long did the request take?
- What output was generated?
- Where did an error occur?
- How much did a request cost?

### 3. Guardrails
Rules and controls that restrict inappropriate inputs and outputs.

They can help prevent:

- Harmful requests
- Sensitive-data leakage
- Prompt injection
- Unsafe outputs
- Policy violations

### 4. LLM Gateways
A control layer between applications and LLM providers.

It can provide centralized control over:

- Model access
- Security
- Routing
- Monitoring
- Policies
- Costs
- Rate limits

### 5. Evaluation
Continuously measure whether the AI system is actually performing correctly.

Examples:

- Answer quality
- Relevance
- Factuality
- Hallucination
- Safety
- Retrieval quality

### 6. Governance
Ensure that the AI application follows organizational, legal, regulatory, and ethical requirements.

---

# 3. Typical GenAI Application Architecture

A typical GenAI architecture can be represented conceptually as:

```text
User
  ↓
Chat / Application Interface
  ↓
AI Application / Orchestration
  ↓
Workflow / Agentic AI / RAG
  ↓
LLM
  ↓
Output
```

But a real application can be considerably more complex.

A more complete architecture can contain:

```text
                 ┌──────────────────────┐
                 │   User / Chat App    │
                 └──────────┬───────────┘
                            ↓
                 ┌──────────────────────┐
                 │ AI Application /     │
                 │ Orchestration Layer  │
                 └──────────┬───────────┘
                            ↓
              ┌─────────────┴─────────────┐
              ↓                           ↓
         RAG / Workflow              AI Agent
              ↓                           ↓
       Vector Database              Tools / APIs
              │                     MCP / Browser
              └─────────────┬─────────────┘
                            ↓
                       LLM Model
                            ↓
                         Output
```

---

# 4. AI Application / Orchestration Layer

The **AI application** or orchestration layer controls the overall workflow.

It could be:

- A simple chatbot
- A RAG application
- An agentic AI application
- An AI agent
- A workflow involving multiple LLM calls and tools

Frameworks such as:

- **LangChain**
- **LangGraph**

can be used to implement these workflows.

---

# 5. LLM Layer

The application can use different LLM providers/models.

Examples mentioned in the lecture:

### OpenAI
OpenAI LLM models.

### Anthropic
Anthropic's Claude models.

### Google
Google Gemini models.

The architecture should ideally not be tightly dependent on a single model provider.

---

# 6. Data Sources in RAG

If the application is a **RAG (Retrieval-Augmented Generation)** system, it will typically have external data sources.

For example:

```text
Documents
   ↓
Embeddings
   ↓
Vector Database
   ↓
Retriever
   ↓
Relevant Context
   ↓
LLM
```

Examples of data that might be stored/retrieved:

- Company documents
- PDFs
- Knowledge bases
- Internal databases
- Customer information
- Product information

A **vector database** therefore becomes another important component that needs security.

---

# 7. Tool Integrations

Modern AI applications frequently interact with external tools.

These can include:

- APIs
- Databases
- Browsers
- External services
- Internal enterprise systems
- MCP servers/tools

MCP stands for **Model Context Protocol**.

An AI agent might therefore have the ability to:

```text
LLM
 ├── Database
 ├── API
 ├── Browser
 ├── File System
 ├── MCP Tool
 └── Enterprise Application
```

This greatly increases the capabilities of the AI system.

However, it also **greatly increases the attack surface**.

---

# 8. Why Does GenAI Introduce New Security Risks?

Traditional software already has security concerns.

GenAI applications introduce additional risks because the system is capable of:

- Understanding natural-language instructions
- Generating dynamic outputs
- Calling tools
- Accessing data
- Interacting with external systems
- Making decisions
- Executing workflows

Therefore, the AI system can potentially be manipulated through natural language.

This creates a **new attack surface**.

---

# 9. Major Risks in GenAI Applications

The lecture identifies several major risks.

---

## 9.1 Untrusted Inputs

One of the biggest concerns is **untrusted user input**.

Users can provide information that should **never be exposed to an LLM**.

### Example: Credit Card Number

Suppose a user enters:

```text
My credit card number is XXXXXXXX...
```

A credit card number is sensitive financial information.

It should not unnecessarily be sent to an LLM.

Similarly, users may enter:

- Government IDs
- Driving licence numbers
- Personal identifiers
- Confidential company information
- Source code
- Proprietary information

Therefore:

> Sensitive information should be detected and protected before it reaches the LLM.

This is one of the reasons **input guardrails** are important.

---

# 10. Sensitive Data / PII

GenAI systems may process large amounts of sensitive information.

Examples include:

### Personal information

- Names
- Addresses
- Phone numbers
- Email addresses
- Government IDs

### Financial information

- Credit card numbers
- Bank information
- Financial records

### Enterprise information

- Proprietary information
- Internal documents
- Source code
- Business data
- Confidential information

The system needs mechanisms to prevent accidental exposure.

---

# 11. Unpredictable Outputs

Another major risk is **unpredictable or unsafe model output**.

LLMs do not always produce deterministic or perfectly controlled responses.

For example, a user could ask:

> "How do I hack a banking website?"

A production AI system should not simply provide detailed instructions for compromising a financial system.

The application therefore needs controls that determine:

```text
User Input
     ↓
Is this request allowed?
     ↓
Yes → Process
No  → Block / Refuse / Redirect
```

This is another reason why **guardrails and policies** are necessary.

---

# 12. Hallucination

LLMs can generate information that sounds convincing but is incorrect.

This is called a:

> **Hallucination**

The problem becomes particularly serious in high-impact domains.

Examples:

- Financial information
- Legal information
- Healthcare information
- Enterprise decision-making

An LLM may confidently provide an incorrect answer.

Therefore, production AI systems need mechanisms to:

- Evaluate responses
- Ground answers in trusted sources
- Monitor hallucinations
- Apply domain-specific guardrails
- Validate outputs

---

# 13. Harmful or Biased Outputs

LLMs can potentially generate:

- Harmful information
- Biased responses
- Incorrect information
- Unsafe advice
- Policy-violating content

The lecture highlights that this can become especially dangerous when the user is vulnerable.

For example, if someone is experiencing severe emotional distress and the model provides an inappropriate or harmful response, the consequences can be serious.

Therefore:

> AI safety is not merely a technical concern; model behavior can have real-world consequences.

---

# 14. Data Leakage

**Data leakage** occurs when sensitive or confidential information is unintentionally exposed.

Potential sources include:

- User inputs
- LLM prompts
- LLM outputs
- Logs
- Vector databases
- Tool calls
- APIs
- Application interfaces

For example:

```text
User
 ↓
Sensitive information
 ↓
Prompt
 ↓
LLM
 ↓
Logs / Monitoring
```

If security is poorly designed, sensitive information could appear in logs or other systems.

Therefore sensitive data must be protected throughout the entire AI pipeline.

---

# 15. Prompt Injection

One of the most important GenAI-specific security risks is:

> **Prompt Injection**

The attacker attempts to manipulate the instructions given to the model.

The attacker may try to make the model:

- Ignore system instructions
- Reveal confidential information
- Reveal hidden prompts
- Perform unauthorized actions
- Access restricted information
- Follow malicious instructions

Conceptually:

```text
System Instructions
        +
User Input
        ↓
    LLM
        ↓
Potentially manipulated behavior
```

Prompt injection becomes particularly dangerous when the LLM has access to tools or sensitive data.

---

# 16. Jailbreaking

**Jailbreaking** refers to attempts to bypass the model's safety restrictions or policies.

The attacker tries to make the model behave outside its intended boundaries.

For example, attempting to persuade the model to provide content that it is designed to refuse.

Therefore production applications need mechanisms to detect and mitigate jailbreak attempts.

---

# 17. Insecure Integrations

Modern GenAI systems connect to many external components:

- APIs
- Databases
- Tools
- Browsers
- MCP servers
- Enterprise applications
- File systems

Every integration introduces another possible attack surface.

For example:

```text
AI Agent
   ↓
API
   ↓
Database
```

If the API or database permissions are poorly configured, the AI agent could potentially perform actions that it should not be allowed to perform.

Therefore:

> **AI security must include the entire tool/integration ecosystem, not just the LLM.**

---

# 18. AI Agents and Excessive Permissions

AI agents are particularly risky because they can potentially **take actions** rather than simply generate text.

For example, an agent could have access to:

- Databases
- APIs
- Cloud resources
- File systems
- Email
- Browsers
- Enterprise systems

If an agent is given excessive permissions, a malicious prompt or unexpected model behavior could result in unintended actions.

### Example from the lecture

A real-world scenario was discussed where an AI agent, while trying to perform its task optimally, ended up identifying **deleting an entire production database** as the optimal route.

The important lesson is:

> An AI agent may technically execute an action that appears logically useful to the model but is completely unacceptable from a business/security perspective.

Therefore AI agents require strong:

- Permissions
- Guardrails
- Tool controls
- Human approval where appropriate
- Monitoring
- Policies

---

# 19. Lack of Visibility

Another major problem is lack of **observability**.

If you cannot see what your AI system is doing, it becomes difficult to:

- Debug failures
- Detect attacks
- Identify hallucinations
- Monitor model behavior
- Track tool usage
- Investigate incidents
- Measure performance
- Control costs

Therefore production AI systems need strong observability.

---

# 20. Compliance and Legal Risks

Enterprise AI systems must comply with applicable laws and regulations.

The lecture mentions examples such as:

- **GDPR**
- **CCPA**
- European Union regulations
- Country-specific data privacy regulations
- Industry-specific regulations

Different countries and markets may have different requirements.

Therefore:

> A production AI system must consider the legal and regulatory environment in which it operates.

This can include requirements around:

- Data privacy
- Data storage
- Data processing
- Consent
- Data retention
- Security
- User rights
- Sensitive information

---

# 21. AI Governance

**AI Governance** refers to the policies, processes, controls, and oversight used to ensure that AI systems are developed and operated responsibly.

Enterprise AI governance should ensure that:

- Sensitive information is protected
- Data is handled appropriately
- AI systems follow organizational policies
- Regulatory requirements are satisfied
- Models are monitored
- AI decisions/actions can be investigated
- Appropriate controls exist around model and tool usage

A production AI application therefore needs more than just technical functionality.

---

# 22. Real-World Examples Mentioned

The lecture highlights several real-world incidents and scenarios.

### 1. Samsung — sensitive code exposure

Employees reportedly leaked sensitive/proprietary code through ChatGPT.

**Lesson:**

Employees using external LLMs can unintentionally expose confidential enterprise information.

---

### 2. Prompt injection bypassing safeguards

Attackers can construct prompts intended to bypass model restrictions.

**Lesson:**

LLM security cannot rely solely on the model's built-in safety behavior.

---

### 3. Malicious prompts causing hidden data exposure

A malicious prompt can potentially manipulate an AI application into revealing information that should remain hidden.

**Lesson:**

User input must be treated as untrusted.

---

### 4. AI agents performing unintended actions

AI agents can be manipulated or can make undesirable decisions when they have access to tools.

**Lesson:**

Agents require strong tool permissions and action controls.

---

### 5. Public vector stores / poor access control

Poorly secured vector databases can expose information that should be private.

**Lesson:**

RAG security is not only about the LLM; **retrieval infrastructure and access control are equally important.**

---

### 6. Hallucinations causing financial/legal misinformation

An LLM can confidently generate incorrect financial or legal information.

**Lesson:**

High-impact applications require continuous evaluation and appropriate safeguards.

---

# 23. Impact of Poor AI Security

Poor security can result in significant consequences.

### Financial losses

Security incidents can directly cause monetary damage.

### Data breaches

Sensitive customer or company information can be exposed.

### Reputation damage

Customers may lose trust in the organization.

### Loss of customer trust/support

Users may stop trusting the company's AI products.

### Legal consequences

Organizations can face penalties, lawsuits, or regulatory action.

### Business disruption

An AI-related incident can disrupt critical business operations.

---

# 24. Security Must Be "By Design"

The course emphasizes an important principle:

> **Security should not be added after the AI application is built.**

Instead:

> **Security should be designed into the AI system from the beginning.**

This is called:

### Security by Design

Instead of:

```text
Build AI
   ↓
Deploy
   ↓
Security problems
   ↓
Add security
```

the desired approach is:

```text
Design AI
   ↓
Security + Governance + Guardrails
   ↓
Build
   ↓
Evaluate
   ↓
Monitor
   ↓
Deploy
```

---

# 25. What the Bootcamp Proposes

The bootcamp proposes several mechanisms for building secure, production-ready AI applications.

---

## 25.1 Validate Inputs

Before sending user data to an LLM, validate the input.

Possible checks include:

- Sensitive information
- Malicious prompts
- Prompt injection
- Jailbreak attempts
- Invalid requests
- Policy violations

---

## 25.2 Validate Outputs

Generated responses should also be checked.

Possible checks include:

- Harmful content
- Sensitive information
- Hallucinations
- Policy violations
- Incorrect formats
- Unsafe recommendations

Therefore:

```text
              ┌──────────────┐
User Input →  │ Input Checks │
              └──────┬───────┘
                     ↓
                    LLM
                     ↓
              ┌──────────────┐
              │Output Checks │
              └──────┬───────┘
                     ↓
                  User
```

---

# 26. Guardrails

Guardrails are one of the major topics of the course.

They establish boundaries around AI behavior.

They can be applied to:

### Input

```text
User → Input Guardrail → LLM
```

### Output

```text
LLM → Output Guardrail → User
```

They can help with:

- Safety
- Privacy
- Security
- Policy enforcement
- Content filtering
- Sensitive-data detection

---

# 27. NVIDIA NeMo Guardrails

One framework specifically mentioned is:

> **NVIDIA NeMo Guardrails**

The bootcamp will explore how guardrails can be implemented using frameworks such as NeMo Guardrails.

The objective isn't just to understand the theory but to understand:

> **How guardrails are implemented in actual agentic AI applications.**

---

# 28. LLM Gateways

Another major topic is:

> **LLM Gateway**

An LLM gateway acts as an intermediary/control layer between the AI application and LLM providers.

Conceptually:

```text
AI Application
      ↓
  LLM Gateway
      ↓
 ┌────┼────┐
 ↓    ↓    ↓
OpenAI Claude Gemini
```

Instead of every application directly communicating with different LLM providers, a gateway can centralize controls.

Potential benefits include:

- Centralized security
- Model routing
- Access control
- Monitoring
- Policy enforcement
- Rate limiting
- Cost control
- Model switching
- Standardized API access

The bootcamp will cover **multiple LLM gateway frameworks**, including open-source and enterprise solutions.

---

# 29. Evaluation

AI systems cannot simply be deployed and forgotten.

They need to be **continuously evaluated**.

Evaluation can help determine:

- Is the model producing good answers?
- Is the response relevant?
- Is it hallucinating?
- Is the retrieved context useful?
- Is the agent behaving correctly?
- Are safety policies being followed?

The course therefore treats evaluation as an ongoing part of the production lifecycle.

---

# 30. Observability

Observability provides visibility into the AI system.

It is important because AI systems involve many moving parts:

```text
User
 ↓
Application
 ↓
Guardrails
 ↓
LLM Gateway
 ↓
LLM
 ↓
Retriever
 ↓
Vector DB
 ↓
Tools/APIs
 ↓
Output
```

Without observability, understanding failures across this chain becomes difficult.

Therefore the course will cover observability as a core production-AI concept.

---

# 31. Secure Data, Tools and Integrations

Security needs to be applied across the entire architecture.

Not just:

```text
LLM ← Security
```

but:

```text
User
 ↓
Application
 ↓
Data
 ↓
Vector DB
 ↓
LLM
 ↓
Tools
 ↓
APIs
 ↓
Enterprise Systems
```

Every component needs appropriate security controls.

---

# 32. Compliance and Governance

Production AI systems need to remain:

- Compliant
- Governed
- Auditable
- Secure

The system needs to follow applicable:

- Privacy regulations
- Industry regulations
- Organizational policies
- AI governance requirements

---

# 33. Core Production AI Components

The major modules of the bootcamp can therefore be summarized as:

| Component | Main Purpose |
|---|---|
| **Security** | Protect AI system, users and data |
| **Observability** | See and understand system behavior |
| **Guardrails** | Restrict unsafe inputs/outputs/actions |
| **LLM Gateway** | Centralize LLM access and controls |
| **Evaluation** | Measure AI quality and safety |
| **Governance** | Ensure responsible and compliant AI |
| **Data Security** | Protect sensitive/private information |
| **Tool Security** | Control what agents can do |
| **Compliance** | Follow legal/regulatory requirements |

---

# 34. Framework-Based Learning

The bootcamp will not focus on only one framework.

For each major concept, multiple frameworks/tools will be explored.

For example:

### Guardrails

The course may cover:

- NVIDIA NeMo Guardrails
- Other guardrail frameworks

### LLM Gateways

The course will cover:

- Multiple open-source frameworks
- Enterprise LLM gateway solutions

The purpose is to understand **different implementation approaches**, rather than becoming dependent on one particular tool.

---

# 35. Why Multiple Frameworks?

Knowing multiple implementations helps you understand:

- Different architectures
- Different trade-offs
- Open-source vs enterprise approaches
- How to choose a tool for a project
- How the same production requirement can be solved in different ways

The ultimate goal is not:

> "I know framework X."

The goal is:

> **"I understand the production problem and know how to solve it using appropriate tools."**

---

# 36. Overall Production-Ready AI Architecture

Putting the lecture concepts together, the desired architecture looks roughly like:

```text
                         USER
                           │
                           ▼
                  ┌─────────────────┐
                  │ Input Guardrails│
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ AI Application  │
                  │ / Agent / RAG   │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │   LLM Gateway   │
                  └────────┬────────┘
                           │
                           ▼
                       ┌───────┐
                       │  LLM  │
                       └───┬───┘
                           │
            ┌──────────────┼──────────────┐
            ▼              ▼              ▼
       Vector DB         APIs          MCP Tools
            │              │              │
            └──────────────┼──────────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │Output Guardrails│
                  └────────┬────────┘
                           │
                           ▼
                         USER

        ─────────────────────────────────────
        Observability + Evaluation + Security
        Governance + Compliance across system
```

This is the key conceptual transition from:

**"I built an LLM application"**

to:

**"I built a production-ready AI system."**

---

# 37. Key Terminology to Remember

### GenAI
Generative Artificial Intelligence — systems capable of generating text, code, images, etc.

### RAG
**Retrieval-Augmented Generation** — retrieves relevant external information and provides it to an LLM to improve grounded responses.

### Agent
An AI system capable of reasoning/planning and potentially taking actions through tools.

### Agentic AI
AI systems that use workflows, reasoning, tools, memory, planning, or multiple steps to accomplish goals.

### Prompt Injection
An attack where malicious instructions are inserted into input/context to manipulate the model.

### Jailbreaking
Attempts to bypass an LLM's safety restrictions.

### Guardrails
Controls that constrain inputs, outputs, or actions of an AI system.

### LLM Gateway
A centralized layer for controlling and managing interactions between applications and LLM providers.

### Observability
The ability to understand and monitor what is happening inside the AI system.

### Hallucination
When an AI model generates information that is false, unsupported, or fabricated but may appear convincing.

### AI Governance
Policies and processes that ensure AI is developed and operated safely, responsibly, and according to organizational/legal requirements.

### Compliance
Following applicable laws, regulations, standards, and policies.

---

# 38. Most Important Takeaways

### 1.
**Building an AI application is not the same as building a production-ready AI system.**

### 2.
Production AI requires much more than an LLM and an application framework.

### 3.
The major concerns are:

**Security + Observability + Guardrails + LLM Gateways + Evaluation + Governance + Compliance**

### 4.
User input should be treated as **untrusted**.

### 5.
Sensitive information such as financial, personal, proprietary, and confidential data must be protected.

### 6.
LLM outputs are not automatically safe or correct.

### 7.
**Prompt injection and jailbreaking** are important GenAI-specific security threats.

### 8.
RAG systems also need security because **vector databases can contain sensitive information**.

### 9.
AI agents introduce additional risk because they can **take actions through tools**.

### 10.
Giving an AI agent excessive permissions can lead to severe unintended consequences.

### 11.
Security must cover the **entire AI architecture**, not just the LLM.

### 12.
AI systems need continuous **evaluation and monitoring**.

### 13.
Enterprise AI must account for **privacy laws, regulations, governance, and compliance**.

### 14.
Security should be implemented from the beginning:

> **Security by Design**

### 15.
The ultimate objective of the bootcamp is to learn how to transform:

> **RAG / Agentic AI / AI Agent → Enterprise-Grade Production AI System**

---

## One-Line Mental Model

If you want to remember the entire lecture in one framework:

> **A production-ready AI system is not just an LLM application; it is an AI application surrounded by security, guardrails, observability, evaluation, controlled tool/data access, governance, and compliance.**

This lecture is essentially the **foundation for the rest of the bootcamp**: first understand *why* these layers are necessary, then learn how to implement each one using different frameworks and technologies.