# importer tout les packages requis
from imutils.video import VideoStream
from imutils.video import FPS
import imutils
import numpy as np
import os
import pickle
import time
import cv2
import sys
import mysql.connector
from datetime import datetime
#from pushbullet import Pushbullet


recognizer = cv2.face.LBPHFaceRecognizer_create()
#recognizer.read("./recognizers/face-trainner.yml")
#pb = Pushbullet(o.CyXbYB9ZRul1yPTwP3bGlAR3QLR8kwY8)


recognizer.read("face-trainner.yml")

labels = {"person_name": 1}

with open("labels.pickle", 'rb') as f:
	og_labels = pickle.load(f)
	labels = {v:k for k,v in og_labels.items()}


#cascPath = sys.argv[1]
cascPath = "haarcascade_frontalface_alt.xml"
print(cascPath)
faceCascade = cv2.CascadeClassifier(cascPath)

# initialiser la caméra du pi, attendre 2s pour la mise au point ,
# initialiser le compteur FPS
print("...demarrage de la Picamera...")
vs = VideoStream(usePiCamera=True, resolution=(800, 600)).start()
time.sleep(2.0)
fps = FPS().start()

# boucle principale du flux vidéo
while True:
	# récupération du flux vidéo, redimension 
	# afin d'afficher au maximum 800 pixels 
	frame = vs.read()
	frame = imutils.resize(frame, width=800)
	
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,
		minSize=(30, 30),
		flags=cv2.CASCADE_SCALE_IMAGE
    )
   
	

    # Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]
		id_, conf = recognizer.predict(roi_gray)
		
		print(x,y,w,h)
	
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
		
		print(conf)
		if conf>=80 :#and conf<=85 
			
			#print(id_)
			#print(labels[id_])
			font  = cv2.FONT_HERSHEY_SIMPLEX
			name = labels[id_]
			color = (255, 255, 255)
			stroke = 2
			cv2.putText(frame, name, (x,y), font,1, color, stroke, cv2.LINE_AA)	
			
		color = (255,0,0)
		stroke = 2
		end_cord_x = x+w
		end_cord_y = y+h
		cv2.rectangle(frame,(x,y), (end_cord_x, end_cord_y), color, stroke)
		
		#push = pb.push_note("This is the title", "This is the body")
		
	# affichage du flux vidéo dans une fenètre 

	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	# la touche q permet d'interrompre la boucle principale
	if key == ord("q"):
		break

	# mise à jour du FPS 
	fps.update()

# insertion des donnees dans la base

mydb = mysql.connector.connect(
  host='localhost',
  user='setsisuser',
  passwd='setsis0809',
  database='SETSISBASE'
)

mycursor = mydb.cursor()
val=name
now = datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

#sql = "INSERT INTO EVENTS(Name,Date) VALUE( \" "+ val+" \", \" " +formatted_date+ " \", ")"
sql = "INSERT INTO EVENTS(Name,Date) VALUE( \" "+ val+" \", \" " +formatted_date+ " \" )"
print(sql)
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "record inserted.")


# arret du compteur et affichage des informations dans la console
fps.stop()
print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

cv2.destroyAllWindows()
vs.stop()
