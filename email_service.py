from abc import ABC, abstractmethod

class EmailService(ABC):
    @abstractmethod
    def send_result(self, message):
        pass

class FakeEmailService(EmailService):
    def send_result(self, message):
        print("Email:", message)