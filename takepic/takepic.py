import cv2
import time
import os


# 保存先フォルダを指定
save_path = 'picture/picture'  



# Webカメラからのキャプチャを開始
cap = cv2.VideoCapture(0)  # 0はカメラのデバイス番号（通常はデフォルトのカメラ）

# # キャプチャが正常に開始されたか確認
# if not cap.isOpened():
#     print("カメラが見つかりません")
#     exit()

while True:
    ret, frame = cap.read()  # フレームをキャプチャ

    if not ret:
        print("フレームを取得できませんでした")
        break

    # # ウィンドウにライブ映像を表示
    # cv2.imshow('Live Feed', frame)

    # # 'q' キーを押したら終了
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

 
    timestamp = int(time.time())

    # 10秒ごとに画像を保存
    if timestamp % 5 == 0:
        # 画像を保存
        image_name = f"{save_path}/image_{timestamp}.jpg"
        cv2.imwrite(image_name, frame)
        print(f"Captured image_{timestamp}.jpg")


cap.release()
# cv2.destroyAllWindows()
