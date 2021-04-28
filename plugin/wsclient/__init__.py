# -*- coding: utf-8 -*

"""
@Software : PyCharm
@File : __init__.py
@Author : 梦影
@Time : 2021/04/27 22:22:42
"""

from plugin.wsclient.content import wsHandler
from plugin.common import bot
from nonebot.log import logger
import websockets
import asyncio
import json


@bot.on_startup
async def init():
    asyncio.ensure_future(ws_connect())


async def ws_connect():
    count = 0
    while True:
        try:
            uri = "wss://socket.nicemoe.cn"
            ws = await websockets.connect(uri)
            logger.critical(f'WebSocket > 建立连接成功！')
            setattr(bot, 'wsClient', ws)
            asyncio.ensure_future(ws_task())
            return
        except ConnectionRefusedError as echo:  # 捕获错误
            logger.critical(f"WebSocket > [{count}] {echo}")
            if count == 30:  # 重连次数
                return
            count += 1
            logger.critical(f"WebSocket < [{count}] 开始尝试向 WebSocket 服务端建立连接！")
            await asyncio.sleep(5)  # 重连间隔


async def ws_task():  # WebSocket 任务分发函数
    handler = wsHandler()
    hold = {
        2001: handler.status,
        2002: handler.news,
        2003: handler.serendipity,
    }
    try:
        while True:
            data = await bot.wsClient.recv()  # 循环接收
            logger.debug(f"WebSocket > {data}")
            data = json.loads(data)
            if data['type'] not in hold.keys():
                continue
            asyncio.ensure_future(hold[data['type']](data))  # 创建任务
    except (websockets.exceptions.ConnectionClosedError, websockets.exceptions.ConnectionClosedOK) as echo:  # 捕获错误
        if echo.code == 1006:
            logger.error('WebSocket > 连接已断开！')  # 服务端内部错误
            asyncio.ensure_future(ws_connect())  # 重新连接
        else:
            logger.error('WebSocket > 连接被关闭！')  # 服务端主动关闭
