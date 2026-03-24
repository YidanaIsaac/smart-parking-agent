# ============================================================
# MANAGEMENT AGENT — Records, payments, and reports
# ============================================================

from datetime import datetime
import math

class ManagementAgent:

    def __init__(self):
        self.records = {}
        self.fee_rate = 5
        self.daily_revenue = 0
        self.monitoring_agent = None
        print("[ManagementAgent] Started. Fee rate: GH₵5/hour.")

    def connect(self, monitoring_agent):
        self.monitoring_agent = monitoring_agent

    def log_entry(self, vehicle_id, slot_id, entry_time):
        self.records[vehicle_id] = {
            "slot_id": slot_id,
            "entry_time": entry_time,
            "exit_time": None,
            "duration": None,
            "fee": None,
            "status": "ACTIVE"
        }
        print(f"[ManagementAgent] Entry logged — Vehicle: {vehicle_id}, "
              f"Slot: {slot_id}, Time: {entry_time.strftime('%I:%M %p')}")

    def log_exit(self, vehicle_id, exit_time):
        if vehicle_id not in self.records:
            print(f"[ManagementAgent] ERROR: No entry record for {vehicle_id}")
            return

        record = self.records[vehicle_id]
        entry_time = record["entry_time"]
        duration_seconds = (exit_time - entry_time).total_seconds()
        duration_hours = duration_seconds / 3600
        billed_hours = max(1, math.ceil(duration_hours))
        fee = billed_hours * self.fee_rate

        record["exit_time"] = exit_time
        record["duration"] = billed_hours
        record["fee"] = fee
        record["status"] = "COMPLETE"
        self.daily_revenue += fee

        print(f"[ManagementAgent] Exit processed — Vehicle: {vehicle_id}")
        print(f"[ManagementAgent] Duration: {billed_hours} hour(s) | Fee: GH₵{fee}")

        slot_id = record["slot_id"]
        if self.monitoring_agent:
            self.monitoring_agent.mark_free(slot_id)

        return fee

    def generate_report(self):
        print("\n" + "="*50)
        print("       END OF DAY REPORT — Smart Parking")
        print("="*50)

        completed = [r for r in self.records.values() if r["status"] == "COMPLETE"]
        active = [r for r in self.records.values() if r["status"] == "ACTIVE"]

        print(f"  Total vehicles served : {len(completed)}")
        print(f"  Currently parked      : {len(active)}")
        print(f"  Total revenue         : GH₵{self.daily_revenue}")
        print(f"  Fee rate              : GH₵{self.fee_rate}/hour")

        if completed:
            print("\n  Transaction Details:")
            for vehicle_id, record in self.records.items():
                if record["status"] == "COMPLETE":
                    print(f"    Vehicle {vehicle_id} | Slot {record['slot_id']} | "
                          f"{record['duration']}hr(s) | GH₵{record['fee']}")

        print("="*50 + "\n")