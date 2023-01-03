class vehicle:
    def __init__(self, fare):
        self.fare = fare

    def __add__(self, other):
        return self.fare + other.fare # Operator Overloading '+'
    
bus = vehicle(20)

car = vehicle(30)
total_fare = bus + car
print(total_fare)