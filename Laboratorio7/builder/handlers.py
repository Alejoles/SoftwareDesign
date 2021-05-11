from builder.modelo1 import Modelo1
from builder.modelo2 import Modelo2
from builder.modelo3 import Modelo3


class ScoreBuilderHandler:
    @staticmethod
    def director_client_1():
        modelo_1 = Modelo1()
        modelo_2 = Modelo2()
        return (modelo_1.process() + modelo_2.process())/2

    @staticmethod
    def director_client_2():
        modelo_2 = Modelo2()
        modelo_3 = Modelo3()
        return (modelo_2.process() + modelo_3.process())/2
