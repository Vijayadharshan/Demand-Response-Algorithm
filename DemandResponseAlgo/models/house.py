from models.appliances import appliance
import math

class house:
    def __init__(self):
        self.appliances = []

    def add_appliance(self, appliance):
        self.appliances.append(appliance)

    def get_total_power(self):
        total = 0
        for i in self.appliances:
            total += i.get_power()
        return total

    def display_status(self):
        print("House Status:")
        for i in self.appliances:
            status = "ON" if i.state else "OFF"
            print(f"{i.name:20} {status:5} {i.get_power()} W")
        print(f"Total Power : {self.get_total_power()} W")

    def check_dr_feasibility(self, reduction_req):
        total_reducible_power = 0
        for i in self.appliances:
            if i.is_on:
                total_reducible_power += i.power_rating

        if total_reducible_power >= reduction_req:
            return True
        else:
            return False

