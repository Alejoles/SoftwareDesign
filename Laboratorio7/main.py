from factory import Factory
from decorators import suma_fake, consulta_continente


@suma_fake
def suma(num):
    return num + 2


@suma_fake
def suma2(num):
    return num + 2

@consulta_continente
def alerta_continente(continente=None):
    return "Continente no soportado"


print(alerta_continente("europa"))

print("=================")

print(suma(3))

print(suma2(6))

print("=================")

object_factory = Factory("Products").get_instance()
print(object_factory().get_name())
