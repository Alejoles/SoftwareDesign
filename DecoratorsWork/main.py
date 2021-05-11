from decorator import consulta_lol_invocador, consulta_lol_ranked


@consulta_lol_invocador
def consulta_lol(region, name, APIkey):
    return f"There was an error. HINT: {region}, {name}"

@consulta_lol_ranked
def consulta_ranked(region, id, APIKey):
    return "There was an error..."


def main():

    print("BRA, EUN, EUW, JAPAN, KOREA ,LAN, LAS, NA, OC, RU, TR")
    region = input("De las anteriores ingrese la región en la que se encuentra su cuenta: ")
    name = input("Ingrese su nombre de invocador: ")
    APIkey = input("Copie y pegue su API KEY desde www.developer.riotgames.com: ")
    response_json = consulta_lol(region, name, APIkey)
    if not response_json:
        return

    if len(consulta_ranked(region, response_json['id'], APIkey)) < 2:
        number = 1
    else:
        number = 2
    for i in range(0, number):
        response2_json = consulta_ranked(region, response_json['id'], APIkey)[i]
        print(response2_json['summonerName'])
        print(response2_json['queueType'])
        print(response2_json['tier'])
        print(response2_json['rank'])
        print('LP: ' + str(response2_json['leaguePoints']))
        print("------------")


if __name__ == "__main__":
    main()

