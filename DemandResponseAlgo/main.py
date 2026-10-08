from models.appliances import appliance
from models.house import house
from simulation.dr_event import dr_event
from optimization.gwo import gwo


house = house()

geyser  = appliance("Geyser", 900, 7, 10, True, True)
kettle = appliance("Kettle", 500, 4, 1, True, True)
lamp = appliance("Lamp", 400, 6, 1, False, True)

house.add_appliance(geyser)
house.add_appliance(kettle)
house.add_appliance(lamp)

gwo = gwo(
    population_size=9,
    iterations=20
)
dr_event = dr_event(
    reduction_req=900,
    duration=2
)
print("\n===== DR TEST =====")

print("DR target:", dr_event.reduction_req, "W")

solution = gwo.optimize(
    house.appliances,
    dr_event.reduction_req
)

reduction = gwo.calculate_power_reduction(
    house.appliances,
    solution
)

fitness = gwo.calculate_fitness(
    house.appliances,
    solution,
    dr_event.reduction_req
)

print("Best solution:", solution)
print("Actual reduction:", reduction, "W")
print("Fitness:", fitness)