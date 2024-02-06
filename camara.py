from picamera import PiCamera
import face_recognition




def camara():
    camera = PiCamera()
    camera.resolution = (640,480)
    camera.rotation = 180
    obama_image = face_recognition.load_image_file("/home/pi/obama.jpg") #Cargo la cara a reconocer
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
    known_face_encodings = [obama_face_encoding]
    camera.capture('/home/pi/imagen.jpg') #Hago la foto
    cara=face_recognition.load_image_file("/home/pi/imagen.jpg")
    cara_encoding = face_recognition.face_encodings(cara)[0] #Reconozco la cara de la foto
    matches = face_recognition.compare_faces(known_face_encodings, cara_encoding) #Comparo las caras
    if True in matches:
            return True #Las caras coinciden
    #Busco una parecida
    face_distances = face_recognition.face_distance(known_face_encodings, cara_encoding)
    best_match_index = np.argmin(face_distances)
    if matches[best_match_index]:
            return True #Las caras coinciden 
    return False #No he encontrado parecido







