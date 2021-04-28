# -*- coding: utf-8 -*

"""
@Software : PyCharm
@File : admin.py
@Author : 梦影
@Time : 2021/04/26 18:04:47
"""

from nonebot.permission import SUPERUSER, GROUP_OWNER, GROUP_ADMIN
from nonebot import CommandSession, on_command
from plugin.common import bot, common
from nonebot.log import logger
import time


@on_command('查询授权', aliases='查看授权', permission=SUPERUSER | GROUP_OWNER | GROUP_ADMIN, only_to_me=False)
async def authorization(session: CommandSession):
    sql = "SELECT * FROM main WHERE Value = %s"
    data = await bot.client.query(sql, (await common.value(session)))
    if data:
        data = await common.next(data)
        dwTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(data['Relet']))
        if data['Relet'] > time.time():
            status = '正常'
        else:
            status = '过期'
        result = f"{list(bot.config.NICKNAME)[0]}·查询授权\n群号：{await common.value(session)}\n过期：{dwTime}\n状态：{status}"
    else:
        result = "该群未被正式授权，请通过正规渠道购买使用！"
    logger.info(result)
    await session.send(result)


@on_command('设置欢迎语', permission=SUPERUSER | GROUP_OWNER | GROUP_ADMIN, only_to_me=False)
async def setup_welcome(session: CommandSession):
    content = str(session.ctx['message'])[6:]
    content = content.replace('&#91;', '[').replace('&#93;', ']')
    if not await common.token(await common.value(session)):
        if not content:
            result = "请输入欢迎语！"
        else:
            sql = "UPDATE switch SET member = %s WHERE Value = %s;"
            await bot.client.execute(sql, (content, await common.value(session)))
            result = "设置欢迎语成功！"
    else:
        result = await common.token(await common.value(session))
    logger.info(result)
    await session.send(result)


@on_command('删除欢迎语', permission=GROUP_OWNER | SUPERUSER | GROUP_ADMIN, only_to_me=False)
async def del_welcome(session: CommandSession):
    if not await common.token(await common.value(session)):
        sql = "SELECT * FROM switch WHERE value = %s"
        data = await bot.client.query(sql, await common.value(session))
        data = await common.next(data)
        if not data['member']:
            result = "本群未设置欢迎语！"
        else:
            sql = "UPDATE switch SET member = %s WHERE Value = %s"
            await bot.client.execute(sql, (None, await common.value(session)))
            result = "删除欢迎语成功！"
    else:
        result = await common.token(await common.value(session))
    logger.info(result)
    await session.send(result)


funcList = {'官方资讯': 'news', '撩人模式': 'random', '奇遇玩法': 'reward', '游戏功能': 'player', '自由聊天': 'nlpchat',
            '奇遇播报': 'scheduler'}


@on_command('开启', permission=GROUP_OWNER | SUPERUSER | GROUP_ADMIN, only_to_me=False)
async def open_func(session: CommandSession):
    content = await common.subtext(session)
    if not await common.token(await common.value(session)):
        if content[0] in funcList.keys():
            sql = f"UPDATE switch SET {funcList[content[0]]} = %s WHERE Value = %s;"
            await bot.client.execute(sql, (1, await common.value(session)))
            result = f"{content[0]} 开启成功！"
        else:
            result = f"找不到 {content[0]} 的开关！"
    else:
        result = await common.token(await common.value(session))
    logger.info(result)
    await session.send(result)


@on_command('关闭', permission=GROUP_OWNER | SUPERUSER | GROUP_ADMIN, only_to_me=False)
async def open_func(session: CommandSession):
    content = await common.subtext(session)
    if not await common.token(await common.value(session)):
        if content[0] in funcList.keys():
            sql = f"UPDATE switch SET {funcList[content[0]]} = %s WHERE Value = %s;"
            await bot.client.execute(sql, (0, await common.value(session)))
            result = f"{content[0]} 关闭成功！"
        else:
            result = f"找不到 {content[0]} 的开关！"
    else:
        result = await common.token(await common.value(session))
    logger.info(result)
    await session.send(result)
