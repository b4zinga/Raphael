# author: myc

import socket
from queue import Queue

from lib.threads import run_threads

DEFAULT = [20, 21, 22, 23, 25, 53, 69, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 110, 111, 135, 137, 139, 143, 161, 389, 443, 445, 512, 513, 514, 873, 1080, 1194, 1352, 1433, 1521, 1723, 2181, 3306, 3389, 3690, 5000, 5432, 5900, 5901, 5984, 6379, 6380, 7001, 7002, 7778, 8000, 8001, 8002, 8003, 8004, 8005, 8006, 8007, 8008, 8009, 8010, 8069, 8080, 8081, 8082, 8083, 8084, 8085, 8086, 8087, 8088, 8089, 8090, 8443, 8888, 9000, 9043, 9080, 9081, 9090, 9200, 9300, 11211, 27017, 27018, 50000, 50060, 50070]

task_queue = Queue()
result_queue = Queue()


def build_task(host, ports):
    for port in ports:
        task_queue.put((host, port))


def task():
    while not task_queue.empty():
        host, port = task_queue.get()
        if connect(host, port):
            result_queue.put(port)


def connect(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.settimeout(0.5)
        if sock.connect_ex((host, int(port))) == 0:
            return True
    except:
        pass
    finally:
        sock.close()


def run(host, **kwargs):
    open_ports = []
    ports = kwargs.get('port') or DEFAULT
    
    build_task(host, ports)
    run_threads(5, task)

    while not result_queue.empty():
        open_ports.append(result_queue.get())
    return open_ports
