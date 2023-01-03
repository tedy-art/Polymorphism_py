class Person:
    def __init__(self, nm):
        self.name = nm

    def __init__(self, nm, age):
        self.name = nm
        self.age = age
    
    def __init__(self, nm, age, wt):
        self.name = nm
        self.age = age
        self.waight = wt

    def print_details(self):
            print(f"name is {self.name}, age is {self.age}, and waight is{self.waight}.")


print('*'*40, '\n\n')
p1 = Person('Jay', 24, 60)
p1.print_details()
print('*'*40, '\n\n')

p2 = Person('Jay')
# TypeError: Person.__init__() missing 2 required positional arguments: 'age' and 'wt'
