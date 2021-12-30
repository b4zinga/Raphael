# author: myc

import logging


class LoggerHandler:
    def __init__(self, name="log", level="INFO", file=None, fmt=None):
        self.name = name
        self.level = level
        self.file = file
        self.fmt = logging.Formatter(fmt)

        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(self.level)

    def set_file_handler(self):
        file_handler = logging.FileHandler(self.file)
        file_handler.setFormatter(self.fmt)
        self.logger.addHandler(file_handler)

    def set_stream_handler(self):
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(self.fmt)
        self.logger.addHandler(stream_handler)

    def get_logger(self):
        if self.file:
            self.set_file_handler()
        self.set_stream_handler()
        return self.logger
