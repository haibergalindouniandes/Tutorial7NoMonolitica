from aeroalpes.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from aeroalpes.seedwork.aplicacion.queries import ejecutar_query as query
from aeroalpes.modulos.vuelos.infraestructura.repositorios import RepositorioReservas
from aeroalpes.modulos.vuelos.dominio.entidades import Reserva
from dataclasses import dataclass
from .base import ReservaQueryBaseHandler
from aeroalpes.modulos.vuelos.aplicacion.mapeadores import MapeadorReserva
import uuid

@dataclass
class ObtenerReserva(Query):
    id: str

class ObtenerReservaHandler(ReservaQueryBaseHandler):

    def handle(self, query: ObtenerReserva) -> QueryResultado:
        print("<==================== ObtenerReservaHandler.handle ========================>")
        print(query)
        vista = self.fabrica_vista.crear_objeto(Reserva)
        print(vista)
        # reserva =  self.fabrica_vuelos.crear_objeto(vista.obtener_por(id=query.id)[0], MapeadorReserva())
        reserva =  self.fabrica_vuelos.crear_objeto(vista.obtener_por(id=query.id), MapeadorReserva())
        print(reserva)
        print("<==================== ObtenerReservaHandler.handle ========================>")
        return QueryResultado(resultado=reserva)

@query.register(ObtenerReserva)
def ejecutar_query_obtener_reserva(query: ObtenerReserva):
    handler = ObtenerReservaHandler()
    return handler.handle(query)