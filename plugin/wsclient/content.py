# -*- coding: utf-8 -*

"""
@Software : PyCharm
@File : content.py
@Author : 梦影
@Time : 2021/04/27 22:23:08
"""

from plugin.wsclient.config import extend, send
from plugin.common import bot
from nonebot.log import logger
import asyncio
import time


class wsHandler:
    @staticmethod
    async def status(data):
        data = data['data']
        sql = "UPDATE `status` SET `status` = %s WHERE `server` = %s"
        await bot.client.execute(sql, (data['status'], data['server']))
        status = {0: "维护", 1: "开服"}
        result = f"{data['server']} 在 {time.strftime('%H:%M:%S', time.localtime(time.time()))} {status[data['status']]}惹！"
        logger.info(result)
        for value in bot.config.ROBOT_LIST:
            asyncio.ensure_future(send.status(value, data['server'], result))
            await asyncio.sleep(0.1)

    @staticmethod
    async def news(data):
        data = data['data']
        result = f"{data['type']}来惹\n标题：{data['title']}\n链接：{data['url']}\n日期：{data['date']}"
        logger.info(result)
        for value in bot.config.ROBOT_LIST:
            asyncio.ensure_future(send.news(value, result))
            await asyncio.sleep(0.1)

    @staticmethod
    async def serendipity(data):
        data = data['data']
        dwTime = time.strftime("%H:%M", time.localtime(data['time']))
        logger.info(await extend.serendipityList(data['name'], dwTime, data['serendipity']))
        for value in bot.config.ROBOT_LIST:  # 开始发送消息
            asyncio.ensure_future(send.serendipity(value, data['server'], data['name'], dwTime, data['serendipity']))
            await asyncio.sleep(0.1)