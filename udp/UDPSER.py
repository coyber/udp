#

import socket
import sys

def udp_server(host, port, filename):
    # 创建UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定socket到地址和端口
    server_socket.bind((host, port))
    print(f"UDP Server listening on {host}:{port}")

    try:
        with open(filename, 'wb') as file:
            while True:
                # 接收数据
                data, addr = server_socket.recvfrom(1024)
                if not data:
                    break
                file.write(data)
                print(f"Received {len(data)} bytes from {addr}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python UDPserver.py <host> <port> <filename>")
        sys.exit(1)

    HOST = sys.argv[1]  # 服务器地址
    PORT = int(sys.argv[2])  # 服务器端口
    FILENAME = sys.argv[3]  # 保存接收数据的文件名

    udp_server(HOST, PORT, FILENAME)