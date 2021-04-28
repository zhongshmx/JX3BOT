# -*- coding: utf-8 -*

"""
@Software : PyCharm
@File : member.py
@Author : 梦影
@Time : 2021/04/28 19:51:29
"""

from nonebot import on_request, RequestSession, on_notice, NoticeSession
from plugin.common import bot, common
from nonebot.log import logger


@on_request('group')
async def _(session: RequestSession):
    user_id = session.ctx['user_id']
    group_id = session.ctx['group_id']
    if not await common.token(group_id):
        # 机器人被邀请
        if session.ctx['sub_type'] == 'invite':
            if user_id in bot.config.SUPERUSERS:  # 被超级用户邀请入群，邀请入群之前请先进行授权，否则会被拒绝！
                await session.approve()
                logger.info(f"管理员:[{user_id}]邀请你加入[{group_id}],已同意！")
            else:
                await session.reject()
                logger.info(f"陌生人:[{user_id}]邀请你加入[{group_id}],已拒绝！")
        # 某人申请入群
        if session.ctx['sub_type'] == 'add':
            await session.approve()
            logger.info(f"[{user_id}]申请加入[{group_id}],已同意！")


@on_notice('group_increase')
async def welcome(session: NoticeSession):
    if not await common.token(await common.value(session)):
        sql = 'SELECT * FROM `switch` WHERE `value` = %s'
        data = await bot.client.query(sql, await common.value(session))
        data = await common.next(data)
        if data['member']:
            result = data['member'].replace("[@QQ]", f"[CQ:at,qq={session.event['user_id']}]")
            logger.info(result)
            await session.send(result)
