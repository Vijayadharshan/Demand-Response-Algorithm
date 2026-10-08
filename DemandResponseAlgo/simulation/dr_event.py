class dr_event:
    def __init__(self, reduction_req, duration):
        self.reduction_req = reduction_req
        self.duration = duration

    def display_event(self):
        print("Demand Response Event Details:")
        print(f"Reduction Requirement: {self.reduction_req} kW")
        print(f"Duration: {self.duration} hours")
