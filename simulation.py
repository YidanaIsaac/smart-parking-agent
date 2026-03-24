# ============================================================
# SIMULATION — Runs all scenarios
# ============================================================

import time
from monitoring_agent import MonitoringAgent
from management_agent import ManagementAgent
from entry_agent import EntryAgent

def run_simulation():
    print("\n" + "="*50)
    print("   SMART PARKING INTELLIGENT AGENT SYSTEM")
    print("   DCIT 403 — Simulation")
    print("="*50 + "\n")

    print(">>> Initialising agents...\n")
    monitoring = MonitoringAgent()
    management = ManagementAgent()
    management.connect(monitoring)
    entry = EntryAgent(monitoring, management)

    time.sleep(1)
    print("\n>>> All agents online. Starting simulation...\n")
    time.sleep(1)

    print("\n--- SCENARIO 1: Successful Entry ---")
    entry.vehicle_arrives("GH-1234-22")
    monitoring.show_status()
    time.sleep(1)

    print("\n--- SCENARIO 2: Second Car Arrives ---")
    entry.vehicle_arrives("GH-5678-22")
    monitoring.show_status()
    time.sleep(1)

    print("\n--- SCENARIO 3: First Car Exits and Pays ---")
    entry.vehicle_exits("GH-1234-22")
    monitoring.show_status()
    time.sleep(1)

    print("\n--- SCENARIO 4: Filling Up the Lot ---")
    extra_cars = [
        "GH-0001", "GH-0002", "GH-0003", "GH-0004",
        "GH-0005", "GH-0006", "GH-0007", "GH-0008",
        "GH-0009"
    ]
    for car in extra_cars:
        entry.vehicle_arrives(car)
        time.sleep(0.2)
    monitoring.show_status()
    time.sleep(1)

    print("\n--- SCENARIO 5: Lot is Full — New Car Denied ---")
    entry.vehicle_arrives("GH-LATE-99")
    time.sleep(1)

    print("\n--- SCENARIO 6: A Car Leaves, Slot Freed ---")
    entry.vehicle_exits("GH-5678-22")
    monitoring.show_status()

    print("\n>>> Waiting car tries again...")
    time.sleep(0.5)
    entry.vehicle_arrives("GH-LATE-99")
    monitoring.show_status()
    time.sleep(1)

    print("\n--- SCENARIO 7: End of Day Report ---")
    management.generate_report()

    print("\n" + "="*50)
    print("   SIMULATION COMPLETE")
    print("="*50 + "\n")

if __name__ == "__main__":
    run_simulation()