import cv2
from deepface import DeepFace

def get_dominant_emotion(dictionary_list):
    dominant_emotion = dictionary_list[0]['dominant_emotion']
    return dominant_emotion

def obejct_detection():
    cap=cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    smile_casacde = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
    
    while True:
        ret, frame = cap.read()
        try:
            emotion=DeepFace.analyze(frame, actions= ['emotion'])
        except:
            print("No face detected.")
        to_gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(to_gray,1.3,5)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
            try:
                dominant=get_dominant_emotion(emotion)
                cv2.putText(frame, dominant, (x+10,y+50), cv2.FONT_HERSHEY_COMPLEX, 1 , (0,255,0),2)
            except:
                print("Face undetected.")
            roi_gray=to_gray[y:y+w, x:x+w]
            roi_color=frame[y:y+h, x:x+w]
            smiles=smile_casacde.detectMultiScale(roi_gray,1.3,7)
            for (x_s,y_s,w_s,h_s) in smiles:
                cv2.rectangle(roi_color,(x_s, y_s),(x_s+w_s,y_s+h_s),(255,0,0),2)
                cv2.putText(roi_color,"Smile", (x_s+10,y_s+50), cv2.FONT_HERSHEY_COMPLEX, 0.5 , (0,255,0),2)
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 5)
                cv2.putText(roi_color,"Eye", (ex+10,ey+30), cv2.FONT_HERSHEY_COMPLEX, 0.5 , (0,255,0),2)
        cv2.imshow('frame', frame)
                
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

obejct_detection()