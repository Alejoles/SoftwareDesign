import requests


def suma_fake(function):
    def wrapper(num):
        if num % 2 == 0:
            return function(num)
        else:
            num = 100
            return function(num)
    return wrapper


def consulta_continente(function):
    def wrapper(continente):
        if continente == "asia":
            response = requests.get(f"https://restcountries.eu/rest/v2/region/{continente}")
            print(
                response
            )
        else:
            return function()
    return wrapper
