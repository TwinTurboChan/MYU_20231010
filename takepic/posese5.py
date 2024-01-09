import cv2
import mediapipe as mp
import time
import os
import glob

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

folder_path = 'picture\picture'  # 画像ファイルの拡張子に合わせて適宜変更してください

while True:
    list_of_files = glob.glob(folder_path)
    if list_of_files:
        latest_file = max(list_of_files, key=os.path.getctime)

        image = cv2.imread(latest_file)
        if image is not None:
            with mp_pose.Pose(
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5) as pose:
                
                image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                results = pose.process(image_rgb)

                # 以下、姿勢推定と画像へのラベル描画の処理
                
                cv2.imshow('Pose Estimation', image)
                cv2.waitKey(5000)  # 5秒間表示する
                
        else:
            print("画像の読み込みに失敗しました。")
    else:
        print("ファイルが見つかりませんでした")

    time.sleep(5)  # 5秒待機してから次のループへ
