import subprocess

n = 2  # 実行したいスクリプト番号を設定

if n == 1:
    subprocess.run(['python', 'takepic2.py'])
elif n == 2:
    subprocess.run(['python', 'posese4.py'])
else:
    print("無効な番号です。")
