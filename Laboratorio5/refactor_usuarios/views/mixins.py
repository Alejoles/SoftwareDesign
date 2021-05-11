from refactor_usuarios.views.products_views import Vehiculo
from refactor_usuarios.views.products_views import Conductor


class ParMixin(Vehiculo, Conductor):
    def valida_conductor_vehiculo(self):
        pass
