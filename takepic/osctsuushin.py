import argparse

from pythonosc import osc_message_builder
from pythonosc import udp_client

port_num = 8002

# セットアップ
parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="127.0.0.1", help="The ip of th OSC Server")
parser.add_argument("--port", type=int, default=port_num, help="The port the OSC server is listening on")
args = parser.parse_args()
client = udp_client.UDPClient(args.ip, args.port)

print("ip:127.0.0.1, port:" + str(port_num) + ", address:/filter")

def main():
  print("type int:")
  input_str = input()
  li = []
  msg = osc_message_builder.OscMessageBuilder(address="/filter")
  for i in range (10):
    li.append(int(input_str.count(str(i))))
    msg.add_arg(li[i])
  print(li)
  msg = msg.build()
  client.send(msg)

if __name__ == "__main__":
  while True:
    main()