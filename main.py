from sense_hat import SenseHat
import time
from inicializar import *
from cambiar_pixel import *
from enviar_datos import *
from camara import *

inicializa_perfil() #Crea el perfil de VPN


sense=SenseHat()

X= [255, 0, 0]  # Rojo
Y= [0,255,0]  #Verde
Z= [0,0,0] #Negro
O = [255, 255, 255]  # Blanco

INCORRECTO = [
  O, O, O, O, O, O, O, O,
  O, X, O, O, O, O, X, O,
  O, O, X, O, O, X, O, O,
  O, O, O, X, X, O, O, O,
  O, O, O, X, X, O, O, O,
  O, O, X, O, O, X, O, O,
  O, X, O, O, O, O, X, O,
  O, O, O, O, O, O, O, O,
  ]

CORRECTO = [
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, Y, O,
  O, O, O, O, O, Y, O, O,
  O, O, O, O, O, Y, O, O,
  O, O, O, O, Y, O, O, O,
  O, Y, O, O, Y, O, O, O,
  O, Y, O, Y, O, O, O, O,
  O, O, Y, O, O, O, O, O,
  ]

ACTIVADO = [
  O, O, Z, Z, Z, Z, O, O,
  O, O, Z, Z, Z, Z, O, O,
  O, O, O, O, O, O, O, O,
  Z, Z, Z, Z, Z, Z, Z, Z,
  O, O, O, O, O, O, O, O,
  O, Z, O, Z, Z, O, Z, O,
  Z, O, Z, O, O, Z, O, Z,
  O, Z, O, O, O, O, Z, O,
  ]

X=0
Y=0
DIR=1 
color=[0,0,255]
sense.clear()

####################################################
#COMIENZA EL PROGRAMA
    


espera=True
reconocido=False
while espera:
    events = sense.stick.get_events()
    for event in events:
        if event.direction  == "middle": #Programa empieza al pulsar el joystick
            espera=False
while not reconocido: #Espero a encontrar la cara
    sense.set_pixel(X,Y,color)
    X,Y,DIR,color=cambia_pixel(X,Y,DIR,color)
    #Función de la cámara devuelve True si encuentra a la persona
    reconocido=camara()
    sense.set_pixels(INCORRECTO)
sense.set_pixels(CORRECTO)
envia_datos() #Envío los datos por Telegram
              
                    
           
                
    
    




