import json

import pytest
from selenium import webdriver

from readConfigfile import config


@pytest.fixture()
@pytest.mark.usefixtures('config')
def configProperties(request, config):
    driver = webdriver.Chrome(executable_path=config[r'chrome'])
    driver.get(config['URL'])
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()



