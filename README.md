# Software FJ – Sistema de Gestión de Clientes, Servicios y Reservas

Proyecto de la **Fase 4 – Prácticas simuladas** del curso **Programación (213023)** de la UNAD, grupo **213023_73**.

Sistema orientado a objetos, sin base de datos, que gestiona clientes, servicios (reserva de salas, alquiler de equipos y asesorías) y reservas, con manejo de excepciones y registro de errores en un archivo de logs.

## Integrantes

| Integrante | Archivos |
|---|---|
| César José Ledesma Frieri | `excepciones.py`, `registro.py`, `cliente.py` |
| Harold Monterroza Díaz | `servicios.py`, `main.py` |
| Gilbert Andrés Rojas Jiménez | `reserva.py`, `README.md` |

## Conceptos aplicados

- **Abstracción:** clases abstractas `EntidadBase` y `Servicio`.
- **Herencia:** `Cliente` hereda de `EntidadBase`; `ReservaSala`, `AlquilerEquipo` y `Asesoria` heredan de `Servicio`.
- **Polimorfismo:** cada servicio implementa a su manera `costo_base()`, `describir()` y `validar_parametros()`.
- **Encapsulación:** los datos personales del cliente son privados (`__nombre`, `__correo`, `__telefono`).
- **Sobrecarga:** `calcular_costo(horas, impuesto=None, descuento=None)` funciona sin parámetros opcionales, con impuesto o con descuento.
- **Excepciones:** excepciones personalizadas, `try/except`, `try/except/else`, `try/except/finally` y encadenamiento con `raise ... from`.
- **Logs:** todos los eventos y errores se guardan en `eventos.log`.

## Cómo ejecutarlo

1. Tener Python 3.9 o superior.
2. Descargar todos los archivos en la misma carpeta.
3. Ejecutar `python main.py`.
4. Revisar la salida en la terminal y el archivo `eventos.log`.
