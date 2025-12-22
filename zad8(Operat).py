from typing import List
import requests
import argparse

URL_API = 'https://api.openbrewerydb.org/v1/breweries'


class Brewery:
    def __init__(self, name):
        self.name = name
        # TODO: add rest of arguments

    def __str__(self):
        # TODO: return string describing class
        pass


def get_breweries_from_api(city: str|None) -> list:
    if city is not None:
        return requests.get(f'{URL_API}?by_city={city}').json()

    return requests.get(URL_API).json()


def brewery_factory(breweries: list) -> List[Brewery]:
    # TODO: run loop over all breweries to create list of Brewery
    pass

def get_args():
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-c', '--city', help='Filter brewery by city', required=False)
    return vars(parser.parse_args())


def main():
    args = get_args()
    breweries = get_breweries_from_api(city=args['city'])

    print(f'{breweries}')
    print(f'{len(breweries)}')

main()