import os
import cv2
import mediapipe as mp
import pygame
import time
import subprocess

from pythonosc import udp_client

# OSCサーバーのIPアドレスとポート番号を設定
ip = '127.0.0.1'  # OSCサーバーのIPアドレス
port = 12345  # OSCサーバーのポート番号

# OSCクライアントを作成
client = udp_client.SimpleUDPClient(ip, port)





mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# 画像が保存されているフォルダのパス
folder_path = 'picture/picture'






# 最後に追加された画像を取得する関数
def get_latest_image():
    list_of_files = os.listdir(folder_path)
    if not list_of_files:
        return None
    return max(list_of_files, key=lambda x: os.path.getctime(os.path.join(folder_path, x)))

# 最後に追加された画像を取得
image_name = get_latest_image()
if image_name:
    image_path = os.path.join(folder_path, image_name)

    # 姿勢推定の初期化
    with mp_pose.Pose(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as pose:

        # 画像の読み込み
        image = cv2.imread(image_path)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # 姿勢推定の実行
        results = pose.process(image_rgb)
        

        
       
        # 検出されたポーズの描画
        if results.pose_landmarks:
            # 各関節に番号を表示
            for idx, landmark in enumerate(results.pose_landmarks.landmark):
                h, w, c = image.shape
                cx, cy = int(landmark.x * w), int(landmark.y * h)
                cv2.putText(image, str(idx), (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
                
            mp_drawing.draw_landmarks(
                image,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 255), thickness=2, circle_radius=2))
            # 関節15が関節11よりも高く、または関節16が関節12よりも高い位置にある場合に"up"を表示
            joint_15 = results.pose_landmarks.landmark[15]
            joint_11 = results.pose_landmarks.landmark[11]
            joint_16 = results.pose_landmarks.landmark[16]
            joint_12 = results.pose_landmarks.landmark[12]
            joint_13 = results.pose_landmarks.landmark[13]
            joint_14 = results.pose_landmarks.landmark[14]
            joint_10 = results.pose_landmarks.landmark[10]
            joint_9 = results.pose_landmarks.landmark[9]
            joint_0 = results.pose_landmarks.landmark[0]

            
            if joint_15.y < joint_11.y and joint_16.y > joint_12.y:
                cv2.putText(image, "SABOTEN", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
                address = '/example'  # OSCアドレス
                message = 10  # 送信するデータ（aキーなら42を送る）
                client.send_message(address, message)
                print(f"Sent OSC message to {ip}:{port} with address '{address}' and message '{message}'")
                

            if joint_15.y > joint_11.y and joint_16.y < joint_12.y:
                cv2.putText(image, "SABOTEN", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
                address = '/example'  # OSCアドレス
            message = 20  # 送信するデータ（aキーなら42を送る）
            client.send_message(address, message)
            print(f"Sent OSC message to {ip}:{port} with address '{address}' and message '{message}'")
          

            if joint_15.y < joint_0.y and joint_16.y < joint_0.y:
                cv2.putText(image, "upper_ki", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
                address = '/example'  # OSCアドレス
            message = 30  # 送信するデータ（aキーなら42を送る）
            client.send_message(address, message)
            print(f"Sent OSC message to {ip}:{port} with address '{address}' and message '{message}'")


            if joint_13.y > joint_11.y and joint_14.y > joint_12.y and joint_15.y > joint_11.y and joint_16.y > joint_12.y:
                cv2.putText(image, "downner_ki", (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
                address = '/example'  # OSCアドレス
            message = 40  # 送信するデータ（aキーなら42を送る）
            client.send_message(address, message)
            print(f"Sent OSC message to {ip}:{port} with address '{address}' and message '{message}'")

            if joint_13.y > joint_9.y and joint_11.y > joint_13.y and joint_14.y > joint_10.y and joint_12.y > joint_14.y:
                cv2.putText(image, "jyuuji", (50, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
                address = '/example'  # OSCアドレス
            message = 50  # 送信するデータ（aキーなら42を送る）
            client.send_message(address, message)
            print(f"Sent OSC message to {ip}:{port} with address '{address}' and message '{message}'")


            





        # 結果の表示
     # ディスプレイの解像度を取得
        screen_width, screen_height = 1920, 1080  # 仮の解像度。ご自身のディスプレイの解像度に置き換えてください。

        # ウィンドウをフルスクリーンモードで表示
        cv2.namedWindow('FullScreen Window', cv2.WINDOW_NORMAL)
        cv2.setWindowProperty('FullScreen Window', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        # 画像のリサイズ
        image = cv2.resize(image, (screen_width, screen_height))  # 画面サイズにリサイズ.

        cv2.imshow('popopo-po.po-popo', image)

        cv2.waitKey(300)
        # cv2.destroyAllWindows()

        time.sleep(5)
    
else:
    print("フォルダに画像が見つかりませんでした。")
