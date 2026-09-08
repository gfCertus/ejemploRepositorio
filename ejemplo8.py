# Modificar para que en cada iteracion inserte una nueva linea en un archivo.
import time
import keyboard

while True:
    if keyboard.is_pressed("esc"):
        print("\nTecla ESC detectada. Bucle detenido.")
        break

    # Lógica de tu programa
    print("Procesando...", end="\r")
    time.sleep(0.1)