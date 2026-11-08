# ============================================================
# cliente.py
# Responsable: César José Ledesma Frieri
# Contiene la clase abstracta EntidadBase y la clase Cliente.
# ============================================================

from abc import ABC, abstractmethod             # para crear clases abstractas
from excepciones import ClienteInvalidoError    # nuestro error personalizado


# ------------------------------------------------------------
# CLASE ABSTRACTA: representa cualquier entidad del sistema.
# No se pueden crear objetos de ella, solo sirve de molde.
# ------------------------------------------------------------
class EntidadBase(ABC):

    def __init__(self, codigo):
        self._codigo = codigo          # código que identifica la entidad

    def obtener_codigo(self):
        return self._codigo

    # Toda entidad debe saber describirse a sí misma
    @abstractmethod
    def describir(self):
        pass


# ------------------------------------------------------------
# CLASE CLIENTE (hereda de EntidadBase)
# Los datos personales están encapsulados con "__",
# así no se pueden cambiar directamente desde afuera.
# ------------------------------------------------------------
class Cliente(EntidadBase):

    def __init__(self, codigo, nombre, correo, telefono):
        super().__init__(codigo)               # llama al constructor del padre
        self.__nombre = self.__validar_nombre(nombre)
        self.__correo = self.__validar_correo(correo)
        self.__telefono = self.__validar_telefono(telefono)

    # ---- Validaciones (métodos privados) ----
    def __validar_nombre(self, nombre):
        if not nombre or nombre.strip() == "":         # vacío o solo espacios
            raise ClienteInvalidoError("El nombre del cliente no puede estar vacío")
        return nombre.strip()

    def __validar_correo(self, correo):
        if "@" not in correo or "." not in correo:     # un correo debe tener @ y punto
            raise ClienteInvalidoError(f"El correo '{correo}' no es válido")
        return correo

    def __validar_telefono(self, telefono):
        if not telefono.isdigit() or len(telefono) != 10:   # 10 números exactos
            raise ClienteInvalidoError(f"El teléfono '{telefono}' debe tener 10 números")
        return telefono

    # ---- Métodos para leer los datos (getters) ----
    def obtener_nombre(self):
        return self.__nombre

    def obtener_correo(self):
        return self.__correo

    # ---- Método para cambiar el correo, validando primero (setter) ----
    def cambiar_correo(self, nuevo_correo):
        self.__correo = self.__validar_correo(nuevo_correo)

    # Implementación del método abstracto
    def describir(self):
        return f"Cliente {self._codigo}: {self.__nombre} ({self.__correo})"
