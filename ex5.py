name = 'Andres Ramirez'
age = 32 # not a lie
height = 72 # inches
my_height = round(72 * 2.54)
weight = 180 # lbs
my_weight = round(180 * 0.453592)
eyes = 'brown'
teeth = 'White'
hair = 'Black'

print(f"Let's talk about {name}.")
print(f"He's {my_height} centimeters tall.")
print(f"He's {my_weight} Kilograms heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the food.")

# This line is tricky, try to get it exactly right
total = age + height + weight
print(f"If if add {age}, {height}, and {weight} i get {total}.")
