from sense_hat import SenseHat
import time

sense=SenseHat()

X= [255, 0, 0]  # Red
Y= [0,255,0]  #Green
Z= [0,0,0] #Black 
O = [255, 255, 255]  # White

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

def cambia_pixel(X,Y,DIR,color
                 
                 ):
    if DIR==1: #Estando arriba hacia la derecha
        X+=1
        if X==7:
            DIR=2
    elif DIR==2: #Estando en la derecha hacia abajo
        Y+=1
        if Y==7:
            DIR=3
    elif DIR==3: #Estando abajo hacia la izquierda
        X-=1
        if X==0:
            DIR=4
    elif DIR==4: #Estando a la izquierda hacia arriba
        Y-=1
        if Y==0:
            DIR=1
            color[2]-=70
            if color[2]<20:
                color[2]=255        
    sense.set_pixel(X,Y,color)
    return X,Y,DIR,color
            
    


bucle=True
k=0
while bucle:
    #sense.set_pixels(INCORRECTO)
    events = sense.stick.get_events()
    for event in events:
        if event.direction  == "middle":
            while True:
                sense.set_pixel(X,Y,color)
                X,Y,DIR,color=cambia_pixel(X,Y,DIR,color)
                #Cosas de la cámara
                time.sleep(0.2) #Tiempo que tardaria la camara
                if k==30: #La camara ha detectado a alguien que no puede usar la VPN
                    sense.set_pixels(INCORRECTO)
                if k==50: #La camara ha detectado a alguien que puede usar la VPN
                    sense.clear()
                    sense.set_pixels(CORRECTO)
                    salir=False
                    k2=0
                    time.sleep(2) #Tiempo que tardaria la VPN en activarse
                    sense.set_pixels(ACTIVADO)
                    while salir==False:
                        #Cosas de la VPN
                        if k2==30:
                            salir=True
                            sense.clear()
                        time.sleep(0.2)
                        k2+=1
                        ##################
                        
                k+=1
                    
                ###################
                
    
    



