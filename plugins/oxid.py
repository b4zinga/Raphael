# author: myc

import socket


def run(host, **kwargs):
    port = kwargs.get('port') or 135
    timeout = 2
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.settimeout(timeout)
        sock.connect((host, port))
        buffer_1 = b"\x05\x00\x0b\x03\x10\x00\x00\x00\x48\x00\x00\x00\x01\x00\x00\x00\xb8\x10\xb8\x10\x00\x00\x00\x00" \
                   b"\x01\x00\x00\x00\x00\x00\x01\x00\xc4\xfe\xfc\x99\x60\x52\x1b\x10\xbb\xcb\x00\xaa\x00\x21\x34\x7a" \
                   b"\x00\x00\x00\x00\x04\x5d\x88\x8a\xeb\x1c\xc9\x11\x9f\xe8\x08\x00\x2b\x10\x48\x60\x02\x00\x00\x00"
        buffer_2 = b"\x05\x00\x00\x03\x10\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00"
        sock.send(buffer_1)
        packet = sock.recv(1024)
        sock.send(buffer_2)
        packet = sock.recv(4096)
        packet_v2 = packet[42:]
        packet_v2_end = packet_v2.find(b"\x09\x00\xff\xff\x00\x00")
        packet_v2 = packet_v2[:packet_v2_end]
        hostname_list = packet_v2.split(b"\x00\x00")
        result = {host: []}
        for h in hostname_list:
            h = h.replace(b'\x07\x00', b'')
            h = h.replace(b'\x00', b'')
            if h == b'':
                continue
            result[host].append(h.decode())
        return result
    except Exception as e:
        raise e
    finally:
        sock.close()
