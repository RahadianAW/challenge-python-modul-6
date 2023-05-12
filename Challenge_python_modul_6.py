from abc import ABC, abstractmethod
class Vehicle(ABC):
    model = None
    year = None
    color = None
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    @abstractmethod
    def honk(self):
        pass


class Car(Vehicle):
    def __init__(self,model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def setModel(self, model):
        self.model = model
        pass

    def getModel(self):
        return self.model

    def go(self):
        print("This " + self.color + " " + self.model + " is driving")

    def stop(self):
        print("This " + self.color + " " + self.model + " is stopped")
    def honk(self):
        print("This " + self.color + " " + self.model + " is HONKING LOUDY")

class Motorcycle(Vehicle):
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def setModel(self, model):
        self.model = model
        pass

    def getModel(self):
        return self.model
    
    def go(self):
        print("This " + self.color + " " + self.model + " is driving")

    def stop(self):
        print("This " + self.color + " " + self.model + " is stopped")

    def honk(self):
        print("This " + self.color + " " + self.model + " is HONKING LOUDY")

class truck(Vehicle):
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def setModel(self, model):
        self.model = model
        pass

    def getModel(self):
        return self.model
    
    def go(self):
        print("This " + self.color + " " + self.model + " is driving")

    def stop(self):
        print("This " + self.color + " " + self.model + " is stopped")

    def honk(self):
        print("This " + self.color + " " + self.model + " is HONKING LOUDY")


car = Car("Corvette", 2021, "blue")
print("Car Model : " + car.getModel())
print("Year : " + str(car.year))
print("Color : " + car.color)
car.go()
car.stop()
car.honk()
print("---------------------------------------")
motorcycle = Motorcycle("Ducati", 2020, "grey")
print("Motorcycle Model : " + motorcycle.getModel())
print("Year : " + str(motorcycle.year))
print("Color : " + motorcycle.color)
motorcycle.go()
motorcycle.stop()
motorcycle.honk()
print("---------------------------------------")
truck = truck("Fuso", 2020, "green")
print("Truck Model : " + truck.getModel())
print("Year : " + str(truck.year))
print("Color : " + truck.color)
truck.go()
truck.stop()
truck.honk()