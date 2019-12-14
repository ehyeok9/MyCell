import cv2
from os import listdir
from os.path import isfile, join
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os
lst = ["/home/user/", "/home/ehyeok9/github/"]
directory = lst[0]
folder_path = directory + "Software-Project-II---AD-project/"
data_path = [folder_path + 'Face_Recognition/userFaces/', folder_path + 'Face_Recognition/othersFaces/', folder_path + 'Face_Recognition/']

class FaceRecognition:

    def __init__(self, username, usergender):
        self.username = username
        self.usergender = usergender
        self.isMan = True if usergender == "man" else False
        self.face_classifier = cv2.CascadeClassifier(data_path[2] + 'haarcascade_frontalface_default.xml')
        self.userFolderPath = data_path[0] + username + '/'
        self.userFiles = [f for f in listdir(self.userFolderPath) if isfile(join(self.userFolderPath, f))]
        self.gender_path = data_path[1] + ("menFaces/" if self.isMan else "womenFaces/")
        self.otherFiles = [f for f in listdir(self.gender_path) if isfile(join(self.gender_path, f))]

        self.Training_Data, self.Labels = [], []

        for i, files in enumerate(self.userFiles):
            image_path = self.userFolderPath + self.userFiles[i]
            images = cv2.imread(image_path, cv2.IMREAD_COLOR)
            images = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
            self.Training_Data.append(np.asarray(images, dtype=np.uint8))
            self.Labels.append(i)

        self.Labels = np.asarray(self.Labels, dtype=np.int32)

        self.model = cv2.face.LBPHFaceRecognizer_create()

        self.model.train(np.asarray(self.Training_Data), np.asarray(self.Labels))

        print("Model Training Complete!!!!!")

    def update_data(self):
        self.userFiles = [f for f in listdir(data_path[0]) if isfile(join(data_path[0], f))]
        self.otherFiles = [f for f in listdir(data_path[1]) if isfile(join(data_path[1], f))]

    def face_detector(self, img):

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
            image_path = self.gender_path + self.otherFiles[i]
            frame = cv2.imread(image_path, cv2.IMREAD_COLOR)
            image, face = self.face_detector(frame)
            name = j.split('.')[0]

            try:
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                result = self.model.predict(face)

                if result[1] < 500:
                    confidence = int(100 * (1 - (result[1]) / 300))
                    display_string = name + " " + str(confidence) + '% Confidence it is user'
                    # print(display_string)
                    conf_dict[name] = confidence
            except:
                print("Face Not Found")

        return conf_dict

    def draw_graph(self, table):
        y1_value = list(table.values())
        x_name = list(table.keys())
        n_groups = len(x_name)
        index = np.arange(n_groups)

        matplotlib.rc('font', family='NanumGothic')

        plt.bar(index, y1_value, tick_label=x_name, align='center')

        plt.xlabel('Name')
        plt.ylabel('Confidence (%)')
        plt.title('Chart')
        plt.xlim(-1, n_groups)
        plt.ylim(min(y1_value) - 1, max(y1_value) + 1)

    def make_file(self, filepath, revised_filepath):
        image = cv2.imread(filepath, cv2.IMREAD_COLOR)
        _, face = self.face_detector(image)
        cv2.imwrite(revised_filepath, face)


class FaceCapture:

    count = 0

    @staticmethod
    def face_extractor(img):
        face_classifier = cv2.CascadeClassifier(data_path[2] + 'haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
        cropped_face = None

        if faces is():
            return None

        for (x, y, w, h) in faces:
            cropped_face = img[y:y+h, x:x+w]

        return cropped_face

    @staticmethod
    def capture_face(username = "Kevin"):

        cap = cv2.VideoCapture(0)
        count = 0
        os.system("mkdir {}".format(data_path[0] + username + '/'))

        while True:
            ret, frame = cap.read()
            if FaceCapture.face_extractor(frame) is not None:
                count += 1
                face = cv2.resize(FaceCapture.face_extractor(frame), (200, 200))

                file_name_path = data_path[0] + '/' + username + '/user' + str(count) + '.jpg'
                cv2.imwrite(file_name_path, face)

                cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                cv2.imshow('Face Cropper', face)
            else:
                print("Face not Found")
                pass

            if cv2.waitKey(1) == 13 or count == 100:
                break

        cap.release()
        cv2.destroyAllWindows()
        print('Colleting Samples Complete!!!')





if __name__ == "__main__":
    FaceCapture.capture_face()

    f = FaceRecognition()
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
