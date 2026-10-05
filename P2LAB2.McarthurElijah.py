#Elijah Mcarthur
#10/4/26
#P2LAB2
#how to write code that uses a dictionary to store user input and displays output to the user

# Pseudocode:
# 1. Create a dictionary containing vehicle names and their MPG.
# 2. Get and display all the keys from the dictionary.
# 3. Ask the user to enter a vehicle.
# 4. Display the MPG for the selected vehicle.
# 5. Ask the user how many miles they will drive.
# 6. Calculate gallons needed by dividing miles by MPG.
# 7. Display the gallons needed rounded to two decimal places.

# Create dictionary of vehicles and MPG
cars = {
    "Toyota Camry": 28,
    "Honda Accord": 30,
    "Ford F-150": 20,
    "Chevrolet Silverado": 18,
    "Tesla Model 3": 130
}

#Get and display the dictionary keys
keys = cars.keys()
print("Available vehicles:")
for key in keys:
    print(key)

  # Get vehicle from user 
vehicle = input("Enter a vehicle from the list above: ")
if vehicle in cars:
    mpg = cars[vehicle]
    print(f"The {vehicle} gets {mpg} MPG.")

# Display MPG
mpg = cars[vehicle]
print(f"The {vehicle} gets {mpg} MPG.")

# Get miles from user
miles = float(input("Enter the number of miles you will drive: "))

#Calculate gallons of gas needed
gallons = miles / mpg

# Display gallons needed
print(f"Gallons of gas needed: {gallons:.2f}")