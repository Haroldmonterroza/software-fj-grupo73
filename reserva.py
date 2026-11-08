# ============================================================
# reserva.py
# Responsable: Gilbert Andrés Rojas Jiménez
# Clase Reserva: une un cliente con un servicio y una duración.
# ============================================================

from excepciones import ReservaError, OperacionNoPermitidaError, ServicioNoDisponibleError
from registro import registrar_evento, registrar_error


class Reserva:

    def __init__(self, cliente, servicio, horas):
        # try / except con encadenamiento: si algo falla al revisar,
        # se lanza un ReservaError que guarda el error original ("from e")
        try:
            servicio.verificar_disponible()
            horas = float(horas)                       # las horas deben ser un número
        except ServicioNoDisponibleError as e:
            raise ReservaError("No se puede reservar un servicio no disponible") from e
        except ValueError as e:
            raise ReservaError(f"La duración '{horas}' no es un número") from e

        if horas <= 0:
            raise ReservaError("La duración de la reserva debe ser mayor que cero")

        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "Pendiente"                      # estados: Pendiente, Confirmada, Cancelada

    # Confirmar la reserva  (try / except / else)
    def confirmar(self):
        try:
            if self.estado != "Pendiente":
                raise OperacionNoPermitidaError(f"No se puede confirmar una reserva {self.estado}")
        except OperacionNoPermitidaError as e:
            registrar_error(str(e))                    # se anota el error en el log
            raise                                      # se vuelve a lanzar para que main lo vea
        else:
            # el else solo se ejecuta si NO hubo error
            self.estado = "Confirmada"
            registrar_evento(f"Reserva confirmada para {self.cliente.obtener_nombre()}")

    # Cancelar la reserva
    def cancelar(self):
        if self.estado == "Cancelada":
            registrar_error("Se intentó cancelar una reserva ya cancelada")
            raise OperacionNoPermitidaError("La reserva ya estaba cancelada")
        self.estado = "Cancelada"
        registrar_evento(f"Reserva cancelada para {self.cliente.obtener_nombre()}")

    # Procesar la reserva: calcula el costo final  (try / except / finally)
    def procesar(self, impuesto=None, descuento=None):
        try:
            if self.estado != "Confirmada":
                raise ReservaError("Solo se pueden procesar reservas confirmadas")
            costo = self.servicio.calcular_costo(self.horas, impuesto, descuento)
            registrar_evento(f"Reserva procesada: {self.servicio.nombre} - ${costo}")
            return costo
        except ReservaError as e:
            registrar_error(str(e))
            raise
        finally:
            # el finally se ejecuta SIEMPRE, haya error o no
            print("   (Proceso de la reserva terminado)")

    def describir(self):
        return (f"{self.cliente.obtener_nombre()} - {self.servicio.nombre} - "
                f"{self.horas} h - {self.estado}")
