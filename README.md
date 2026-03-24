================================================================
   SMART PARKING INTELLIGENT AGENT SYSTEM
   DCIT 403 — Intelligent Agent Systems
   Individual Semester Project
================================================================

WHAT THIS PROJECT IS
---------------------
A simulation of a Smart Parking system built using the Prometheus
agent methodology. Three intelligent agents work together to manage
a parking lot automatically — no human intervention needed.

THE 3 AGENTS
-------------
1. Entry/Exit Agent  (entry_agent.py)
   - Controls the barrier gate
   - Detects arriving and departing vehicles
   - Communicates with the other two agents

2. Monitoring Agent  (monitoring_agent.py)
   - Tracks all 10 parking slot statuses in real time
   - Responds to availability requests
   - Updates slots when cars arrive or leave

3. Management Agent  (management_agent.py)
   - Records all entry and exit events
   - Calculates parking fees (GH₵5 per hour)
   - Generates the end-of-day report

FILES IN THIS PROJECT
----------------------
monitoring_agent.py  — Agent 2: tracks all slot statuses
management_agent.py  — Agent 3: records and payments
entry_agent.py       — Agent 1: gate control and agent loop
simulation.py        — Runs all 7 scenarios end to end
README.md            — This file

REQUIREMENTS
-------------
- Python 3.6 or higher
- No external libraries needed
- Works on Windows, Mac, and Linux

HOW TO RUN
-----------
Step 1 — Open Command Prompt (Windows key + R, type cmd, Enter)

Step 2 — Navigate to this folder:
          cd Desktop\smart_parking

Step 3 — Run the simulation:
          python simulation.py

Step 4 — Watch the output. You will see all 3 agents
          communicating in real time across 7 scenarios.

SCENARIOS DEMONSTRATED
-----------------------
Scenario 1 — Successful vehicle entry, slot assigned
Scenario 2 — Second car arrives, different slot assigned
Scenario 3 — First car exits, fee calculated and paid
Scenario 4 — Lot fills up completely, all 10 slots taken
Scenario 5 — New car denied entry, lot is full
Scenario 6 — Car leaves, slot freed, waiting car enters
Scenario 7 — End of day report generated

HOW THIS MAPS TO PROMETHEUS DESIGN
------------------------------------
Phase 1 - Goals      : Each agent has a clear, defined goal
Phase 2 - Architecture: 3 separate agent classes, own data
Phase 3 - Interaction : Agents call each other's methods
Phase 4 - Detailed    : Each class has capabilities and plans
Agent Loop            : PERCEIVE → DECIDE → ACT in every scenario

CHALLENGES AND LIMITATIONS
----------------------------
- Sensors are simulated, not real hardware
- Time is based on system clock, fees minimum 1 hour
- Payment is displayed only, not processed through a gateway
- No graphical interface, runs in terminal only
- Manages one parking lot only

================================================================
   DCIT 403 | Smart Parking | 2025/2026
================================================================