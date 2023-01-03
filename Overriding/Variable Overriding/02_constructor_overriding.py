class Parson:
    def __init__(self, nm, age):
        self.name = nm
        self.age = age

class Student(Parson):
    def __init__(self, nm, age, rl, mks):
        super().__init__(nm, age)
        self.roll = rl
        self.marks = mks

s1 = Student('Jay', 24, 1, 85)
print(s1.name, s1.age)