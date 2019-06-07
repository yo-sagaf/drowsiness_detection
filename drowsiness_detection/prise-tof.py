# importer tout les packages requis
from imutils.video import VideoStream
from imutils.video import FPS
import imutils
import time
import cv2
import sys

#cascPath = sys.argv[1]
cascPath = "haarcascade_frontalface_alt.xml"
print(cascPath)
faceCascade = cv2.CascadeClassifier(cascPath)

# initialiser la caméra du pi, attendre 2s pour la mise au point ,
# initialiser le compteur FPS
print("...démarrage de la Picamera...")
vs = VideoStream(usePiCamera=True, resolution=(800, 600)).start()
time.sleep(2.0)
fps = FPS().start()
cptFaceDetect=0;
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
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]
		nameImage="./Images/nader/"+str(cptFaceDetect)+".png"
		
		cv2.imwrite(nameImage,	frame )
		cptFaceDetect+=1;
	
	# affichage du flux vidéo dans une fenètre 

	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	# la touche q permet d'interrompre la boucle principale
	if key == ord("q"):
		break

	# mise à jour du FPS 
	fps.update()

# arret du compteur et affichage des informations dans la console
fps.stop()
print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

cv2.destroyAllWindows()
vs.stop()
