# ============================================================
# excepciones.py
# Responsable: César José Ledesma Frieri
# Aquí se crean las excepciones personalizadas del sistema.
# Una excepción personalizada es un error con nombre propio,
# así sabemos exactamente qué salió mal.
# ============================================================


# Excepción general del sistema: todas las demás heredan de esta
class SoftwareFJError(Exception):
    pass


# Error cuando los datos de un cliente no son válidos
class ClienteInvalidoError(SoftwareFJError):
    pass


# Error cuando un servicio se crea con datos incorrectos
class ServicioInvalidoError(SoftwareFJError):
    pass


# Error cuando un servicio no está disponible
class ServicioNoDisponibleError(SoftwareFJError):
    pass


# Error cuando una reserva no se puede hacer o procesar
class ReservaError(SoftwareFJError):
    pass


# Error cuando se intenta una operación que no está permitida
# (por ejemplo, cancelar una reserva ya cancelada)
class OperacionNoPermitidaError(SoftwareFJError):
    pass
