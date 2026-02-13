class Parent:
    def __init__(self):
        print("Parent class constructor")
class Child(Parent):
    def __init__(self):
        print("Child class constructor")
    pass
obj=Child()