import cv2
import numpy as np
 
# 透過の画像を読み込む
foreground = cv2.imread('fukuchan.png', -1)  # 透過の画像ファイル名を指定

# 透過情報を示すアルファチャンネルを持つ場合のマスクを作成
mask = foreground[:, :, 3]

# RGBチャンネルのみを取得
foreground = foreground[:, :, 0:3]

# 背景画像を読み込む
background = cv2.imread('picture/picture/haikei1.jpg')  # 背景画像ファイル名を指定
background = cv2.resize(background, (foreground.shape[1], foreground.shape[0]))  # 透過画像と同じサイズにリサイズ

# 透過の画像と背景画像の型を同じにする
foreground = foreground.astype(float)
background = background.astype(float)

# マスクを3チャンネルに変換
mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

# 透過情報を持つ画像を背景画像に合成
result = cv2.addWeighted(background, 1.0, foreground, 1.0, 0)

# マスクを使って透過を適用
result = cv2.multiply(result, (mask / 255.0))

# 合成結果を表示
cv2.imshow('Result', result.astype(np.uint8))  # 最終的な画像をuint8型に変換して表示
cv2.waitKey(0)
cv2.destroyAllWindows()
