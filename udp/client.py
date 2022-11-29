import socket

udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input('>> ').strip()
    if msg:
        udp_client.sendto(msg.encode('utf-8'), ('127.0.0.1', 9000))
