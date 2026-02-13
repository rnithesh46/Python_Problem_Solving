class A:
    def show(self):
        print("showing A")
class B:
    def show(self):
        print("showing B")
class C(A,B):
        pass

obj=C()
obj.show()