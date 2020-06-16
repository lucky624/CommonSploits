import socket

READ_TIMEOUT = 5
APPEND_TIMEOUT = 0.05
BUFSIZE = 4096

flags = ['c6ebc83c-1e03-4669-a18d-6adb2a58b33b']

def recvall(sock):
    sock.settimeout(READ_TIMEOUT)
    chunks = [sock.recv(BUFSIZE)]

    sock.settimeout(APPEND_TIMEOUT)
    while True:
        try:
            chunk = sock.recv(BUFSIZE)
            if not chunk:
                break

            chunks.append(chunk)
        except socket.timeout:
            break

    sock.settimeout(READ_TIMEOUT)
    return b''.join(chunks)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('192.168.0.102', 1488))
    data = recvall(s).decode().strip()
    for flag in flags:
        s.sendall(flag.encode() + b'\n')
        data = recvall(s).decode().strip()
        print(data)
    s.close()
