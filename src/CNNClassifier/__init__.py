import os
import sys
import logging

logging_str="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"

log_dir="logs"            # collect all logs

log_filepath=os.path.join(log_dir,"running_logs.log")  #log file path name

os.makedir(log_dir,exist_ok=True)

logging.basicConig(
    level=logging.INFO,  #level of logging
    format-logging_str
    handlers=[
        logging.FileHandler(log_filepath)   #all msg collecting
        logging.StreamHandler(sys.stdout)   # whatever msg or logs capture inside the file ,it is visible in cmd also
    ]
                    )
    logger = logging.getLogger("CNNClassifier")






