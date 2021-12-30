# author: myc

import socket


def run(host, **kwargs):
    port = kwargs.get('port') or 2181
    payload = "envi".encode()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.settimeout(0.5)
        sock.connect((host, port))
        sock.send(payload)
        data = sock.recv(1024)
        if b"zookeeper.version" in data:
            return True
    except Exception as err:
        raise err
    finally:
        sock.close()
