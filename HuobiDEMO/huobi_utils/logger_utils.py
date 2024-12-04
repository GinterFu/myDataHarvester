#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/12/4 22:56
# @Author : Ginter Fu
# @File : logger_utils.py
# @Purpose : 描述
'''
HuobiLogger
'''
import logging

class HBLogger:
    def __init__(self, logger_level=logging.INFO):
        self.logger_level=logger_level
        self.formatter = logging.Formatter(
            '[%(levelname)s]%(asctime)s|ThreadID:%(thread)s|%(filename)s|%(pathname)s|%(funcName)s|%(lineno)s|%(message)s'
            , '%Y-%m-%d %H:%M:%S'
        )
        self.logger : logging.Logger = logging.getLogger()
        self.logger.setLevel(logger_level)