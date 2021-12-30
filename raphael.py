#!/usr/bin/env python3
# author: myc

import time
from lib.data import logger
from lib.options import init
from lib.controller import start


def main():
    start_time = time.time()
    logger.info("Raphael Start ~")
    init()
    start()
    logger.info("Finished at: {}".format(time.strftime("%Y-%m-%d %H:%M:%S")))
    logger.info("Total: {} s".format(time.time() - start_time))


if __name__ == '__main__':
    main()
