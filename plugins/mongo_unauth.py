# author: myc

import socket


def run(host, **kwargs):
    port = kwargs.get('port') or 27017
    payload = b'C\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\xd4\x07\x00\x00\x00\x00\x00\x00admin.$cmd\x00\x00\x00' \
              b'\x00\x00\xff\xff\xff\xff\x1c\x00\x00\x00\x01listDatabases\x00\x00\x00\x00\x00\x00\x00\xf0?\x00'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.settimeout(0.5)
        sock.connect((host, port))
        sock.send(payload)
        data = sock.recv(1024)
        if b'databases' in data:
            return True
    except Exception as e:
        raise e
    finally:
        sock.close()
