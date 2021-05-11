from bot import Bot
from commands import *


turn_on = TurnOn()
turn_off = TurnOff()
speak = Speak()
sleep = Sleep()

object_bot = Bot(turn_on)
object_bot.execute_command()
object_bot.set_command(turn_on)
