# author: myc

import socket


def run(host, **kwargs):
    port = kwargs.get('port') or 6379
    payload = '\x2a\x31\x0d\x0a\x24\x34\x0d\x0a\x69\x6e\x66\x6f\x0d\x0a'.encode()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.settimeout(0.5)
        sock.connect((host, port))
        sock.send(payload)
        data = sock.recv(1024)
        if b'redis_version' in data:
            return True
    except Exception as e:
        raise e
    finally:
        sock.close()
