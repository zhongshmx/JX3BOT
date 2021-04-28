# -*- coding: utf-8 -*

"""
@Software : PyCharm
@File : common.py
@Author : 梦影
@Time : 2021/04/25 19:30:09
"""

from plugin.dict import serverList, flowerList, sectList, serendipityList
from aiocqhttp import ActionFailed, ApiNotAvailable
from plugin.database import MySql, MySqlInit
from aiocqhttp.message import Message
from aiohttp import ClientSession

from nonebot.log import logger
from nonebot import get_bot
import asyncio
import json
import time

bot = get_bot()
BOT = bot.config


class common:
    @staticmethod
    async def tencent(arg):  # CQ:QQ # 公共模块
        arg_as_msg = Message(arg)
        return [s.data['qq'] for s in arg_as_msg if s.type == 'at']

    @staticmethod
    async def subtext(session):  # 获取参数组
        return session.current_arg_text.split()

    @staticmethod
    async def value(session):  # 获取来源群号
        return session.ctx['group_id']

    @staticmethod
    async def token(value):  # 判断是否被授权
        sql = 'SELECT * FROM `main` WHERE `Value` = %s'
        data = await bot.client.query(sql, value)
        if not data:
            return "该群未被正式授权，请通过正常渠道购买使用！"
        base = await common.next(data)
        if base['Relet'] > int(time.time()):
            result = False
        else:
            result = "该群已过期，请尽快续费恢复服务！"
        return result

    @staticmethod
    async def next(data: list):  # 下一条数据
        for item in data:
            return item

    @staticmethod
    async def table(Table, FieldName, FieldValue, Value):  # 自定义查询数据库数据 # 公共模块
        sql = f"SELECT * FROM `{Table}` WHERE `{FieldName}` = '{FieldValue}'"
        data = await bot.client.query(sql)
        if data:
            data = await common.next(data)
            return data[Value]
        return None


# 网页访问
class submit:
    @staticmethod
    async def connect(url: str, data=None, headers=None, timeout=10): # POST
        async with ClientSession() as session:
            async with session.post(url=url, data=data, headers=headers, timeout=timeout) as data:
                result = await data.text()
                data.close()
                return await submit.data(result)

    @staticmethod
    async def content(url: str, params=None, headers=None, timeout=10): # GET
        async with ClientSession() as session:
            async with session.get(url=url, params=params, headers=headers, timeout=timeout) as data:
                result = await data.text()
                data.close()
                return await submit.data(result)

    @staticmethod
    async def sms(tencent: int):  # 发送短信通知
        data = {"phone": BOT.SMS_PHONE, "tencent": tencent}
        result = await submit.connect(url=f"{bot.domain}/qcloud/app.php", data=data)
        if not result['result']:
            logger.info("发送短信成功！")
        else:
            logger.info("发送短信失败！")
        bot.status[tencent] = 0

    @staticmethod
    async def data(text):
        try:
            result = json.loads(text)
        except ValueError:
            return text
        return result


# 机器人操作
class robot:
    @staticmethod
    async def group_list(self_id: int):  # 获取群列表
        result = list()
        try:
            result = await bot.get_group_list(self_id=self_id)
            if bot.status[self_id] == 0:
                bot.status[self_id] = 1
        except ApiNotAvailable:
            logger.error(f"请求群信息'{self_id}'有问题惹！")
            if bot.status[self_id] == 1:
                asyncio.ensure_future(submit.sms(self_id))  # 发送短信
        return result

    @staticmethod
    async def group_send(self_id: int, group_id, message):  # 发送群消息
        try:
            await bot.send_group_msg(self_id=self_id, group_id=group_id, message=message)
        except ActionFailed:
            logger.error(f"发送群消息'{group_id}'有问题惹！")

    @staticmethod
    async def event(event, content):  # 发送事件消息
        try:
            await bot.send(event, content)
        except ActionFailed:
            logger.error(f"发送群消息'{event['group_id']}有问题惹！")

    @staticmethod
    async def sender(session):  # 发送人名称
        if "sender" not in session.keys():
            if not session.ctx['sender']['card']:
                return session.ctx['sender']['nickname']
            return session.ctx['sender']['card']
        else:
            if not session['sender']['card']:
                return session['sender']['nickname']
            return session['sender']['card']


class static:
    @staticmethod
    async def data(data, value):  # 检索服务器，花价，心法，奇遇数据
        if data == 0:
            return value['Main']
        m = {1: serverList, 2: flowerList, 3: sectList, 4: serendipityList}
        result = None
        for k, v in m[data].items():
            if value in v:
                result = k
        return result


@bot.on_startup
async def init():  # 初始化
    connect = MySql()
    pool = await connect.initpool(BOT)
    connect.pool = pool
    setattr(bot, 'status', dict())
    setattr(bot, 'client', connect)
    setattr(bot, 'domain', BOT.DATA_DOMAIN)
    for x in BOT.ROBOT_LIST:
        bot.status[x] = 0
    asyncio.ensure_future(MySqlInit(bot, serverList))
