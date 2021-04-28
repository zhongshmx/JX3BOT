# -*- coding: utf-8 -*

"""
@Software : PyCharm
@File : config.py
@Author : 梦影
@Time : 2021/04/27 22:23:04
"""

from plugin.common import robot, bot, common
import random


class extend:
    @staticmethod
    async def server(value):  # 检查用户群已绑定服务器
        sql = "SELECT * FROM main WHERE Value = %s"
        data = await bot.client.query(sql, value)
        if not data:
            return None
        data = await common.next(data)
        return data['Main']

    @staticmethod
    async def serendipityList(name, dwTime, serendipity):  # 奇遇播报发送格式
        sendList = [
            f"{name} 在 {dwTime} 带着 {serendipity} 跑惹！",
            f"{serendipity} 在 {dwTime} 被 {name} 抱走惹！",
            f"{name} 带着 {serendipity} 在 {dwTime} 跑惹！",
            f"{serendipity} 被 {name} 在 {dwTime} 抱走惹！",
            f"{dwTime} {serendipity} 被 {name} 抱走惹！",
            f"{name} 抱着 {serendipity} 在 {dwTime} 走惹！",
            f"{serendipity} 在 {dwTime} 由 {name} 抱走惹！",
            f"{name} 在 {dwTime} 触发了 {serendipity}",
            f"{name} 于 {dwTime} 带走了 {serendipity}",
            f"{serendipity} 于 {dwTime} 被 {name} 触发了",
            f"{serendipity} 在 {dwTime} 卒于 {name}",
            f"{serendipity} 在 {dwTime} 跟着 {name} 跑惹",
        ]
        return random.choice(sendList)


class send:
    @staticmethod
    async def status(value: int, server, message):  # 发送开服信息 # 监控模块
        group_list = await robot.group_list(self_id=value)
        for group_data in group_list:
            sever = await extend.server(group_data['group_id'])
            if sever == server and not await common.token(group_data['group_id']):
                await robot.group_send(self_id=value, group_id=group_data['group_id'], message=message)

    @staticmethod
    async def news(value, message):
        group_list = await robot.group_list(self_id=value)
        for group_data in group_list:
            switch = await common.table('switch', 'Value', group_data['group_id'], 'news')  # 读取开关
            if switch and not await common.token(group_data['group_id']):  # 如果开关打开且群已授权
                await robot.group_send(self_id=value, group_id=group_data['group_id'], message=message)

    @staticmethod
    async def serendipity(value, server, name, dwTime, serendipity):  # 解析奇遇播报数据
        group_list = await robot.group_list(self_id=value)
        for group_data in group_list:
            switch = await common.table('switch', 'Value', group_data['group_id'], 'scheduler')
            sever = await extend.server(group_data['group_id'])
            if switch and sever == server and not await common.token(group_data['group_id']):
                await robot.group_send(self_id=value, group_id=group_data['group_id'],
                                       message=await extend.serendipityList(name, dwTime, serendipity))

    @staticmethod
    async def quake(value, message):
        group_list = await robot.group_list(self_id=value)
        for group_data in group_list:
            switch = await common.table('switch', 'Value', group_data['group_id'], 'quake')
            if switch and not await common.token(group_data['group_id']):
                await robot.group_send(self_id=value, group_id=group_data['group_id'],
                                       message=message)
