#

import socket
import sys

def udp_client(server_host, server_port, filename):
    # 创建UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    with open(filename, 'rb') as file:
        while True:
            # 读取文件数据
            data = file.read(1024)
            if not data:
                break
            # 发送数据
            client_socket.sendto(data, (server_host, server_port))
            print(f"Sent {len(data)} bytes to {server_host}:{server_port}")

    client_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python UDPclient.py <server_host> <server_port> <filename>")
        sys.exit(1)

    SERVER_HOST = sys.argv[1]  # 服务器地址
    SERVER_PORT = int(sys.argv[2])  # 服务器端口
    FILENAME = sys.argv[3]  # 要发送的文件名

    udp_client(SERVER_HOST, SERVER_PORT, FILENAME)