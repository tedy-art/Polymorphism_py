What is ploymorphism??
->  ploymorphism refers to having multiple forms.
->  ploymorphism is a programming term refers to use of the same function 
    name but with deffernt signatures, for multiple types:-

    ex> In-built 
        #len() function is used for string
        print(len("Python"))

        # len() function is used for list
        print(len([100,210,130,321]))

    o/p>
        6
        4

    ex> User-defined
        def add(p,q,r=0)
            return p+q+r

        print(add(6,23))
        print(add(22,31, 544))

    o/p>
        29
        597

** How to use ploymorphism:??
types of ploymorphism:-
    1) Overloading
        I) Operator Overloading
        II) Method Overloading
    2) Overriding
        I) Method Overriding
        II) Variable Overriding

1) Overloading
I) Operator Overloading:-
    Operator Overloading is the type of Overloading in which an Operator can be used in multiple ways beyond its predefined meaning.

    e.g.

        print(2 * 7)
        >>> 14

        print('a' * 3)
        >>> aaa

        print('10' + '20')
        >>> 1020

        print(10 + 20)
        >>> 30

    **practical implementation of Operator Overloading**
    e.g.
            class vehicle:
                def __init__(self, fare):
                    self.fare = fare

            bus = vehicle(20)
            car = vehicle(30)
            total_fare = bus + car
            print(total_fare)
    o/p:
        Error
        TypeErro: unsupported operand type(s) for + : 'vehicle'

    ** New we will Overload the special function __add__ Operator**
    e.g.

            class vehicle:
                def __init__(self, fare):
                    self.fare = fare

                def __add__(self, other):
                    return self.fare + other.fare

            bus = vehicle(20)
            car = vehicle(30)
            total_fare = bus + car
            print(total_fare)

    o/p:
        50

    e.g.
        class Book:
            def __init__(self, nm, pr, pgs):
                self.book_name = nm
                self.price = pr
                self.pages = pgs

            def __add__(self, other):
                return self.price + other.price
        
        b1 = ("Basic Python", 250, 300)

        b2 = ("Advance Python", 450, 700)

        print(b1 + b2)

    o/p:-
        112500

    
II) Method Overloading:
->  Python is Dynamically typed language that why there is no need of Method
    Overloading.
->  Method Overloading is not there in Python.
->  Constructor Overloading is not there in Python.
->  If we try to Overload Constructor/Method the PVM(Python Virtual Machine)
    will run last or the most recent Construct Method/Constructor.

e.g.
    class Person:
        def __init__(self, nm):
            self.name = nm

        def __init__(self, nm, age):
            self.name = nm
            self.age = age

        def __init__(self.nm, age, wt):
            self.name = nm
            self.age = age
            self.waight = wt

    p1 = Person('jay')
o/p:
    TypeError: Person.__init__() mising 2 required positinal argument: 'age' and 'wt'

e.g.
    class Person:
        def __init__(self, nm):
            self.name = nm

        def __init__(self, nm, age):
            self.name = nm
            self.age = age

        def __init__(self.nm, age, wt):
            self.name = nm
            self.age = age
            self.waight = wt

        def print_details(self):
            print(f"name is {self.name}, age is {self.age}, and waight is {self.waight}.")
    p1 = Person('jay', 24, 60)

o/p: 
    name is jay, age is 24, and waight is 60.

2) Overriding
I) Method Overriding:-