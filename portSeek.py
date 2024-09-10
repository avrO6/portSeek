import socket
import threading

# Códigos ANSI para colores
ROJO = "\033[31m"
VERDE = "\033[32m"
AZUL = "\033[34m"
AMARILLO = "\033[33m"
RESET = "\033[0m"


puertos = []

def escanear_puertos(ip, puerto):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    
    res = sock.connect_ex((ip, puerto))
    
    if res == 0:
        print(VERDE + "[+] " + RESET + str(puerto))
        puertos.append(puerto)
        sock.close

def main():
    
    ip = input("Indica la IP que quieres escanear: ")
    
    # Creamos una lista para almacenar los hilos
    hilos = []
    
    for puerto in range (1,65535):
        # Creamos un hilo para cada puerto y lo agregamos a la lista
        hilo = threading.Thread(target=escanear_puertos, args=(ip, puerto))
        hilos.append(hilo)
        hilo.start()
        
    # Esperamos a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()
    
    print(puertos)
        
        
    
if __name__ == "__main__":
    main()