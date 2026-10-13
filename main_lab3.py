from triangle_calculator import TriangleCalculator
from database import Database
from user_interface import ConsoleUserInterface
from email_service import FakeEmailService
from controller import Controller

def main():
    calculator = TriangleCalculator()
    db = Database()
    ui = ConsoleUserInterface()
    email_service = FakeEmailService()
    controller = Controller(calculator, db, ui, email_service)

    result = controller.process_triangle()
    print(result)

if __name__ == "__main__":
    main()