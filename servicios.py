# ============================================================
# servicios.py
# Responsable: Harold Monterroza Díaz
# Contiene la clase abstracta Servicio y los tres servicios
# que ofrece Software FJ.
# ============================================================

from abc import ABC, abstractmethod
from excepciones import ServicioInvalidoError, ServicioNoDisponibleError


# ------------------------------------------------------------
# CLASE ABSTRACTA SERVICIO
# ------------------------------------------------------------
class Servicio(ABC):

    def __init__(self, nombre, precio_hora):
        if precio_hora <= 0:                           # el precio debe ser positivo
            raise ServicioInvalidoError(f"El precio de '{nombre}' debe ser mayor que cero")
        self.nombre = nombre
        self.precio_hora = precio_hora
        self.disponible = True                         # todo servicio empieza disponible

    # SOBRECARGA SIMULADA: el mismo método se puede usar de 3 formas
    #   calcular_costo(horas)                     -> costo normal
    #   calcular_costo(horas, impuesto=0.19)      -> con impuesto
    #   calcular_costo(horas, descuento=0.10)     -> con descuento
    def calcular_costo(self, horas, impuesto=None, descuento=None):
        costo = self.costo_base(horas)                 # cada servicio calcula su base
        if descuento is not None:
            costo = costo - costo * descuento          # se resta el descuento
        if impuesto is not None:
            costo = costo + costo * impuesto           # se suma el impuesto
        return round(costo, 2)

    # Revisa que el servicio se pueda usar
    def verificar_disponible(self):
        if not self.disponible:
            raise ServicioNoDisponibleError(f"El servicio '{self.nombre}' no está disponible")

    # Métodos que cada servicio debe implementar a su manera (polimorfismo)
    @abstractmethod
    def costo_base(self, horas):
        pass

    @abstractmethod
    def describir(self):
        pass

    @abstractmethod
    def validar_parametros(self):
        pass


# ------------------------------------------------------------
# SERVICIO 1: RESERVA DE SALA
# ------------------------------------------------------------
class ReservaSala(Servicio):

    def __init__(self, nombre, precio_hora, capacidad):
        super().__init__(nombre, precio_hora)
        self.capacidad = capacidad
        self.validar_parametros()

    def validar_parametros(self):
        if self.capacidad <= 0:
            raise ServicioInvalidoError("La capacidad de la sala debe ser mayor que cero")

    def costo_base(self, horas):
        return self.precio_hora * horas                # precio por hora

    def describir(self):
        return f"Sala '{self.nombre}' para {self.capacidad} personas - ${self.precio_hora}/hora"


# ------------------------------------------------------------
# SERVICIO 2: ALQUILER DE EQUIPOS
# ------------------------------------------------------------
class AlquilerEquipo(Servicio):

    def __init__(self, nombre, precio_hora, cantidad):
        super().__init__(nombre, precio_hora)
        self.cantidad = cantidad
        self.validar_parametros()

    def validar_parametros(self):
        if self.cantidad <= 0:
            raise ServicioInvalidoError("La cantidad de equipos debe ser mayor que cero")

    def costo_base(self, horas):
        return self.precio_hora * horas * self.cantidad   # se cobra cada equipo

    def describir(self):
        return f"Alquiler de {self.cantidad} '{self.nombre}' - ${self.precio_hora}/hora c/u"


# ------------------------------------------------------------
# SERVICIO 3: ASESORÍA ESPECIALIZADA
# ------------------------------------------------------------
class Asesoria(Servicio):

    def __init__(self, nombre, precio_hora, especialista):
        super().__init__(nombre, precio_hora)
        self.especialista = especialista
        self.validar_parametros()

    def validar_parametros(self):
        if self.especialista.strip() == "":
            raise ServicioInvalidoError("La asesoría debe tener un especialista")

    def costo_base(self, horas):
        return self.precio_hora * horas + 50000       # tarifa fija de 50.000 por asesoría

    def describir(self):
        return f"Asesoría '{self.nombre}' con {self.especialista} - ${self.precio_hora}/hora"
