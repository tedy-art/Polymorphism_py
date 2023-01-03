class Parent:
    def property(self):
        print("This is parent property..")

    def marry(self): # Overridn method
        print("Our child will marrry with Girl A..")


class Child(Parent):
    def property1(self):
        print("This is child's property..")

    def marry(self):  # Overring Parent's method
        print("I will mary with Girl B..")
        super().marry()  # Our child will marrry with Girl A..


jay = Child()
jay.property1()
jay.property()
jay.marry()