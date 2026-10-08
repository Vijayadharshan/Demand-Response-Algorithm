class incentive:
    def __init__(self, rate):
        self.rate = rate
    def calculate_incentive(self, curtailed_energy):
        incentive = curtailed_energy * self.rate
        return incentive