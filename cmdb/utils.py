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

# 通用分页函数
def paginate(page, size, query):
    try:
        page = page if page > 0 else 1
        size = size if 0 < size < 101 else 20

        count = query.count()
        pages = math.ceil(count / size)
        result = query.limit(size).offset(size * (page - 1)).all()
        return result, (page, size, count, pages)
    except Exception as e:
        logger.error('{}'.format(e))

