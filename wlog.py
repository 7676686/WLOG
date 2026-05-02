import logging
import time
import os
import json

version="1.0.0"
def init(project="project",version="1.0.0"):
    stable={"project":project,"version":version}
    # Init log file
    try:
        os.mkdir(".local")
    except FileExistsError:
        pass
    try:
        config=json.load(open(".wlog_info.json","r"))
        try:
            os.mkdir(".local/"+config['project'])
        except FileExistsError:
            pass
        try:
            os.mkdir(".local/"+config['project']+"/wlog/")
        except FileExistsError:
            pass
        return config
    except FileNotFoundError:
        with open(".wlog_info.json","w+") as f:
            json.dump(stable,f)
            return init(project=project,version=version)
config=init()
_format=logging.Formatter("[%(asctime)s](%(filename)s)(%(funcName)s){%(lineno)d}[%(levelname)s]:%(message)s")
logger=logging.getLogger(config["project"])
logger.setLevel(logging.DEBUG)
ch=logging.StreamHandler()
fh=logging.FileHandler(filename=".local/"+config["project"]+"/wlog/"+str(time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime()))+".log",mode="w+")
ch.setLevel(logging.DEBUG)
fh.setLevel(logging.DEBUG)
ch.setFormatter(_format)
fh.setFormatter(_format)
logger.addHandler(ch)
logger.addHandler(fh)
logger.info("WLOG initialized successfully")
logger.info("------------------------------WLOG INFO-------------------------")
logger.info(" | project: %s | version: %s | WLOG version: %s |", config["project"], config["version"],version)
logger.info("----------------------------------------------------------------")