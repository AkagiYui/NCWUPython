import socket

udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_client.bind(('127.0.0.1', 9000))

while True:
    msg, addr = udp_client.recvfrom(1024)
    print(f'收到消息：{msg.decode("utf-8")}', addr)
