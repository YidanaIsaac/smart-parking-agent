# ============================================================
# ENTRY/EXIT AGENT — Controls the gate
# ============================================================

from datetime import datetime

class EntryAgent:

    def __init__(self, monitoring_agent, management_agent):
        self.gate_status = "CLOSED"
        self.monitoring_agent = monitoring_agent
        self.management_agent = management_agent
        print("[EntryAgent] Started. Gate is CLOSED.")

    def vehicle_arrives(self, vehicle_id):
        print(f"\n{'='*50}")
        print(f"[EntryAgent] PERCEPT: Vehicle {vehicle_id} detected at entrance.")

        print(f"[EntryAgent] Sending check_availability to MonitoringAgent...")
        slot_id = self.monitoring_agent.check_availability()

        if slot_id == "FULL":
            self._deny_entry(vehicle_id)
        else:
            self._grant_entry(vehicle_id, slot_id)

    def _grant_entry(self, vehicle_id, slot_id):
        entry_time = datetime.now()
        self.gate_status = "OPEN"
        print(f"[EntryAgent] ACT: Opening gate for {vehicle_id}.")
        print(f"[EntryAgent] ACT: Displaying — Welcome! Please go to Slot {slot_id}")
        self.monitoring_agent.mark_occupied(slot_id)
        print(f"[EntryAgent] Sending log_entry to ManagementAgent...")
        self.management_agent.log_entry(vehicle_id, slot_id, entry_time)
        self.gate_status = "CLOSED"
        print(f"[EntryAgent] ACT: Gate closed.")

    def _deny_entry(self, vehicle_id):
        print(f"[EntryAgent] ACT: Gate stays CLOSED.")
        print(f"[EntryAgent] ACT: Displaying — Sorry {vehicle_id}, Parking is FULL!")

    def vehicle_exits(self, vehicle_id):
        print(f"\n{'='*50}")
        print(f"[EntryAgent] PERCEPT: Vehicle {vehicle_id} detected at exit.")

        exit_time = datetime.now()
        print(f"[EntryAgent] Sending log_exit to ManagementAgent...")
        fee = self.management_agent.log_exit(vehicle_id, exit_time)

        self.gate_status = "OPEN"
        print(f"[EntryAgent] ACT: Opening exit gate.")
        if fee:
            print(f"[EntryAgent] ACT: Displaying — Goodbye! Your fee was GH₵{fee}. Drive safely!")

        self.gate_status = "CLOSED"
        print(f"[EntryAgent] ACT: Exit gate closed.")