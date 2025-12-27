class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, area, rooms, price, address, plot: int):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address
        self.plot = plot

    def __str__(self):
        return f'Powierzchnia domu: {self.area}, pokoje: {self.rooms}, cena: {self.price}, adres:  {self.address}, powierzchnia działki:  {self.plot}'


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address
        self.floor = floor

    def __str__(self):
        return f'Powierzchnia domu: {self.area}, pokoje: {self.rooms}, cena: {self.price}, adres:  {self.address}, ilośc poziomów:  {self.floor}'
