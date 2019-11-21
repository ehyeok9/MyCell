import cv2
from os import listdir
from os.path import isfile, join
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

class Face_Recognition:

    def __init__(self):
        self.data_path = ['userFaces/', 'othersFaces/']
        self.userFiles = [f for f in listdir(self.data_path[0]) if isfile(join(self.data_path[0],f))]
        self.otherFiles = [f for f in listdir(self.data_path[1]) if isfile(join(self.data_path[1], f))]

        self.Training_Data, self.Labels = [], []

        for i, files in enumerate(self.userFiles):
            image_path = self.data_path[0] + self.userFiles[i]
            images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            self.Training_Data.append(np.asarray(images, dtype=np.uint8))
            self.Labels.append(i)

        self.Labels = np.asarray(self.Labels, dtype=np.int32)

        self.model = cv2.face.LBPHFaceRecognizer_create()

        self.model.train(np.asarray(self.Training_Data), np.asarray(self.Labels))

        print("Model Training Complete!!!!!")

        self.face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    def face_detector(self, img, size = 0.5):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.face_classifier.detectMultiScale(gray,1.3,5)

        if faces is():
            return img,[]

        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,255),2)
            roi = img[y:y+h, x:x+w]
            roi = cv2.resize(roi, (200,200))

        return img, roi

    def compare_face(self):
        conf_dict = {}

        for i, j in enumerate(self.otherFiles):
            image_path = self.data_path[1] + self.otherFiles[i]
            frame = cv2.imread(image_path, cv2.IMREAD_COLOR)
            image, face = self.face_detector(frame)
            name = j.split('.')[0]

            try:
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                result = self.model.predict(face)

                if result[1] < 500:
                    confidence = int(100 * (1 - (result[1]) / 300))
                    display_string = name + " " + str(confidence) + '% Confidence it is user'
                    print(display_string)
                    conf_dict[name] = confidence

            except:
                print("Face Not Found")

        return conf_dict

    def draw_graph(self, table, obj):
        y1_value = list(table.values())
        x_name = list(table.keys())
        n_groups = len(x_name)
        index = np.arange(n_groups)

        matplotlib.rc('font', family='NanumGothic')

        obj.bar(index, y1_value, tick_label=x_name, align='center')

        plt.xlabel('Name')
        plt.ylabel('Confidence (%)')
        plt.title('Chart')
        plt.xlim(-1, n_groups)
        plt.ylim(min(y1_value) - 1, max(y1_value) + 1)


if __name__ == "__main__":
    f = Face_Recognition()
    dic = f.compare_face()
    f.draw_graph(dic)


"""
cap = cv2.VideoCapture(0)
while True:

    ret, frame = cap.read()

    image, face = face_detector(frame)

    try:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        result = model.predict(face)

        if result[1] < 500:
            confidence = int(100*(1-(result[1])/300))
            display_string = str(confidence)+'% Confidence it is user'
        cv2.putText(image,display_string,(100,120), cv2.FONT_HERSHEY_COMPLEX,1,(250,120,255),2)


        if confidence > 75:
            cv2.putText(image, "Unlocked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Face Cropper', image)

        else:
            cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow('Face Cropper', image)


    except:
        cv2.putText(image, "Face Not Found", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow('Face Cropper', image)
        pass

    if cv2.waitKey(1)==13:
        break


cap.release()
cv2.destroyAllWindows()
"""
