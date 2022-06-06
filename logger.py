import config
import logging.handlers
import sys
from datetime import datetime
from bot import Bot


class Logger:
    def __init__(self):
        self.file_handler = logging.FileHandler(filename=config.logging_filename,
                                                mode="a",
                                                encoding="utf-8")

        self.formatter = logging.Formatter("%(asctime)s %(levelname)s %(filename)s %(funcName)s: %(message)s")

        self.stream_handler = logging.StreamHandler(sys.stdout)
        self.stream_handler.setLevel(logging.DEBUG)
        self.stream_handler.setFormatter(self.formatter)

        self.file_handler.setFormatter(self.formatter)

        self.logger = logging.getLogger("Recognizer")
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(self.stream_handler)

    def log_undefined(self):
        if self.stranger():
            self.logger.warning(config.logging_message)
            Bot().send_message(message=config.logging_message)

    def stranger(self):
        last_row = open(config.logging_filename, encoding="utf-8").readlines()[-1]
        last_log_date = datetime.strptime(last_row[:19], '%Y-%m-%d %H:%M:%S')
        now = datetime.now()
        minutes = (now - last_log_date).total_seconds() / 60.0
        if minutes > 5:
            return True
        return False
