# -*- coding: utf-8 -*

"""
@Software : PyCharm
@File : scheduler.py
@Author : 梦影
@Time : 2021/04/28 21:15:58
"""

from plugin.common import bot, robot, common
import nonebot
import datetime

job = nonebot.scheduler.scheduled_job


@job('cron', minute='0', hour='0', day_of_week='*', misfire_grace_time=5)
async def exit():
    for value in bot.config.ROBOT.LIST:
        group_list = await robot.group_list(self_id=value)
        for group_data in group_list:
            sql = 'SELECT * FROM main WHERE Value = %s'
            data = await bot.client.query(sql, group_data['group_id'])
            if data:
                data = await common.next(data)
                result = (datetime.datetime.now() - datetime.datetime.fromtimestamp(data['Relet'])).days
                if result >= bot.config.ROBOT_EXIT_TIME:
                    await bot.set_group_leave(self_id=value, group_id=group_data['group_id'])
            else:
                await bot.set_group_leave(self_id=value, group_id=group_data['group_id'])
