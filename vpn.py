import os
import time
import random
import subprocess

#Crear el cliente con el nombre que quieres.
#Cuando lo creas, se crea un archivo llamado nombre.ovpn que tiene todos los datos
#Antes de poder leerlo, hay que darle permisos con estos comandos:
# super su
# chmod 777 /root/nombre.ovpn
#Y ya se puede leer desde python



x=input("¿Quien eres?")  #Esto sería la detección facial
file=open("/root/"+x+".ovpn","r")  #Abrir el archivo de la persona
y=file.read()  #Leer el archivo
file=open("Datos_de_"+x+".txt","w")  #Crear un nuevo archivo con los datos leidos
file.write(y)  #Escribir en el nuevo archivo
file.close()



