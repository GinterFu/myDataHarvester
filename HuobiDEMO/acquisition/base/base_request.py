#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/12/4 21:49
# @Author : Ginter Fu
# @File : base_request.py
# @Purpose : 描述
'''

'''
__all__=['BaseData']
import datetime
import os

import httpx
import tomllib
import urllib3
from HuobiDEMO.huobi_utils.utils import Fetcher

with open('/Users/ginter/mySpace/myProjects/devPython/HuobiDEMO/CONFIG.toml', 'rb') as f:
    config = tomllib.load(f)

class BaseData(Fetcher):
    domain=config.get('base').get('DOMAIN')
    def __init__(self, api_name, symbol):
        super().__init__()
        self.api_name = api_name
        self.timestamp = int(datetime.datetime.now().timestamp())

    def get(self):
        try:
            print(self.api_name)
            resource_path = config.get('base').get('API').get(self.api_name)
            url = ''.join([self.domain, resource_path])
            response=httpx.get(url, params={'t': self.timestamp})
        except Exception as e:
            print(e)
        else:
            return response.json()


ins=BaseData('symbols', 'usdt')
ins.get()

ins.get()
print(1==1)
# if __name__ == '__main__':
#     pass
