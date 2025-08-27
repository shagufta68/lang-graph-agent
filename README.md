\# Lang Graph Agent – Customer Support Workflow



\## Author

Shagufta Israr



\## Description

This project implements a Lang Graph Agent for customer support workflows using Python and YAML.



\## Features

\- 11 stages: INTAKE → COMPLETE

\- Deterministic and Non-deterministic stages

\- MCP Client orchestration (Atlas / Common)

\- State persistence across stages

\- Logging of each stage and ability

\- Final structured payload output



\## How to Run

1\. Activate virtual environment:

&nbsp;  venv\\Scripts\\activate

2\. Install dependencies:

&nbsp;  pip install -r requirements.txt

3\. Run agent:

&nbsp;  python agent.py

4\. Check output in `output\_payload.json`



\## Sample Input

`demo\_input.json`:

```json

{

&nbsp; "customer\_name": "Alice",

&nbsp; "email": "alice@example.com",

&nbsp; "query": "My order is delayed",

&nbsp; "priority": "high",

&nbsp; "ticket\_id": "T12345"

}



\# Lang Graph Agent – Workflow Diagram



'''                    ┌────────────┐

&nbsp;                   │   INTAKE   │

&nbsp;                   │ accept\_payload │

&nbsp;                   │ MCP: COMMON │

&nbsp;                   └──────┬─────┘

&nbsp;                          │

&nbsp;                          ▼

&nbsp;                   ┌────────────┐

&nbsp;                   │ UNDERSTAND │

&nbsp;                   │ parse\_request\_text (COMMON) │

&nbsp;                   │ extract\_entities (ATLAS)  │

&nbsp;                   └──────┬─────┘

&nbsp;                          │

&nbsp;                          ▼

&nbsp;                   ┌────────────┐

&nbsp;                   │  PREPARE   │

&nbsp;                   │ normalize\_fields (COMMON) │

&nbsp;                   │ enrich\_records (ATLAS)   │

&nbsp;                   │ add\_flags\_calculations(COMMON) │

&nbsp;                   └──────┬─────┘

&nbsp;                          │

&nbsp;                          ▼

&nbsp;                   ┌────────────┐

&nbsp;                   │    ASK     │

&nbsp;                   │ clarify\_question (ATLAS) │

&nbsp;                   └──────┬─────┘

&nbsp;                          │

&nbsp;                          ▼

&nbsp;                   ┌────────────┐

&nbsp;                   │   WAIT     │

&nbsp;                   │ extract\_answer (ATLAS)   │

&nbsp;                   │ store\_answer (COMMON)    │

&nbsp;                   └──────┬─────┘

&nbsp;                          │

&nbsp;                          ▼

&nbsp;                   ┌────────────┐

&nbsp;                   │  RETRIEVE  │

&nbsp;                   │ knowledge\_base\_search (ATLAS) │

&nbsp;                   │ store\_data (COMMON)           │

&nbsp;                   └──────┬─────┘

&nbsp;                          │

&nbsp;                          ▼

&nbsp;                   ┌────────────┐

&nbsp;                   │   DECIDE   │  ← Non-deterministic

&nbsp;                   │ solution\_evaluation (COMMON) │

&nbsp;                   │ escalation\_decision (ATLAS) │

&nbsp;                   │ update\_payload (COMMON)     │

&nbsp;                   └──────┬─────┘

&nbsp;                          │

&nbsp;                          ▼

&nbsp;                   ┌────────────┐

&nbsp;                   │   UPDATE   │

&nbsp;                   │ update\_ticket (ATLAS) │

&nbsp;                   │ close\_ticket  (ATLAS) │

&nbsp;                   └──────┬─────┘

&nbsp;                          │

&nbsp;                          ▼

&nbsp;                   ┌────────────┐

&nbsp;                   │   CREATE   │

&nbsp;                   │ response\_generation (COMMON) │

&nbsp;                   └──────┬─────┘

&nbsp;                          │

&nbsp;                          ▼

&nbsp;                   ┌────────────┐

&nbsp;                   │     DO     │

&nbsp;                   │ execute\_api\_calls (ATLAS) │

&nbsp;                   │ trigger\_notifications (ATLAS) │

&nbsp;                   └──────┬─────┘

&nbsp;                          │

&nbsp;                          ▼

&nbsp;                   ┌────────────┐

&nbsp;                   │  COMPLETE  │

&nbsp;                   │ output\_payload (COMMON) │

&nbsp;                   └────────────┘

'''



