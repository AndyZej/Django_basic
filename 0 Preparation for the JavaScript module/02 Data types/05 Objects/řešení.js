
// Car object
const car = {
  type: "sedan",
  color: "green",
  engine: 2.0
};

// Display car information
console.log(car.type + " " + car.color + " " + car.engine);

// Color object
const color = {
  red: 100,
  green: 0,
  blue: 50
};

// Reference to the color object
const referenceColor = color;

// Modify the object through the reference
referenceColor.red = 50;
referenceColor.green = 50;

// Display the updated object (optional)
console.log(color);