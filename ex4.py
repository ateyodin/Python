# Variable Cars
cars = 100
# how many people can go inside a car
space_in_a_car = 4.0
# variable drivers
drivers = 30
# variable passengers
passengers = 90
# quantity of not driven Cars
cars_not_driven = cars - drivers
# cars driven by drivers
cars_driven = drivers
# how many people is going inside the cars
carpool_capacity = cars_driven * space_in_a_car
# avera of passengers
average_passengers_per_car = passengers / cars_driven
# print cars available - 100
print("There are", cars, "cars available.")
# print driver available - 30
print("There are only", drivers, "drivers available.")
# print cars not driven 100 - 30 = 70
print("There will be", cars_not_driven, "empty cars today.")
# print carpool capacity 30 * 4.0 = 120.0
print("We can transport", carpool_capacity, "people today.")
# print amount of passenger for that day - 90
print("We have", passengers, "to carpool today.")
# print amount on people to put inside a car 90 / 30 = 3.0
print("We need to put about", average_passengers_per_car, "in each car.")
