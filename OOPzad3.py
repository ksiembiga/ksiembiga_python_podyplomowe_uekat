import Property_classes

class Property :
    def __init__(self,area, rooms:int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self,area, rooms, price, address, plot:int):
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



domek_w_gorach = House(area='200', rooms=8, price= '700000', address='ul. lesna12, ustron', plot=900)
mieszkanie_w_miescie = Flat(area='80', rooms = 4, price ='450000', address='ul. Miejska, Bielsko-Biała', floor='1')

print(domek_w_gorach)
print(mieszkanie_w_miescie)