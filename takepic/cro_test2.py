import cv2
import numpy as np

# グリーンバックの動画を読み込む
green_screen_video = cv2.VideoCapture('dougasozai2.mp4')  # グリーンバックの動画ファイル名を指定

# 新しい背景動画を読み込む
background_video = cv2.VideoCapture('dougasozai1.mp4')  # 背景動画ファイル名を指定

while True:
    ret1, green_frame = green_screen_video.read()
    ret2, background_frame = background_video.read()

    # 両方の動画からフレームが読み込めなくなったら終了
    if not ret1 or not ret2:
        break

    # グリーンバックのフレームをHSVに変換
    hsv = cv2.cvtColor(green_frame, cv2.COLOR_BGR2HSV)
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    mask_inv = cv2.bitwise_not(mask)

    # 背景フレームをグリーンバックのフレームと同じサイズにリサイズ
    background_frame = cv2.resize(background_frame, (green_frame.shape[1], green_frame.shape[0]))

    # グリーンバックの部分を透明にする
    green_frame = cv2.bitwise_and(green_frame, green_frame, mask=mask_inv)

    # 背景とグリーンバックを合成
    result = cv2.add(green_frame, background_frame)

    # 合成結果を表示
    cv2.imshow('Result', result)
    
    # 'q' キーが押されたら終了
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# ビデオキャプチャの後始末とウィンドウのクローズ
green_screen_video.release()
background_video.release()
cv2.destroyAllWindows()
