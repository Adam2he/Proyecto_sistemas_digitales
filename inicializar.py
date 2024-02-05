import os
import subprocess

def inicializa_perfil():
    #Crea un perfil llamado datos, con contraseña datos y que puede usar
    #la VPN durante 1 día, después se borra.
    subprocess.run("pivpn ovpn add -n datos -p datos -d 1",shell=True)
    #Si ha pasado menos de 1 día se mantiene el perfil anterior
    #sin dar fallo en la ejecución







