import requests
import typing
import json
import dataclasses


class Browar:
    def __init__(self, id, name, brewery_type, address_1, address_2, address_3, city, state_province, postal_code, country, longitude, latitude, phone, website_url, state, street):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.address_1 = address_1
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state_province = state_province
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
        self.state = state
        self.street = street

    def __str__(self):
        return str(f"Browar {self.name} typu {self.brewery_type}, "
                   f" adres {self.address_1}, {self.address_2}, {self.address_3} w {self.city}, {self.state_province}, {self.postal_code}, {self.country}."
                   f"Telefon: {self.phone}, strona {self.website_url}"
                   f"Stan i ulica: {self.state}, {self.street}"
                   f" Jego współrzedne to {self.longitude} {self.latitude}"
                   )


def pobierz_browary(api_url: str, limit: int = 20) -> list[Browar]:

    params = {'per_page': limit}
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()

        data: list[dict[str, any]] = response.json()
        browary_lista: list[Browar] = []

        for browar_dict in data:
            browar_obj = Browar(**browar_dict)
            browary_lista.append(browar_obj)
        return browary_lista

    except requests.exceptions.RequestException as e:
        print(f"Nie mozna połączyć z API: {e}")
        return []


if __name__ == "__main__":
    api_url = "https://api.openbrewerydb.org/v1/breweries"
    liczba_browarow = 20

    browary_lista = pobierz_browary(api_url, liczba_browarow)
    if browary_lista:
        print("\n" + "=" * 80)
        print(f"Wyświetlanie informacji dla {len(browary_lista)} browarów:")
        print("=" * 80 + "\n")

        for Browar in browary_lista:

            print(Browar)
