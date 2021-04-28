# -*- coding: utf-8 -*

"""
@Software : PyCharm
@File : config.py
@Author : 梦影
@Time : 2021/04/26 20:21:16
"""

from plugin.common import bot, common
import time


class extend:
    @staticmethod
    async def select(value):  # 查询用户群数据
        sql = 'SELECT * FROM `main` WHERE `Value` = %s'
        data = await bot.client.query(sql, value)
        result = await common.next(data)
        return result

    @staticmethod
    async def update(value, name, number):  # 更新用户群间隔数据
        name = f"CD.{name}"
        sql = f"UPDATE `main` SET `{name}` = {time.time() + number} WHERE `Value` = {value}"
        await bot.client.execute(sql)

    @staticmethod
    async def week(date):  # 指定时间星期几 # 查询模块
        text = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期天"]
        ret = date.weekday()
        return text[ret]

    @staticmethod
    async def count(text):  # 计算冷却时间 # 查询模块
        result = text - int(time.time())
        return f'模块冷却中({result})...'

    @staticmethod
    async def local(data, value):  # 本地记录的时间戳
        if not data:
            return 0
        if value == 1080:
            result = time.time()
        else:
            result = data[f'CD.{value}']
        return result

    @staticmethod
    async def lock(server, value):  # 更新数据库数据
        sql = 'UPDATE `main` SET `Main` = %s WHERE `Value` = %s'
        await bot.client.execute(sql, (server, value))
