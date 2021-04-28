# -*- coding: utf-8 -*

"""
@Software : PyCharm
@File : __init__.py
@Author : 梦影
@Time : 2021/04/27 22:22:13
"""

from plugin.common import bot, robot, common
from plugin.random.content import seasun
from plugin.random.config import extend
from nonebot.log import logger
from nonebot import aiocqhttp

command = f"{list(bot.config.NICKNAME)[0]}说"

func = {command: seasun.content}


@bot.on_message('group')  # 聊天功能
async def nlpchat(event: aiocqhttp.Event):
    message = str(event['message'])
    value = await common.tencent(message)
    if value:
        if value[0] == str(event.self_id):
            message = message.replace(f"[CQ:at,qq={value[0]}]", list(bot.config.NICKNAME)[0])
    if list(bot.config.NICKNAME)[0] in message and message[0:3] != command:
        print(message)
        if not await common.token(event['group_id']):
            result = await seasun.nlpchat(message)
        else:
            result = await common.token(event['group_id'])
        logger.info(result)
        await robot.event(event, result)
    return


@bot.on_message('group')  # 语音合成
async def voice(event: aiocqhttp.Event):
    message = str(event['message'])
    if func.get(message[0:3], None):
        if not await common.token(event['group_id']):
            result = await func[message[0:3]](message[0:3])
        else:
            result = await common.token(event['group_id'])
        logger.info(result)
        await robot.event(event, result)
    return


@bot.on_message('group')  # 随机骚话
async def random(event: aiocqhttp.Event):
    message = str(event['message'])
    if len(message) >= 5 and 'CQ' not in message and await extend.rand():
        switch = await common.table('switch', 'Value', event['group_id'], 'random')
        if switch and not await common.token(event['group_id']):
            result = await seasun.random(event)
            logger.info(result)
            await robot.event(event, result)
    return


@bot.on_message('group')  # 自由聊天
async def randchat(event: aiocqhttp.Event):
    message = str(event['message'])
    if len(message) >= 2 and 'CQ' not in message and await extend.chat():
        switch = await common.table('switch', 'Value', event['group_id'], 'nlpchat')
        if switch and not await common.token(event['group_id']):
            result = await seasun.nlpchat(message)
            logger.info(result)
            await robot.event(event, result)
    return
