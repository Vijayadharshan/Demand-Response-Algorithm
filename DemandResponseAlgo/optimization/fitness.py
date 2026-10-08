class fitnessfunc:
    def __init__(self, reduction_req):
        self.reduction_req = reduction_req

    def calculate(self, actual_reduction, no_of_switches, comfort_penalty):
        difference = abs(self.reduction_req - actual_reduction)
        comfort_weight = 10
        switching_penalty = no_of_switches*1
        fitness = difference + switching_penalty
        return fitness