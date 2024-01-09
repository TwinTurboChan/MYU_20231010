from pythonosc import udp_client
import msvcrt  # Windowsでキー入力を受け付けるためのモジュール（他のOSでは異なる）

# OSCサーバーのIPアドレスとポート番号を設定
ip = '127.0.0.1'  # OSCサーバーのIPアドレス
port = 12345  # OSCサーバーのポート番号

# OSCクライアントを作成
client = udp_client.SimpleUDPClient(ip, port)

while True:
    if msvcrt.kbhit():
        key = msvcrt.getch().decode()  # キー入力を取得（Windows用）

        # OSCメッセージを送信
        if key == 'a':
            address = '/example'  # OSCアドレス
            message = 42  # 送信するデータ（aキーなら42を送る）
            client.send_message(address, message)
            print(f"Sent OSC message to {ip}:{port} with address '{address}' and message '{message}'")
        elif key == 'b':
            address = '/example'  # OSCアドレス
            message = 40  # 送信するデータ（bキーなら40を送る）
            client.send_message(address, message)
            print(f"Sent OSC message to {ip}:{port} with address '{address}' and message '{message}'")
