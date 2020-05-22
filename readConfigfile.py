import json

import pytest


@pytest.fixture(scope='session')
def config():
    with open('config.json') as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture()
def read_method():
    with open('dataAtMethodlevel.json') as read_data:
        read_methoddata = json.load(read_data)
    return read_methoddata
