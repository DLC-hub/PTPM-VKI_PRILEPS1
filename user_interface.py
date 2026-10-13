from abc import ABC, abstractmethod

class UserInterface(ABC):
    @abstractmethod
    def get_sides(self):
        pass

class ConsoleUserInterface(UserInterface):
    def get_sides(self):
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        return a, b, c