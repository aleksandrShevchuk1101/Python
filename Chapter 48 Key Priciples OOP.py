# Encapsulation

# class Email:
#     def __init__(self, sender,  recipient, subject, body):
#         self.sender = sender
#         self.recipient = recipient
#         self.subject = subject
#         self.body = body


#     def send_email(self):
#         # Logic related to sening email
#         pass


#     def read_email(self):
#         # Logic 
#         pass


# Inheritance

# class Vehicle:
#     def __init__(self, make, model) -> None:
#         self.make = make
#         self.model = model


#     def start(self):
#         print("asdf")
#         # pass


#     def stop(self):
#         pass    


# class Car(Vehicle):

#     def __init__(self, make, model, doors_qty) -> None:
#         super().__init__(make, model)
#         self.doors_qty = doors_qty


#     def lock_doors(self):
#         pass


#     def unlock_doors(self):
#         pass


# Abstraction

from abc import ABC, abstractmethod

class Payment():

    @abstractmethod
    def process_payemt(self):
        pass



class CreditCardPayment(Payment):
    def process_payemt(seld):
        pass

class StripPayement(Payment):
    def process_payemt(seld):
        pass

class PayPalPayment(Payment):
    def process_payemt(seld):
        pass


