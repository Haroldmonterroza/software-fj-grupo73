# ============================================================
# main.py
# Responsable: Harold Monterroza Díaz
# Sistema de Gestión de Clientes, Servicios y Reservas
# Empresa: Software FJ - UNAD, Programación 213023, Grupo 73
#
# Simula 12 operaciones, unas correctas y otras con errores,
# para demostrar que el sistema NO se cierra ante los errores.
# ============================================================

from datetime import datetime
from cliente import Cliente
from servicios import ReservaSala, AlquilerEquipo, Asesoria
from reserva import Reserva
from excepciones import SoftwareFJError
from registro import registrar_evento, registrar_error

# Listas internas (no se usa base de datos)
clientes = []
servicios = []
reservas = []

print("=" * 60)
print(" SOFTWARE FJ - Sistema de clientes, servicios y reservas")
print(" Fecha:", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
print("=" * 60)
registrar_evento("----- Inicio de la simulación -----")


# ---------- Operación 1: cliente válido ----------
print("\n1. Registrar cliente válido")
try:
    c1 = Cliente("C01", "Ana Pérez", "ana@gmail.com", "3001234567")
    clientes.append(c1)
    registrar_evento("Cliente registrado: " + c1.obtener_nombre())
    print("   OK:", c1.describir())
except SoftwareFJError as e:
    registrar_error(str(e))
    print("   ERROR:", e)


# ---------- Operación 2: cliente con correo inválido ----------
print("\n2. Registrar cliente con correo sin @")
try:
    c2 = Cliente("C02", "Luis Gómez", "luisgmail.com", "3009876543")
    clientes.append(c2)
except SoftwareFJError as e:
    registrar_error(str(e))
    print("   ERROR:", e)


# ---------- Operación 3: cliente con nombre vacío ----------
print("\n3. Registrar cliente con nombre vacío")
try:
    c3 = Cliente("C03", "   ", "maria@gmail.com", "3015551234")
    clientes.append(c3)
except SoftwareFJError as e:
    registrar_error(str(e))
    print("   ERROR:", e)


# ---------- Operación 4: crear sala válida ----------
print("\n4. Crear servicio de sala válido")
try:
    sala = ReservaSala("Sala Juntas", 40000, 12)
    servicios.append(sala)
    registrar_evento("Servicio creado: " + sala.describir())
    print("   OK:", sala.describir())
except SoftwareFJError as e:
    registrar_error(str(e))
    print("   ERROR:", e)


# ---------- Operación 5: equipo con cantidad negativa ----------
print("\n5. Crear alquiler de equipo con cantidad negativa")
try:
    equipo_malo = AlquilerEquipo("Portátil", 15000, -3)
    servicios.append(equipo_malo)
except SoftwareFJError as e:
    registrar_error(str(e))
    print("   ERROR:", e)


# ---------- Operación 6: crear equipo y asesoría válidos ----------
print("\n6. Crear alquiler de equipo y asesoría válidos")
try:
    equipo = AlquilerEquipo("Video beam", 20000, 2)
    asesoria = Asesoria("Ciberseguridad", 80000, "Ing. Torres")
    servicios.append(equipo)
    servicios.append(asesoria)
    registrar_evento("Servicios creados: equipo y asesoría")
    print("   OK:", equipo.describir())
    print("   OK:", asesoria.describir())
except SoftwareFJError as e:
    registrar_error(str(e))
    print("   ERROR:", e)


# ---------- Operación 7: reserva válida y confirmada ----------
print("\n7. Crear y confirmar una reserva válida")
try:
    r1 = Reserva(c1, sala, 3)
    r1.confirmar()
    reservas.append(r1)
    print("   OK:", r1.describir())
except SoftwareFJError as e:
    registrar_error(str(e))
    print("   ERROR:", e)


# ---------- Operación 8: reserva con 0 horas ----------
print("\n8. Crear reserva con 0 horas")
try:
    r2 = Reserva(c1, equipo, 0)
    reservas.append(r2)
except SoftwareFJError as e:
    registrar_error(str(e))
    print("   ERROR:", e)


# ---------- Operación 9: reserva con duración que no es número ----------
print("\n9. Crear reserva con duración 'dos' (encadenamiento de excepciones)")
try:
    r3 = Reserva(c1, asesoria, "dos")
    reservas.append(r3)
except SoftwareFJError as e:
    registrar_error(f"{e} | causa original: {e.__cause__}")
    print("   ERROR:", e)
    print("   Causa original:", e.__cause__)


# ---------- Operación 10: reservar un servicio no disponible ----------
print("\n10. Reservar un servicio que no está disponible")
try:
    asesoria.disponible = False            # la asesoría queda ocupada
    r4 = Reserva(c1, asesoria, 2)
    reservas.append(r4)
except SoftwareFJError as e:
    registrar_error(str(e))
    print("   ERROR:", e)
finally:
    asesoria.disponible = True             # se deja disponible de nuevo


# ---------- Operación 11: calcular costos (sobrecarga) ----------
print("\n11. Procesar la reserva y calcular costos de 3 formas")
try:
    print("   Costo normal:        $", r1.procesar())
    print("   Costo con IVA 19%:   $", r1.procesar(impuesto=0.19))
    print("   Costo con 10% desc.: $", r1.procesar(descuento=0.10))
except SoftwareFJError as e:
    registrar_error(str(e))
    print("   ERROR:", e)


# ---------- Operación 12: cancelar dos veces la misma reserva ----------
print("\n12. Cancelar una reserva dos veces")
try:
    r1.cancelar()
    print("   OK: primera cancelación ->", r1.describir())
    r1.cancelar()                          # esta segunda vez debe fallar
except SoftwareFJError as e:
    print("   ERROR:", e)


# ---------- Resumen final ----------
print("\n" + "=" * 60)
print(f" Clientes registrados: {len(clientes)}")
print(f" Servicios creados:    {len(servicios)}")
print(f" Reservas realizadas:  {len(reservas)}")
print(" Simulación terminada: el sistema siguió funcionando.")
print(" Revise el archivo eventos.log para ver los registros.")
print("=" * 60)
registrar_evento("----- Fin de la simulación -----")
