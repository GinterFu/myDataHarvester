#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/11/2 01:38
# @Author : Ginter Fu
# @File : test.py
# @Purpose : 描述

import re
from playwright.sync_api import sync_playwright, Page, expect



def get_page():
    context = sync_playwright().start().chromium.launch(
        headless=False,
        ignore_default_args=["--enable-automation"],  # 关闭自动控制特征
        args=["--window-size=1920,1080", "-–start-maximized"],  # 全屏打开
        slow_mo=0.5,
        channel='chrome'
    )
    browser = context.new_context(
        viewport={"width": 1920, "height": 1080},
        screen={"width": 1920, "height": 1080},
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70",
    )
    # 防止被识别为自动控制
    js1 = """
               Object.defineProperties(navigator,{webdriver:{get:()=>undefined}});
               """
    js2 = """window.navigator.chrome={runtime:{},};"""
    js3 = (
        """Object.defineProperty(navigator,'languages',{get:()=>['en-US','en']});"""
    )
    js4 = """Object.defineProperty(navigator,'plugins',{get:()=>[1,2,3,4,5,6],});"""
    browser.add_init_script(js1)
    browser.add_init_script(js2)
    browser.add_init_script(js3)
    browser.add_init_script(js4)
    page = browser.new_page()
    return page
page = get_page()
page.goto('https://www.dianping.com')
print(1==1)