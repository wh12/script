'''
@File:log.py
@DateTime:2021/12/17 22:12
@Author:wh
@Desc:
'''
import logging
from config.config import log_path

logger=logging.getLogger()
logger.setLevel(logging.INFO)
format=logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s %(message)s')
logFile=log_path
fh=logging.FileHandler(logFile,mode='a',encoding='utf-8')
fh.setLevel(logging.INFO)
fh.setFormatter(format)
logger.addHandler(fh)