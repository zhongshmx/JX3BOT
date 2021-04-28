# -*- coding: utf-8 -*

"""
@Software : PyCharm
@File : config.py
@Author : 梦影
@Time : 2021/04/28 19:56:08
"""

from plugin.common import bot
import random


class extend:
    @staticmethod
    async def rand():  # 文字触发几率 # 随机模块
        if random.randint(1, 100) <= bot.config.RANDOM_MAX_VALUE:
            result = True
        else:
            result = False
        return result

    @staticmethod
    async def chat():  # 聊天触发几率 # 随机模块
        if random.randint(1, 100) <= bot.config.NLPCHAT_MAX_VALUE:
            result = True
        else:
            result = False
        return result
