# -*- coding: utf-8 -*

"""
@Software : PyCharm
@File : __init__.py
@Author : 梦影
@Time : 2021/04/26 20:21:12
"""

from nonebot.permission import SUPERUSER, GROUP_OWNER, GROUP_ADMIN, GROUP_MEMBER
from nonebot import on_command, CommandSession, aiocqhttp
from plugin.common import robot, bot, common
from plugin.content.content import seasun
from nonebot.log import logger


@on_command('日常', aliases=('日常查询', '查询日常'), permission=GROUP_MEMBER, only_to_me=False)
async def content(session: CommandSession):
    if not await common.token(await common.value(session)):
        result = await seasun.content(session)
    else:
        result = await common.token(await common.value(session))
    logger.info(result)
    await session.send(result)


@on_command('开服', aliases=('开服查询', '查询开服'), permission=GROUP_MEMBER, only_to_me=False)
async def status(session: CommandSession):
    if not await common.token(await common.value(session)):
        result = await seasun.status(session)
    else:
        result = await common.token(await common.value(session))
    logger.info(result)
    await session.send(result)


@on_command('金价', aliases=('金价查询', '查询金价'), permission=GROUP_MEMBER, only_to_me=False)
async def gold(session: CommandSession):
    if not await common.token(await common.value(session)):
        result = await seasun.gold(session)
    else:
        result = await common.token(await common.value(session))
    logger.info(result)
    await session.send(result)


@on_command('花价', aliases=('花价查询', '查询花价'), permission=GROUP_MEMBER, only_to_me=False)
async def flower(session: CommandSession):
    if not await common.token(await common.value(session)):
        result = await seasun.flower(session)
    else:
        result = await common.token(await common.value(session))
    logger.info(result)
    await session.send(result)


@on_command('沙盘', aliases=('沙盘查询', '查询沙盘'), permission=GROUP_MEMBER, only_to_me=False)
async def sand(session: CommandSession):
    if not await common.token(await common.value(session)):
        result = await seasun.sand(session)
    else:
        result = await common.token(await common.value(session))
    logger.info(result)
    await session.send(result)


@on_command('副本', aliases=('PVE', 'pve'), permission=GROUP_MEMBER, only_to_me=False)
async def pve(session: CommandSession):
    if not await common.token(await common.value(session)):
        result = await seasun.pve(session)
    else:
        result = await common.token(await common.value(session))
    logger.info(result)
    await session.send(result)


@on_command('竞技', aliases=('PVP', 'pvp'), permission=GROUP_MEMBER, only_to_me=False)
async def pvp(session: CommandSession):
    if not await common.token(await common.value(session)):
        result = await seasun.pvp(session)
    else:
        result = await common.token(await common.value(session))
    logger.info(result)
    await session.send(result)


@on_command('绝境', aliases=('绝境奇穴', '吃鸡', '吃鸡奇穴'), permission=GROUP_MEMBER, only_to_me=False)
async def plan(session: CommandSession):
    if not await common.token(await common.value(session)):
        result = await seasun.plan(session)
    else:
        result = await common.token(await common.value(session))
    logger.info(result)
    await session.send(result)


@on_command('战场', aliases=('战场奇穴', '奇穴', '查询奇穴'), permission=GROUP_MEMBER, only_to_me=False)
async def battle(session: CommandSession):
    if not await common.token(await common.value(session)):
        result = await seasun.battle(session)
    else:
        result = await common.token(await common.value(session))
    logger.info(result)
    await session.send(result)


@on_command('小药', aliases=('小药查询', '查询小药'), permission=GROUP_MEMBER, only_to_me=False)
async def heighten(session: CommandSession):
    if not await common.token(await common.value(session)):
        result = await seasun.heighten(session)
    else:
        result = await common.token(await common.value(session))
    logger.info(result)
    await session.send(result)


@on_command('宏', aliases=('宏命令', '云端宏'), permission=GROUP_MEMBER, only_to_me=False)
async def macro(session: CommandSession):
    if not await common.token(await common.value(session)):
        result = await seasun.macro(session)
    else:
        result = await common.token(await common.value(session))
    logger.info(result)
    await session.send(result)


@bot.on_message('group')  # 格式：冰心宏
async def macros(event: aiocqhttp.Event):
    message = str(event['message'])
    if len(message) >= 3 and message[-1] == '宏':
        if not await common.token(event['group_id']):
            result = await seasun.macros(event)
        else:
            result = await common.token(event['group_id'])
        logger.info(result)
        await robot.event(event, result)


@on_command('物价', aliases=('物价查询', '查询物价'), permission=GROUP_MEMBER, only_to_me=False)
async def prices(session: CommandSession):
    if not await common.token(await common.value(session)):
        result = await seasun.prices(session)
    else:
        result = await common.token(await common.value(session))
    logger.info(result)
    await session.send(result)


@on_command('条件', aliases=('条件查询', '查询条件'), permission=GROUP_MEMBER, only_to_me=False)
async def method(session: CommandSession):
    if not await common.token(await common.value(session)):
        result = await seasun.method(session)
    else:
        result = await common.token(await common.value(session))
    logger.info(result)
    await session.send(result)


@on_command('成就', aliases=('成就查询', '查询成就'), permission=GROUP_MEMBER, only_to_me=False)
async def achievement(session: CommandSession):
    if not await common.token(await common.value(session)):
        result = await seasun.achievement(session)
    else:
        result = await common.token(await common.value(session))
    logger.info(result)
    await session.send(result)


@on_command('科举', aliases=('科举查询', '查询科举'), permission=GROUP_MEMBER, only_to_me=False)
async def exam(session: CommandSession):
    if not await common.token(await common.value(session)):
        result = await seasun.exam(session)
    else:
        result = await common.token(await common.value(session))
    logger.info(result)
    await session.send(result)


@on_command('图谱', aliases=('器物谱', '查询器物谱'), permission=GROUP_MEMBER, only_to_me=False)
async def travel(session: CommandSession):
    if not await common.token(await common.value(session)):
        result = await seasun.travel(session)
    else:
        result = await common.token(await common.value(session))
    logger.info(result)
    await session.send(result)


@on_command('装饰', aliases=('装饰查询', '查询装饰'), permission=GROUP_MEMBER, only_to_me=False)
async def furniture(session: CommandSession):
    if not await common.token(await common.value(session)):
        result = await seasun.furniture(session)
    else:
        result = await common.token(await common.value(session))
    logger.info(result)
    await session.send(result)


@on_command('公告', aliases=('公告查询', '更新公告'), permission=GROUP_MEMBER, only_to_me=False)
async def announcement(session: CommandSession):
    if not await common.token(await common.value(session)):
        result = await seasun.announcement(session)
    else:
        result = await common.token(await common.value(session))
    logger.info(result)
    await session.send(result)


@on_command('奇遇', aliases=('奇遇查询', '查询奇遇'), permission=GROUP_MEMBER, only_to_me=False)
async def adventure(session: CommandSession):
    if not await common.token(await common.value(session)):
        result = await seasun.adventure(session)
    else:
        result = await common.token(await common.value(session))
    logger.info(result)
    await session.send(result)


@on_command('查询', aliases=('个人查询', '查询个人'), permission=GROUP_MEMBER, only_to_me=False)
async def personal(session: CommandSession):
    if not await common.token(await common.value(session)):
        result = await seasun.personal(session)
    else:
        result = await common.token(await common.value(session))
    logger.info(result)
    await session.send(result)


@on_command('点歌', aliases=('腾讯点歌', 'QQ点歌'), permission=GROUP_MEMBER, only_to_me=False)
async def music(session: CommandSession):
    if not await common.token(await common.value(session)):
        result = await seasun.music(session)
    else:
        result = await common.token(await common.value(session))
    logger.info(result)
    await session.send(result)


@on_command('网易', aliases=('网易点歌', '163点歌'), permission=GROUP_MEMBER, only_to_me=False)
async def netease(session: CommandSession):
    if not await common.token(await common.value(session)):
        result = await seasun.netease(session)
    else:
        result = await common.token(await common.value(session))
    logger.info(result)
    await session.send(result)


@on_command('世界', aliases=('骚话', '世界骚话'), permission=GROUP_MEMBER, only_to_me=False)
async def world(session: CommandSession):
    if not await common.token(await common.value(session)):
        result = await seasun.world(session)
    else:
        result = await common.token(await common.value(session))
    logger.info(result)
    await session.send(result)


@on_command('阵眼', aliases=('阵眼查询', '查询阵眼'), permission=GROUP_MEMBER, only_to_me=False)
async def gest(session: CommandSession):
    if not await common.token(await common.value(session)):
        result = await seasun.gest(session)
    else:
        result = await common.token(await common.value(session))
    logger.info(result)
    await session.send(result)


@on_command('挂件', aliases=('挂件查询', '查询挂件'), permission=GROUP_MEMBER, only_to_me=False)
async def pendant(session: CommandSession):
    if not await common.token(await common.value(session)):
        result = await seasun.pendant(session)
    else:
        result = await common.token(await common.value(session))
    logger.info(result)
    await session.send(result)


@on_command('日记', aliases=('舔狗', '舔狗日记'), permission=GROUP_MEMBER, only_to_me=False)
async def dog(session: CommandSession):
    if not await common.token(await common.value(session)):
        result = await seasun.dog(session)
    else:
        result = await common.token(await common.value(session))
    logger.info(result)
    await session.send(result)


@on_command('菜单', aliases=('功能', '帮助', '说明', '使用说明', '使用帮助'), permission=GROUP_MEMBER, only_to_me=False)
async def explain(session: CommandSession):
    if not await common.token(await common.value(session)):
        result = await seasun.explain(session)
    else:
        result = await common.token(await common.value(session))
    logger.info(result)
    await session.send(result)


@on_command('绑定', aliases=('绑定区服', '区服绑定'), permission=SUPERUSER | GROUP_OWNER | GROUP_ADMIN, only_to_me=False)
async def serverlock(session: CommandSession):
    if not await common.token(await common.value(session)):
        result = await seasun.lock(session)
    else:
        result = await common.token(await common.value(session))
    logger.info(result)
    await session.send(result)
