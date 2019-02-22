import logging

# 日志
def getlogger(mod_name:str, filepath:str="D:log"):
    logger = logging.getLogger(mod_name)
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.FileHandler('{}/{}.log'.format(filepath, mod_name))
    formatter = logging.Formatter('%(asctime)s [%(module)s %(funcName)s] %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger