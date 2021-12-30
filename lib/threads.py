# author: myc

import time
from threading import Thread

from lib.data import logger


def handle_function(function):
    try:
        function()
    except Exception as err:
        logger.error(err)


def run_threads(thread_num, thread_function):
    threads = []

    try:
        if thread_num == 1:
            thread_function()
            return
        for num in range(thread_num):
            thread = Thread(target=handle_function, name="Thread: "+str(num), args=(thread_function,))
            thread.setDaemon(True)
            try:
                thread.start()
            except:
                break
            threads.append(thread)

        alive = True
        while alive:
            alive = False
            for thread in threads:
                if thread.is_alive():
                    alive = True
                    time.sleep(0.1)
    except KeyboardInterrupt:
        logger.info("Aborted, [Ctrl+C] was pressed")
    except Exception as err:
        logger.error(err)
