from bot import Command


class TurnOn(Command):
    def __init__(self):
        self.message = "Initializing system"

    def execute(self):
        print(self.message)


class TurnOff(Command):
    def __init__(self):
        self.message = "Shutting down system"

    def execute(self):
        print(self.message)


class Speak(Command):
    def __init__(self):
        self.message = "Hello, i'm Bot"

    def execute(self):
        print(self.message)


class Sleep(Command):
    def __init__(self):
        self.message = "ZzZzZzZzZz"

    def execute(self):
        print(self.message)

