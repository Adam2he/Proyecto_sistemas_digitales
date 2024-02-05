from sense_hat import SenseHat
import time

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





