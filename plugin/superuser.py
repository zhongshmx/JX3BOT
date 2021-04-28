# -*- coding: utf-8 -*

"""
@Software : PyCharm
@File : superuser.py
@Author : 梦影
@Time : 2021/04/25 19:39:50
"""

from plugin.common import robot, bot, static, common
from nonebot.permission import SUPERUSER
from nonebot import CommandSession, on_command
from nonebot.log import logger
import asyncio
import time


class super:
    @staticmethod
    async def new_group_token(session, content):  # 新增一个群的授权
        number = int(content[2]) * 86400
        server = None
        if len(content) == 4:
            server = await static.data(1, content[3])  # 寻找主服务器全称
        sql = "SELECT * FROM main WHERE Value = %s"
        data = await bot.client.query(sql, content[1])
        if not data:
            number = time.time() + number  # 计算授权天数
            sql = "INSERT INTO main(Value, Main, Relet, Users, Robot) VALUES (%s, %s, %s, %s, %s)"
            await bot.client.execute(sql, (content[1], server, number, session.ctx.user_id, session.self_id))
            if not await bot.client.query("SELECT * FROM switch WHERE value = %s", content[1]):
                sql = "INSERT INTO switch(value) VALUES (%s)"  # 插入群开关数据值
                await bot.client.execute(sql, content[1])
            dwTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(number))
            result = f"{list(bot.config.NICKNAME)[0]}·新增时间\n群号：{content[1]}\n新增：{content[2]}\n区服：{server}\n过期：{dwTime}"
            logger.info(result)
            return result
        data = await common.next(data)
        if time.time() > data['Relet']:  # 本地时间大于数据库时间
            number = time.time() + number  # 重新计算授权天数
        else:
            number = data['Relet'] + number  # 计算授权天数,数据库时间小于本地时间
        server = server if server else data['Main']
        sql = "UPDATE main SET Main = %s, Relet = %s, Users = %s, Robot = %s WHERE Value = %s"
        await bot.client.execute(sql, (server, number, session.ctx.user_id, session.self_id, content[1]))  # 更新授权数据
        dwTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(number))
        result = f"{list(bot.config.NICKNAME)[0]}·追加时间\n群号：{content[1]}\n追加：{content[2]}\n区服：{server}\n过期：{dwTime}"
        logger.info(result)
        return result

    @staticmethod
    async def modify_group_token(session, content):  # 修改某个群的授权
        sql = "SELECT * FROM `main` WHERE `Value` = %s"
        data = await bot.client.query(sql, content[1])
        if data:
            data = await common.next(data)
            sql = "UPDATE main SET Value = %s, Users = %s, Robot = %s WHERE ID = %s"
            await bot.client.execute(sql, (content[2], session.ctx.sender['user_id'], session.self_id, data['ID']))
            dwTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(data['Relet']))
            result = f"{list(bot.config.NICKNAME)[0]}·授权信息\n群号：{content[2]}\n区服：{data['Main']}\n过期：{dwTime}"
        else:
            result = "找不到相关信息！"
        logger.info(result)
        return result

    @staticmethod
    async def del_group_token(session, subtext):  # 取消某个群的授权
        sql = "SELECT * FROM main WHERE Value = %s"
        data = await bot.client.query(sql, subtext[1])
        if data:
            sql = "UPDATE main SET Relet = %s, Users = %s, Robot = %s WHERE Value = %s"
            await bot.client.execute(sql, (1582128000, session.ctx.sender['user_id'], session.self_id, subtext[1]))
            result = f"{list(bot.config.NICKNAME)[0]}·授权信息\n已取消对:{subtext[1]} 的授权！"
        else:
            result = "找不到相关信息！"
        logger.info(result)
        return result


hold = super()
Func = {
    "授权群": hold.new_group_token,
    "修改授权": hold.modify_group_token,
    "取消授权": hold.del_group_token
}


@on_command('G', permission=SUPERUSER, only_to_me=True)
async def admin(session: CommandSession):
    content = await common.subtext(session)
    if len(content) >= 2 and content[0] == '发送群消息':  # 发送消息给所有已授权的群
        text = str(session.ctx['message'])[8:]
        for value in bot.config.ROBOT_LIST:
            asyncio.ensure_future(group.send(value, text))
            await asyncio.sleep(0.1)
    if Func.get(content[0], None):
        result = await Func[content[0]](session, content)
        await session.send(result)


class group:
    @staticmethod
    async def send(value: int, message: str):
        logger.info(message)
        group_list = await robot.group_list(self_id=value)
        for group_data in group_list:
            if not await common.token(group_data['group_id']):
                await robot.group_send(self_id=value, group_id=group_data['group_id'], message=message)
