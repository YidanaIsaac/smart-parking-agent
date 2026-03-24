# ============================================================
# MONITORING AGENT — Tracks all parking slots in real time
# ============================================================

class MonitoringAgent:

    def __init__(self):
        self.slots = {
            "A1": "FREE", "A2": "FREE", "A3": "FREE",
            "B1": "FREE", "B2": "FREE", "B3": "FREE",
            "C1": "FREE", "C2": "FREE", "C3": "FREE",
            "C4": "FREE"
        }
        self.total_slots = 10
        print("[MonitoringAgent] Started. All 10 slots are FREE.")

    def check_availability(self):
        for slot_id, status in self.slots.items():
            if status == "FREE":
                self.slots[slot_id] = "RESERVED"
                print(f"[MonitoringAgent] Slot {slot_id} is available. Reserving it.")
                return slot_id
        print("[MonitoringAgent] All slots are FULL.")
        return "FULL"

    def mark_occupied(self, slot_id):
        self.slots[slot_id] = "OCCUPIED"
        print(f"[MonitoringAgent] Slot {slot_id} is now OCCUPIED.")

    def mark_free(self, slot_id):
        self.slots[slot_id] = "FREE"
        print(f"[MonitoringAgent] Slot {slot_id} is now FREE again.")

    def show_status(self):
        print("\n--- PARKING LOT STATUS ---")
        free = 0
        for slot_id, status in self.slots.items():
            icon = "FREE  " if status == "FREE" else "TAKEN"
            print(f"  [{icon}] Slot {slot_id}")
            if status == "FREE":
                free += 1
        print(f"  Available: {free}/{self.total_slots} slots")
        print("--------------------------\n")