import os
import cv2
import mediapipe as mp
import time

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# 画像が保存されているフォルダのパス
folder_path = 'picture/picture'

# 最新の画像を取得する関数
def get_latest_image():
    list_of_files = os.listdir(folder_path)
    latest_file = max(list_of_files, key=os.path.getctime)
    return os.path.join(folder_path, latest_file)

# 姿勢推定の初期化
with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:

    # 最新の画像を取得
    image_path = get_latest_image()

    # 画像の読み込み
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 姿勢推定の実行
    results = pose.process(image_rgb)

    # 検出されたポーズの描画
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 255), thickness=2, circle_radius=2))

    # 結果の表示（5秒間）
    cv2.imshow('Pose Estimation', image)
    cv2.waitKey(5000)

    cv2.destroyAllWindows()
