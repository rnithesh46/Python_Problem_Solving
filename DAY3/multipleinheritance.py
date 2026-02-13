class Father:
    def showA(self):
        print("class A")

class Mother:
    def showB(self):
        print("class B")

class Child(Father, Mother):
    def showC(self):
        print("class C")