# author: myc

import socket


def run(host, **kwargs):
    port = kwargs.get('port') or 11211
    payload = "stats\r\n".encode()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.settimeout(0.5)
        sock.connect((host, port))
        sock.send(payload)
        data = sock.recv(1024)
        if b"STAT pid" in data:
            return True
    except Exception as e:
        raise e
    finally:
        sock.close()
