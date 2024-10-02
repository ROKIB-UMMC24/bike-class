from bike import bike

# Question 1: Instantiate a new bike object.
my_bike = bike(gear=15, current_gear=1, wheels=4, brake="hand brakes")  # Initialize a new bike object with default values
print(my_bike)


# Question 2: Using your well-named class method, set the gear to 10 and show that the gear has been set to 10.
try:
    my_bike.setGear(10)  # Set the gear to 10
    print(f"Gear set to: {my_bike.getGear()}")  # Show the gear has been set to 10

    # Question : Using your well-named class method, increase the gear and show that the gear has increased.
    my_bike.increaseGear()  # Increase the gear
    print(f"Current gear after increasing: {my_bike.getCurrentGear()}")  # Show the current gear


# Question 3. Attempt to set the gear above the limit
    max_gear = int(input("Please enter a gear value beyond (1 to15): "))
    my_bike.setGear(max_gear)  # Attempt to set the max gear
except ValueError as e:
    print(e)


# Question 4: Attempt to set the gear below the limit
try:
    min_gear = int(input("Please enter a gear value (must be 1 or less): "))
    my_bike.setGear(min_gear)  # Input a number gear below 1
except ValueError as e:
    print(e)  # Print the error message if the gear is invalid

# Question 5: Attempt to set the brake type to "electric"
try:
    my_bike.setBrake("electric")  # Attempt to set an invalid brake type
except ValueError as e:
    print(e)  # Print the error message if the brake type is invalid
