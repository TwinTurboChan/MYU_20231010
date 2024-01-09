import os
import cv2
import numpy as np

def get_latest_image(folder_path):
    try:
        # フォルダ内の画像ファイルの一覧を取得
        image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        
        # フォルダ内の画像ファイルを最終更新日時でソートして、最新の画像ファイルを取得
        latest_image = max(image_files, key=os.path.getmtime)
        return latest_image
    except FileNotFoundError:
        print("フォルダが見つかりません")

def show_latest_image_cv2(folder_path):
    latest_image_path = get_latest_image(folder_path)
    if latest_image_path:
        try:
            img = cv2.imread(latest_image_path)
            cv2.imshow("Latest Image", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except FileNotFoundError:
            print("ファイルが見つかりません")

# 画像ファイルが保存されているフォルダのパスを指定して、その中で最新の画像を表示する
folder_path = "picture/picture"  # 画像ファイルが保存されているフォルダの実際のパスに置き換えてください

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

background = folder_path
background = cv2.resize(background, (w, h))  # グリーンバック画像と同じサイズにリサイズ

#  グリーン部分を透明にする
green_screen_img = cv2.bitwise_and(green_screen_img, green_screen_img, mask=mask_inv)

# 新しい背景画像とグリーンバック画像を合成
result = cv2.add(green_screen_img, background)

# 合成結果を表示
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()






