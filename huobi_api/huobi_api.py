#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/12/3 22:34
# @Author : Ginter Fu
# @File : huobi_api.py
# @Purpose : 描述
# import websocket

import requests





response = requests.get('https://api.huobi.pro/market/history/kline', params={
    'symbol': 'btcusdt',
    'period': '1min',
    'size': 10,
})


print(1==1)

if __name__ == '__main__':
    pass
