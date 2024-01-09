import cv2
import mediapipe as mp
from pythonosc import udp_client

# OSCサーバーのIPアドレスとポート番号を設定q
ip = '127.0.0.1'  # OSCサーバーのIPアドレス
port = 12345  # OSCサーバーのポート番号

# OSCクライアントを作成
client = udp_client.SimpleUDPClient(ip, port)


# Mediapipe設定
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

# 関節番号の定義（15: 左肩、12: 左肘）

joint0 = 0
joint9= 9
joint10= 10
joint11 = 11
joint12 = 12
joint13 = 13
joint14 = 14
joint15 = 15
joint16 = 16


# カメラ起動
cap = cv2.VideoCapture(0)  # カメラ番号を変更する場合は適宜変更してください

while cap.isOpened():
    success, image = cap.read()
    if not success:
        continue

    # Mediapipeで姿勢推定
    results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # 関節の高さを比較してOSCメッセージ送信
    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark
        if (landmarks[joint15].y < landmarks[joint11].y and landmarks[joint16].y > landmarks[joint12].y):
            address = '/example'  # OSCアドレス
            cv2.putText(image, "SABOTEN", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
            message = 10  # 送信するデータ（aキーなら42を送る）
            client.send_message(address, message)
            print(f"Sent OSC message to {ip}:{port} with address '{address}' and message '{message}'")

    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark
        if (landmarks[joint15].y > landmarks[joint11].y and landmarks[joint16].y < landmarks[joint12].y):
            address = '/example'  # OSCアドレスcv2.putText(image, "SABOTEN", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
            message = 20  # 送信するデータ（aキーなら42を送る）
            client.send_message(address, message)
            print(f"Sent OSC message to {ip}:{port} with address '{address}' and message '{message}'")

    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark
        if (landmarks[joint15].y < landmarks[joint0].y and landmarks[joint16].y < landmarks[joint0].y):
            address = '/example'  # OSCアドレス
            cv2.putText(image, "upper_ki", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
            message = 30  # 送信するデータ（aキーなら42を送る）
            client.send_message(address, message)
            print(f"Sent OSC message to {ip}:{port} with address '{address}' and message '{message}'")


    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark
        if (landmarks[joint13].y > landmarks[joint11].y and landmarks[joint14].y > landmarks[joint12].y and landmarks[joint15].y > landmarks[joint11].y and landmarks[joint16].y > landmarks[joint12].y):
            address = '/example'  # OSCアドレス
            cv2.putText(image, "downner_ki", (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
            message = 40  # 送信するデータ（aキーなら42を送る）
            client.send_message(address, message)
            print(f"Sent OSC message to {ip}:{port} with address '{address}' and message '{message}'")

    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark
        if (landmarks[joint13].y > landmarks[joint9].y and landmarks[joint11].y > landmarks[joint13].y and landmarks[joint14].y > landmarks[joint10].y and landmarks[joint12].y > landmarks[joint14].y):
            address = '/example'  # OSCアドレス
            cv2.putText(image, "jyuuji", (50, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
            message = 50  # 送信するデータ（aキーなら42を送る）
            client.send_message(address, message)
            print(f"Sent OSC message to {ip}:{port} with address '{address}' and message '{message}'")




    # 関節を描画
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # 画面に映像表示
    cv2.imshow('Mediapipe Pose Detection', image)

    # 'q'を押すと終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 後処理
cap.release()
cv2.destroyAllWindows()
pose.close()
