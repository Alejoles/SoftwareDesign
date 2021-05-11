import requests


def verify_region(region):
    regions = {
        "BRA": "br1", "EUN": "eun1", "EUW": "euw1", "JAPAN": "jp1", "KOREA": "kr", "LAN": "la1",
        "LAS": "la2", "NA": "na1", "OC": "oc1", "RU": "ru", "TR": "tr1"
    }

    if region in regions:
        return regions[f"{region}"]
    else:
        return False


def consulta_lol_invocador(function):
    def wrapper(region, name, APIKey):
        if type(verify_region(region)) == type(" "):
            selected_region = verify_region(region)
        else:
            return function(region, "", "")

        response = requests.get(
            f"https://{selected_region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?api_key={APIKey}")
        return response.json()

    return wrapper


def consulta_lol_ranked(function):
    def wrapper(region, id, APIKey):
        if type(verify_region(region)) == type(" "):
            selected_region = verify_region(region)
        else:
            return function(region, "", "")

        response = requests.get(
            f"https://{selected_region}.api.riotgames.com/lol/league/v4/entries/by-summoner/{id}?api_key={APIKey}")
        return response.json()
    return wrapper
