import numpy as np
import os
from keras import models
from keras.preprocessing import image
import dlib
from imutils.face_utils import FaceAligner
from imutils.face_utils import rect_to_bb
import imutils
import time
import cv2

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

model = models.load_model('./model/emo0809_epo50lr6.h5')
predictor = dlib.shape_predictor('./landmark/shape_predictor_68_face_landmarks.dat')
fa = FaceAligner(predictor, desiredFaceWidth=224)
facecasc = cv2.CascadeClassifier('./harrcascade/haarcascade_frontalface_alt.xml')
static_alignment_path = os.path.join(os.getcwd(), 'static', 'alignment')

class Emotion():
    def __init__(self, img_path):
        self.emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised", 7: "Worry"}
        self.fear_threshold = 0.0002
        self.worry_threshold = 0.065
        self.img_path = img_path

    def predict(self):
        result = 'none'
        confidence = 0.00
        print("image path: "+ self.img_path)

        img = cv2.imread(self.img_path)
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        faces = facecasc.detectMultiScale(rgb, scaleFactor=1.05 , minNeighbors=5)
        print('number of detected face : {0}'.format(len(faces)))
        # no face
        if len(faces) < 1:
            #print("no face")
            resp = dict()
            resp["isRecognized"] = False
            resp["numOfFaces"] = 0
            resp["emotion"] = result
            resp["confidence"] = confidence
            resp["info"] = "no face detected"
            return resp
        # too many faces
        elif len(faces) > 1:
            #print("too more faces")
            resp = dict()
            resp["isRecognized"] = True
            resp["numOfFaces"] = len(faces)
            resp["emotion"] = result
            resp["confidence"] = confidence
            resp["info"] = "too mamy faces detected"
            return resp
        # only one face
        else:
            #print("got one face")
            for (x, y, w, h) in faces:
                # crop face
                rect = dlib.rectangle(x,y,x+w+10,y+h+15)
                # alignment
                faceAligned = fa.align(rgb, rgb, rect)
                # resize
                cropped_img = cv2.resize(faceAligned, (224, 224))
                # bgr2rgb(opencv)
                cropped_img = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2RGB)
                #save alignment
                file_name = os.path.basename(self.img_path)
                cv2.imwrite('{0}/{1}'.format(static_alignment_path, file_name), cropped_img)

                # img to tensor & predict
                img_tensor = image.img_to_array(cropped_img)
                img_tensor = np.expand_dims(img_tensor, axis=0)
                img_tensor /= 255.
                prediction = model.predict(img_tensor)
                maxindex = int(np.argmax(prediction))

                pred = model.predict_proba(img_tensor)
                print('angry:{0:.15f}, disguested:{1:.15f}, fearful:{2:.15f}, \nhappy:{3:.15f}, neutral:{4:.15f}, sad:{5:.15f}, \nsurprised:{6:.15f}'.format(pred[0][0], 
                        pred[0][1], pred[0][2], pred[0][3], pred[0][4], pred[0][5], pred[0][6]))
                print('worry:{0:.15f}'.format(pred[0][7]))
                #pred proba
                print('Predict: {0}, Confidence: {1}'.format(str(self.emotion_dict[maxindex]), np.max(pred[0])))
                # result & confidence
                result = str(self.emotion_dict[maxindex])
                confidence = round(np.max(pred[0]) * 100, 2) 
                
                # enhance worry 
                if float(pred[0][7]) >= self.worry_threshold or maxindex==2 and float(pred[0][7]) >= 0.0050:
                    print("is worry")
                    result = str(self.emotion_dict[7])
                    confidence = round(float(pred[0][7]) * 150, 2)
                    if float(confidence) >= 100.00:
                        confidence = 100.00

                resp = dict()
                resp["isRecognized"] = True
                resp["numOfFaces"] = len(faces)
                resp["emotion"] = result
                resp["confidence"] = confidence
                resp["info"] = "ok"
                return resp

if __name__ == "__main__":
   
    img = Emotion("/Users/mingshenglyu/Desktop/jaffe2/happy/MK.HA3.118.png")
    img.predict()