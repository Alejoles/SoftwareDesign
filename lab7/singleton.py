class Singleton:
    instance = None

    def __new__(cls):
        if not Singleton.instance:
            Singleton.instance = object.__new__(cls)
        return Singleton.instance

    def __str__(self):
        return "Hola"


object_singleton1 = Singleton()
object_singleton2 = Singleton()
print("=================Singleton=====================")
print(id(object_singleton1))
print(id(object_singleton2))


class SinSingleton:
    def __init__(self):
        pass


object_singleton1_a = SinSingleton()
object_singleton1_b = SinSingleton()
print("=================SinSingleton=====================")
print(id(object_singleton1_a))
print(id(object_singleton1_b))
