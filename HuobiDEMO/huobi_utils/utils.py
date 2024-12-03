#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/12/3 23:08
# @Author : Ginter Fu
# @File : utils.py
# @Purpose : 描述

class Parser:
    def __init__(self, args):
        self.args = args

    def parse(self, *args, **kwargs):
        raise NotImplementedError(f'【调用错误】方法未实现，以至于实际调用接口：{self.__class__.__qualname__}')