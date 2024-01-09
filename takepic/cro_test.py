import cv2
import numpy as np

# グリーンバックの画像を読み込む
green_screen_img = cv2.imread('GB_test02.jpg')  # グリーンバックの画像ファイル名を指定

# HSV色空間に変換
hsv = cv2.cvtColor(green_screen_img, cv2.COLOR_BGR2HSV)

# 緑色のHSV範囲を定義
lower_green = np.array([40, 40, 40])
upper_green = np.array([80, 255, 255])

# HSVから緑色に該当する部分をマスク
mask = cv2.inRange(hsv, lower_green, upper_green)

# マスクの反転
mask_inv = cv2.bitwise_not(mask)

# 画像のサイズを取得
h, w = green_screen_img.shape[:2]

# 新しい背景画像を読み込む
background = cv2.imread('picture/picture/haikei1.jpg')  # 背景画像ファイル名を指定
background = cv2.resize(background, (w, h))  # グリーンバック画像と同じサイズにリサイズ

# グリーン部分を透明にする
green_screen_img = cv2.bitwise_and(green_screen_img, green_screen_img, mask=mask_inv)

# 新しい背景画像とグリーンバック画像を合成
result = cv2.add(green_screen_img, background)

# 合成結果を表示
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
