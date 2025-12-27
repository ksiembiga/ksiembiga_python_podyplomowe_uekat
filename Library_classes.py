class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (f"Adres:  {self.street}, {self.zip_code}, {self.city}, Godziny otwarcia: {self.open_hours}, Telefon: {self.phone}")


class Employee:
    def __init__(self, first_name, last_name, hire_data, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_data = hire_data
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (f"Imię i nazwisko pracownika: {self.first_name} {self.last_name}, Data urodzenia: {self.birth_date}, Data zatrudnienia: {self.hire_data},"
                f" Telefon: {self.phone}, Dane pracownika: {self.street}, {self.zip_code}, {self.city}")


class Book:
    def __init__(self, title, library, publication_date, author_name, author_surname, number_of_pages):
        self.title = title
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (f"Autor:{self.author_name}, {self.author_surname}, Liczba stron: {self.number_of_pages}, Data wydania: {self.publication_date}, Biblioteka: {self.library}")


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return (f"Pracownik: {self.employee}, Wypozyczył: {self.student}, Książki:{self.books}, Data zamówienia:{self.order_date}")


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return (f'Student: + {self.first_name}  + {self.last_name}')
