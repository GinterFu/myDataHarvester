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
import httpx
import tomllib
import urllib3
from ...huobi_utils.utils import Fetcher

config = tomllib.load(open('../../CONFIG.toml', 'rb')).get('base', {})

class BaseData(Fetcher):
    domain=config.get('DOMAIN')
    def __init__(self, api_name, symbol):
        super().__init__()
        self.api_name = api_name
        self.timestamp = int(datetime.datetime.now().timestamp())

    def get(self):
        try:
            resource_path = config.get('API').get(self.api_name)
            url = self.domain + resource_path
            response=httpx.get(url)
        except Exception as e:
            print(e)
        return response.json()


BaseData('currencies').get()
print(1==1)
# if __name__ == '__main__':
#     pass
