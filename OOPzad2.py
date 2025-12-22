import Libraries_project_class

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
        return (f"Imię i nazwisko pracownika: {self.first_name} {self.last_name}, Data urodzenia: {self.birth_date}, Data zatrudnienia: {self.hire_data} "
                f"Telefon: {self.phone}, Dane pracownika: {self.street}, {self.zip_code}, {self.city}")


class Book:
    def __init__(self, title, library, publication_date, author_name, author_surname, number_of_pages):
        self.title = title
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages
    def __str__(self):
        return(f"Autor:{self.author_name}, {self.author_surname}, Liczba stron: {self.number_of_pages}, Data wydania: {self.publication_date}, Biblioteka: {self.library}")

class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return(f"Pracownik: {self.employee}, Wypozyczył: {self.student}, Książki:{self.books}, Data zamówienia:{self.order_date}")



class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return(f'Student: + {self.first_name}  + {self.last_name}')


#Biblioteki
mbpkatowice = Library(city = 'Katowice', street='Chrobrego 2', zip_code = '40-871', open_hours= '8-16', phone='+32 555 555')
mpbtychy = Library (city='Tychy', street= 'Piłsudskiego 10', zip_code='43-102', open_hours= '8-16', phone='+32 111 111' )
#Książki
wladca_pierscieni = Book(title = 'Władca Pierscieni', library = mbpkatowice, publication_date='1955', author_name='J.R.R.', author_surname='Tolkien', number_of_pages='600')
hobbit = Book(title = 'Hobbit', library=mbpkatowice, publication_date='1955', author_name='J.R.R.', author_surname='Tolkien', number_of_pages='200')
historia_chorzowa = Book(title = 'Historia Chorzowa', library=mpbtychy, publication_date='2000', author_name='Jan', author_surname='Drabina', number_of_pages='330')
Swiaty_tolkiena = Book(title = 'Światy Tolkiena', library=mbpkatowice, publication_date='2015', author_name='John', author_surname='Garth', number_of_pages='180')
Niemiecki_nie_gryzie = Book(title = 'Niemiecki nie gryzie', library=mpbtychy, publication_date='2020', author_name='Autor', author_surname='Nieznany', number_of_pages='135')
#pracownicy
jan_kowalski = Employee(first_name="Jan", last_name="Kowalski", hire_data="01-01-2012", birth_date="02-04-1977", phone='+32 123 456', street="Jodłowa 2", zip_code=' 11-111', city="Bytom")
jan_nowak = Employee(first_name="Jan", last_name="Nowak", hire_data="05-10-2018", birth_date="12-06-1972", phone='+32 321 654', street="Główna 6", zip_code=' 22-121', city="Chorzów")
tomasz_nowak = Employee(first_name="Tomasz", last_name="Nowak", hire_data="10-07-2003", birth_date="11-10-1968", phone='+32 333 333', street="Wschodnia 12/6", zip_code=' 44-144', city="Zabrze")
#studenci
Adam_Niezgodka = Student(first_name="Adam", last_name="Niezgodka", )
Ambrozy_Kleks = Student(first_name="Ambrozy", last_name="Kleks", )
Filip_Golarz = Student(first_name="Filip", last_name="Golarz", )
#zamówienia
zamowienie1 = Order(employee= jan_nowak.first_name + jan_nowak.last_name, student= Filip_Golarz.first_name + Filip_Golarz.last_name, books= wladca_pierscieni.title + hobbit.title, order_date='2-2-2025')
zamowienie2 = Order(employee=jan_kowalski.first_name + jan_kowalski.last_name, student=Ambrozy_Kleks.first_name + Ambrozy_Kleks.last_name, books= historia_chorzowa.title + Niemiecki_nie_gryzie.title, order_date= '4-2-2026')


print(zamowienie1)
print(zamowienie2)




