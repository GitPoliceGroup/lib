import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  #

from deepface import DeepFace
import cv2
import time

# Add tf-keras THEN deepface

# Must make sure that tensorflow is installed

class HappinessEnforcer:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        print("Initialized face classifier...")
        
    def emotion_analysis(self):
        # Load the image
        video = cv2.VideoCapture(0)

        if (not video.isOpened()):
            print("Could not open video device")

        happy = False
        while video.isOpened():
            _, frame = video.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face = self.face_cascade.detectMultiScale(gray, 1.1, 5)

            for x, y, w, h in face:
                image = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                try:
                    analyze = DeepFace.analyze(frame, actions=['emotion'])[0]
                    # [{'emotion': {'angry': np.float32(1.7090334), 'disgust': np.float32(2.2264721e-06), 'fear': np.float32(11.091586), 'happy': np.float32(0.033611566), 'sad': np.float32(12.082921), 'surprise': np.float32(0.01599837), 'neutral': np.float32(75.06685)}, 'dominant_emotion': 'neutral', 'region': {'x': 857, 'y': 544, 'w': 474, 'h': 474, 'left_eye': (1199, 731), 'right_eye': (1005, 738)}, 'face_confidence': np.float64(0.93)}]
                    cv2.putText(image, analyze['dominant_emotion'], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
                    # print(analyze['dominant_emotion'])
                    if analyze['dominant_emotion'] == 'happy':
                        happy = True
                        break
                except:
                    # print("No Face")
                    pass

            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break

            if happy:
                break

        video.release()
        cv2.destroyAllWindows()
        return happy

