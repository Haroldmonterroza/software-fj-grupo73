# ============================================================
# registro.py
# Responsable: César José Ledesma Frieri
# Configura el archivo de logs (eventos.log), donde se anotan
# todos los errores y eventos importantes con fecha y hora.
# ============================================================

import logging    # módulo de Python para llevar registros

# Se configura el archivo donde se guardan los registros
logging.basicConfig(
    filename="eventos.log",                                 # nombre del archivo
    level=logging.INFO,                                     # guarda desde INFO en adelante
    format="%(asctime)s - %(levelname)s - %(message)s",     # fecha - tipo - mensaje
    encoding="utf-8"                                        # para que salgan bien las tildes
)


# Función para anotar un evento normal (algo que salió bien)
def registrar_evento(mensaje):
    logging.info(mensaje)


# Función para anotar un error
def registrar_error(mensaje):
    logging.error(mensaje)
