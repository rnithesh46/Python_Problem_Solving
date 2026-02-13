from abc import ABC,abstractmethod
class Veichel(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Veichel):
    def start(self):
        print("Vechiel is car")

C=Car()
C.start()