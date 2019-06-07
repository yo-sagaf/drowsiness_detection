import os
import cv2
from PIL import Image
import numpy as np
import pickle


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "Images")
recognizer = cv2.face.LBPHFaceRecognizer_create()

cascPath = "haarcascade_frontalface_alt2.xml"
print(cascPath)
faceCascade = cv2.CascadeClassifier(cascPath)

current_id = 0
labels_ids = {}
y_labels = []
x_train = []

for root, dirs, files in os.walk(image_dir) :
	for file in files:
		
			path=os.path.join(root,file)
			label=os.path.basename(root).replace(" ","-").lower()
			
			if not label in labels_ids:
				labels_ids[label] = current_id
				current_id += 1
			id_ = labels_ids[label]
			
			pil_image = Image.open(path).convert("L")
			size=(550,550)
			final_image = pil_image.resize(size,Image.ANTIALIAS)
			image_array = np.array(final_image,"uint8")
			faces = faceCascade.detectMultiScale(image_array,scaleFactor=1.5,minNeighbors=5)
			print(label,path)
			#print(id_)
			for (x,y,w,h) in faces:
				
				roi = image_array[y:y+h,x:x+w]
				x_train.append(roi)
				y_labels.append(id_)
				
print(x_train)
print(y_labels)


with open("labels.pickle",'wb')	as f:
	pickle.dump(labels_ids,f)
	
recognizer.train(x_train,np.array(y_labels))
recognizer.save("face-trainner.yml")	
				
	



