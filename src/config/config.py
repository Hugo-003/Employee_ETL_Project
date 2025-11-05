import configparser
import logging
import os

class Config:

    def __init__(self):

        print("[INFO] Running the Config File")
        config_file = "./config/config.ini"

        self.config = configparser.ConfigParser()
        self.config.sections()
        self.config.read(config_file)

        # LOGGING_CONFIGURATION
        self.log_path = self.config["LOGGING_CONFIGURATION"]["LOG_PATH"]
        self.log_level = self.config["LOGGING_CONFIGURATION"]["LOG_LEVEL"]

        if self.log_level == "CRITICAL":
            self.log_level = logging.CRITICAL
        elif self.log_level == "ERROR":
            self.log_level = logging.ERROR
        elif self.log_level == "WARNING":
            self.log_level = logging.WARNING
        elif self.log_level == "INFO":
            self.log_level = logging.INFO
        elif self.log_level == "DEBUG":
            self.log_level = logging.DEBUG
        elif self.log_level == "NOTSET":
            self.log_level = logging.NOTSET

        self.etl_name = self.config["ETL_GLOBALS"]["ETL_NAME"]

        self.input_csv = self.config["INPUT_FILE"]["INPUT_CSV"]

        self.out_csv = self.config["OUTPUT_FILE"]["OUTPUT_CSV"]
        self.out_csv2 = self.config["OUTPUT_FILE"]["OUTPUT2_CSV"]
        self.out_csv3 = self.config["OUTPUT_FILE"]["OUTPUT3_CSV"]
        self.out_csv4 = self.config["OUTPUT_FILE"]["OUTPUT4_CSV"]
        self.out_csv5 = self.config["OUTPUT_FILE"]["OUTPUT5_CSV"]
        self.out_csv6 = self.config["OUTPUT_FILE"]["OUTPUT6_CSV"]
        self.out_csv7 = self.config["OUTPUT_FILE"]["OUTPUT7_CSV"]

        print(f"{self.input_csv}")
