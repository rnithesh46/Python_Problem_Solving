# class Sample:
#     num=10
#     def Method():
#         print("Hello")

class Mobile:
    def __init__(self):
        pass
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def display(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
        print("Price:",self.price) 

m1=Mobile("Apple","iPhone 14 Pro",120000)
m1.display()
        
# Example of default constructor