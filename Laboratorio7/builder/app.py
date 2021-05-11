from handlers import ScoreBuilderHandler


def risk_score():
    client_1 = ScoreBuilderHandler.director_client_1()
    print(client_1)
    client_2 = ScoreBuilderHandler.director_client_2()
    print(client_2)


risk_score()
