#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/12/3 22:34
# @Author : Ginter Fu
# @File : market_realtime.py
# @Purpose : 描述

import requests
import httpx
# import pydantic
from HuobiDEMO.huobi_utils.utils import Parser


class MarketParams:
    symbol = 'btcusdt'
    period = '1min'
    size = 10


class MarketFetcher:
    def fetch(self, *args, **kwargs):
        '''
        Args:
            params:
                @symbol: 交易对
                    btcusdt、ethusdt等，如需获取杠杆ETP净值K-line则：净值symbol=杠杆ETP交易对symbol+后缀nav，如btc3lusdtnav
                @period: 数据时间粒度
                    返回数据时间粒度，如1min、5min、15min、30min、60min、4hour、1day、1mon、1week、1year
                @size: 数据量
                    返回数据量，[1, 2000]
        Return:
            response:httpx.Response
        '''
        params = kwargs.get('params', None)
        response = httpx.get('https://api.huobi.pro/market/history/kline', params=params)
        if not response.is_error:
            return response
        else:
            raise httpx.HTTPStatusError(f'【响应错误】请求状态码为：{response.status_code}')



# class MarketParser(Parser):
#     def parse(self):
#         return response.json()

print(1==1)

if __name__ == '__main__':
    pass
