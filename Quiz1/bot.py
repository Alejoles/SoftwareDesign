from abc import ABC, abstractmethod


class Command(ABC):
    """
    La interface Command declara un metodo para ejecutar una instruccion
    """

    @abstractmethod
    def execute(self) -> None:
        pass


# INVOKER
class Bot:
    """
    El invocador esta asociado con uno o con muchos comandos, este envia una peticion a el comando
    """

    def __init__(self, command):
        self.command = command

    def set_command(self, command):
        self.command = command

    def execute_command(self):
        self.command.execute()
