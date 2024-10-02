class bike:
    # Private properties
    __gear: int = 15  # Total number of gears (1-15)
    __current_gear: int = 1  # Default current gear is 1
    __wheels: int = 4  # Default number of wheels is 1
    __brake: str = ""  # Brake type

    # Constructor to initialize the bike
    def __init__(self, gear=15, current_gear=1, wheels=4, brake="hand brakes"):
        self.setGear(gear)  # Set total number of gears
        self.setCurrentGear(current_gear)  # Set the current gear
        self.setWheels(wheels)  # Set number of wheels
        self.setBrake(brake)  # Set brake type

    # Getter and setter for Gear (1-15)
    def getGear(self) -> int:
        return self.__gear

    def setGear(self, gear: int) -> None:
        """Set the total number of gears (1-15)."""
        if 1 <= gear <= 15:
            self.__gear = gear
            print(f"Number of gears set to: {self.__gear}")
        else:
            raise ValueError("Number of gears must be between 1 and 15.")

    # Getter and setter for the Current Gear
    def getCurrentGear(self) -> int:
        return self.__current_gear

    def setCurrentGear(self, current_gear: int) -> None:
        """Set the current gear (between 1 and the total gear)."""
        if 1 <= current_gear <= self.__gear:
            self.__current_gear = current_gear
            print(f"Current gear set to: {self.__current_gear}")
        else:
            raise ValueError(f"Current gear must be between 1 and {self.__gear}.")

    # Getter and setter for the number of wheels (1, 2, 3, or 4)
    def getWheels(self) -> int:
        return self.__wheels

    def setWheels(self, wheels: int) -> None:
        """Set the number of wheels (1, 2, 3, or 4)."""
        if wheels in [1, 2, 3, 4]:
            self.__wheels = wheels
            print(f"Number of wheels set to: {self.__wheels}")
        else:
            raise ValueError("Number of wheels must be 1, 2, 3, or 4.")

    # Getter and setter for the brake type ("hand brakes" or "foot brakes")
    def getBrake(self) -> str:
        return self.__brake

    def setBrake(self, brake: str) -> None:
        """Set the brake type (hand brakes or foot brakes)."""
        if brake in ["hand brakes", "foot brakes"]:
            self.__brake = brake
            print(f"Brake type set to: {self.__brake}")
        else:
            raise ValueError('Brake type must be "hand brakes" or "foot brakes".')

    # Reset gear to 1
    def reset_gear(self):
        self.__current_gear = 1

    # Increase the current gear by 1
    def increaseGear(self) -> None:
        """Increase the current gear by 1, not exceeding the total number of gears."""
        if self.__current_gear < self.__gear:
            self.__current_gear += 1
            print(f"Gear increased to: {self.__current_gear}")
        else:
            print(f"Cannot increase gear. Already at maximum gear: {self.__gear}.")

    # Decrease the current gear by 1
    def decreaseGear(self) -> None:
        """Decrease the current gear by 1, but not below 1."""
        if self.__current_gear > 1:
            self.__current_gear -= 1
            print(f"Gear decreased to: {self.__current_gear}")
        else:
            print("Cannot decrease gear. Already at minimum gear: 1.")

