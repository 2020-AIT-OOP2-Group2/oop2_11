# -*- coding: utf-8 -*-

import cv2

class FaceRecognition():
    def rectangle_face(self,img_path):
        #HAAR分類器の顔検出用の特徴量
        cascade_path = "haarcascades/haarcascade_frontalface_alt.xml"

        image_path = img_path

        color = (255, 255, 255) #白
        #color = (0, 0, 0) #黒

        #ファイル読み込み
        image = cv2.imread(image_path)
        #グレースケール変換
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        #カスケード分類器の特徴量を取得する
        cascade = cv2.CascadeClassifier(cascade_path)

        #物体認識（顔認識）の実行
        facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))

        #print("face rectangle")
        #print(facerect)

        if len(facerect) > 0:
            #検出した顔を囲む矩形の作成
            for rect in facerect:
                cv2.rectangle(image, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2)

            #認識結果の保存
            cv2.imwrite("output_faceRecognition/detected.png", image)
    


