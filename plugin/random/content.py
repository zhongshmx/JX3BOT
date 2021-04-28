# -*- coding: utf-8 -*

"""
@Software : PyCharm
@File : content.py
@Author : 梦影
@Time : 2021/04/28 19:56:13
"""

from plugin.common import bot, robot, submit
import random


class seasun:
    @staticmethod
    async def nlpchat(message):
        data = {'question': message, 'appid': bot.config.NLPCHAT_APPID, 'appkey': bot.config.NLPCHAT_APPKEY,
                'name': list(bot.config.NICKNAME)[0]}
        data = await submit.connect(url=f"{bot.domain}/extend/getnlpchat", data=data)
        if data['code'] == 200:
            result = data['data']['answer']
        else:
            result = None
        return result

    @staticmethod
    async def content(message):  # 语音合成中转
        result = await seasun.voice(message)
        if result:
            result = f"[CQ:record,file={result}]"
        else:
            result = "找不到相关信息！"
        return result

    @staticmethod
    async def random(event):
        text = await seasun.text()
        if random.randint(1, 2) == 1:
            return f"{await robot.sender(event)} {text}"
        else:
            result = await seasun.voice(text)
            result = f"[CQ:record,file={result}]"
        return result

    @staticmethod
    async def text():
        data = await submit.connect(url=f"{bot.domain}/app/getrandom")
        if data['code'] == 200:
            return data['data']['text']
        else:
            return None

    @staticmethod
    async def voice(text: str):
        data = {'appkey': bot.config.ALIYUN_APPKEY, 'access': bot.config.ALIYUN_ACCESS,
                'secret': bot.config.ALIYUN_SECRET, 'text': text}
        data = await submit.connect(url=f"{bot.domain}/extend/getaliyun", data=data)
        if data['code'] == 200:
            return data['data']['url']
        else:
            return None
