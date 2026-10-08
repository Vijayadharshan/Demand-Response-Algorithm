
class appliance:
    def __init__(self, name, rated_power, priority, comfort, flexibility, state):
        self.name = name
        self.rated_power = rated_power
        self.current_power = rated_power
        self.priority = priority
        self.comfort = comfort
        self.flexibility = flexibility
        self.state = state

    def turn_on(self):
        self.state = True

    def turn_off(self):
        self.state = False

    def get_power(self):
        if self.state:
            return self.current_power

        return 0