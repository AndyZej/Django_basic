# Car object
car = {
    "type": "sedan",
    "color": "green",
    "engine": 2.0
}

# Display car information
print(car["type"] + " " + car["color"] + " " + str(car["engine"]))

# Color object
color = {
    "red": 100,
    "green": 0,
    "blue": 50
}

# Reference to the same object
referenceColor = color

# Modify the color object
referenceColor["red"] = 50
referenceColor["green"] = 50

# Display the modified object
print(color)