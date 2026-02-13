class BandAccount:
    def __init__(self, name,accn,balance):
        self.name = name
        self.accn = accn
        self.__balance = balance
    def getBalance(self):
        return self.__balance
    def setBalance(self,balance):
        self.__balance = balance

acc1=BandAccount("bavi",123456789,100000    )
print(acc1.getBalance())
acc1.setBalance(150000)
print(acc1.getBalance())