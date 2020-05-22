import logging

import pytest


def logger():
    logging.basicConfig(filename="newfile.log",
                        format='%(asctime)s,%(msecs)d %(levelname)-8s [%(module)s:%(lineno)d] %(message)s',
                        filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    return logger

@pytest.mark.usefixtures('configProperties')
class BaseClassPySel:
    pass