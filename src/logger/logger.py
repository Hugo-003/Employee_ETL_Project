import sys
import datetime
import logging


class Logger:

    def __init__(self, log_path, log_level, log_identifier, show_file_line=True):

        self.total_ast_num = 60
        self.log_identifier = log_identifier
        self.logger = logging.getLogger(log_identifier)
        self.log_level = log_level
        self.logger.setLevel(log_level)

        file_line = "(%(filename)s:%(lineno)s) || " if show_file_line else ""

        if not self.logger.handlers:

            formatter = logging.Formatter(f"[%(asctime)s] || %(levelname)s || {file_line}%(message)s",
                                          datefmt="%Y-%m-%d %H:%M:%S")

            file_handler = logging.FileHandler(log_path +
                                               datetime.date.today().strftime("%Y%m%d") +
                                               "_" + log_identifier +
                                               "_ETL.log", mode="w")
            file_handler.setLevel(log_level)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

            console_handler = logging.StreamHandler(stream=sys.stdout)
            console_handler.setLevel(log_level)
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

    def log(self, message, log_level=None):
        log_level = log_level if log_level else self.log_level
        self.logger.log(log_level, message)

    def start_log(self):
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        start_msg = f"INITIATING {self.log_identifier} ETL"
        init_date = f"{now}"

        start_msg_side_space = round((self.total_ast_num - len(start_msg) - 2) / 2)
        init_date_side_space = round((self.total_ast_num - len(init_date) - 2) / 2)

        self.log("*" * self.total_ast_num, logging.INFO)
        self.log((" " * start_msg_side_space) + start_msg, logging.INFO)
        self.log((" " * init_date_side_space) + init_date, logging.INFO)
        self.log("*" * self.total_ast_num, logging.INFO)

    def log_dict(self, message, dictionary):
        for key, value in dictionary.items():
            self.log(f"{message}[{key.upper()}]: {value}")