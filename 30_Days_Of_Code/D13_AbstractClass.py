from abc import ABCMeta, abstractmethod
class Book(object, metaclass = ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author
    @abstractmethod
    def display(): pass

class MyBook(Book):
    def __init__(self, title, author, price):           # Creo una subclase de Book con los datos que necesito
        Book.__init__(self, title, author)              # Traigo los datos que necesito de la clase madre Book
        self.price = price                              # Tomo el valor que no tiene la clase madre

    def display(self):                                  # Creo el display
        print('Title: ' + self.title)                   # Accedo al valor de la clase madre
        print('Author: ' + self.author)                 
        print('Price: ' + str(self.price))              # Accedo al valor del precio propio de esta clase. 
