# -*- coding: utf-8 -*

"""
@Software : PyCharm
@File : content.py
@Author : 梦影
@Time : 2021/04/26 20:21:20
"""

from plugin.common import bot, submit, static, common
from plugin.content.config import extend
import datetime
import time


class seasun:
    @staticmethod
    async def content(session):
        data = await extend.select(await common.value(session))
        if await extend.local(data, 1001) <= await extend.local(data, 1080):
            content = await common.subtext(session)
            if not content:
                server = await static.data(0, data)
            else:
                server = await static.data(1, content[0])
            data = await submit.connect(url=f"{bot.domain}/app/getdaily", data={"server": server})
            if data['code'] == 200:
                dayDraw, data, result = "", data['data'], ""
                if 'DayDraw' in data.keys():
                    dayDraw = f"美人画像：{data['DayDraw']}\n"
                dayList = {
                    "一": f"帮会跑商：阴山商路(10:00)\n阵营祭天：出征祭祀(19:00)\n",
                    "二": f"阵营攻防：逐鹿中原(20:00)\n",
                    "三": f"世界首领：少林·乱世,七秀·乱世(20:00)\n{dayDraw}",
                    "四": f"阵营攻防：逐鹿中原(20:00)\n",
                    "五": f"世界首领：藏剑·乱世,万花·乱世(20:00)\n{dayDraw}",
                    "六": f"攻防前置：南屏山(12:00)\n阵营攻防：浩气盟(13:00,19:00)\n{dayDraw}",
                    "日": f"攻防前置：昆仑(12:00)\n阵营攻防：恶人谷(13:00,19:00)\n{dayDraw}",
                }
                result = f"当前时间：{time.strftime('%Y年%m月%d日', time.localtime())} {await extend.week(datetime.datetime.now())}\n秘境大战：{data['DayWar']}\n今日战场：{data['DayBattle']}\n公共任务：{data['DayCommon']}\n阵营任务：{data['DayCamp']}\n{dayList[data['Week']]}\n武林通鉴·公共任务\n{data['WeekCommon']}\n武林通鉴·秘境任务\n{data['WeekFive']}\n武林通鉴·团队秘境\n{data['WeekTeam']}"
                await extend.update(await common.value(session), 1001, 30)
            else:
                result = "找不到相关信息！"
        else:
            result = await extend.count(await extend.local(data, 1001))
        return result

    @staticmethod
    async def status(session):
        data = await extend.select(await common.value(session))
        if await extend.local(data, 1002) <= await extend.local(data, 1080):
            content = await common.subtext(session)
            if not content:
                server = await static.data(0, data)
            else:
                server = await static.data(1, content[0])
            if not server:
                return "请输入正确的服务器！"
            result = await common.table('status', 'server', server, 'status')
            status = {1: '已开服', 0: '维护中'}
            result = f"{server} 在 {time.strftime('%H:%M:%S', time.localtime(time.time()))} 的状态 [{status[result]}]"
            await extend.update(await common.value(session), 1002, 30)
        else:
            result = await extend.count(await extend.local(data, 1002))
        return result

    @staticmethod
    async def gold(session):
        data = await extend.select(await common.value(session))
        content = await common.subtext(session)
        if not content:
            server = await static.data(0, data)
        else:
            server = await static.data(1, content[0])
        if not server:
            return "请输入正确的服务器！"
        if await extend.local(data, 1003) <= await extend.local(data, 1080):
            data = await submit.connect(url=f"{bot.domain}/app/getgold", data={"server": server})
            if data['code'] == 200:
                wanbaolou = data['data']['wanbaolou']
                dd373 = data['data']['dd373']
                uu898 = data['data']['uu898']
                s7881 = data['data']['7881']
                result = f"金价·{'%-5s' % server} {time.strftime('%m-%d %H:%M', time.localtime(time.time()))}\n官方平台：1元 = {wanbaolou}金\n嘟嘟平台：1元 = {dd373}金\n悠悠平台：1元 = {uu898}金\n其他平台：1元 = {s7881}金 "
                await extend.update(await common.value(session), 1003, 30)
            else:
                result = "找不到相关信息！"
        else:
            result = await extend.count(await extend.local(data, 1003))
        return result

    @staticmethod
    async def flower(session):
        data = await extend.select(await common.value(session))
        content = await common.subtext(session)
        if not content:
            return 'https://jx3api.com/php/flower.php'
        if len(content) == 1:
            server = await static.data(0, data)
            flower = await static.data(2, content[0])
        else:
            server = await static.data(1, content[0])
            flower = await static.data(2, content[1])
        if not server:
            return "请输入正确的服务器！"
        if not flower:
            return "请输入正确的关键字！"
        if await extend.local(data, 1004) <= await extend.local(data, 1080):
            data = await submit.connect(url=f"{bot.domain}/app/getflower", data={"server": server, "flower": flower})
            if data['code'] == 200:
                data = data['data']
                region_result = ""
                for region in data:
                    region_list = data[region]
                    level_result = ""
                    for i in region_list:
                        if 'color' in i:
                            level_result += f"{i['name']}({i['color']})\n倍率:{i['price']}({','.join(i['line'])})\n"
                        else:
                            level_result += f"{i['name']}\n倍率:{i['price']}({','.join(i['line'])})\n"
                    region_result += f"{region}\n{level_result.strip()}\n"
                result = f"{server}·{flower}\n{region_result.strip()}"
                await extend.update(await common.value(session), 1004, 30)
            else:
                result = f"{flower} 的数据收集中..."
        else:
            result = await extend.count(await extend.local(data, 1004))
        return result

    @staticmethod
    async def sand(session):
        data = await extend.select(await common.value(session))
        content = await common.subtext(session)
        if not content:
            server = await static.data(0, data)
        else:
            server = await static.data(1, content[0])
        if not server:
            return "请输入正确的服务器！"
        if await extend.local(data, 1005) <= await extend.local(data, 1080):
            data = await submit.connect(url=f"{bot.domain}/app/getSand", data={"server": server})
            if data['code'] == 200:
                data = data['data']
                result = f"[CQ:image,file={data['url']},cache=false]"
                await extend.update(await common.value(session), 1005, 30)
            else:
                result = "找不到相关信息！"
        else:
            result = await extend.count(await extend.local(data, 1005))
        return result

    @staticmethod
    async def pve(session):
        data = await extend.select(await common.value(session))
        content = await common.subtext(session)
        if not content:
            return "请输入关键字！"
        name = await static.data(3, content[0])
        if not name:
            return "请输入正确的关键字！"
        if '×' in name:
            text = name.split('×')
            return f"{content[0]}·[PVE {text[0]}丨PVE {text[1]}]"
        if await extend.local(data, 1006) <= await extend.local(data, 1080):
            data = await submit.connect(url=f"{bot.domain}/app/getequipment",
                                        data={'name': name, 'user': session.self_id})
            if data['code'] == 200:
                result = f"[CQ:image,file={data['data']['pve']},cache=false]"
                await extend.update(await common.value(session), 1006, 30)
            else:
                result = "找不到相关信息！"
        else:
            result = await extend.count(await extend.local(data, 1006))
        return result

    @staticmethod
    async def pvp(session):
        data = await extend.select(await common.value(session))
        content = await common.subtext(session)
        if not content:
            return "请输入关键字！"
        name = await static.data(3, content[0])
        if not name:
            return "请输入正确的关键字！"
        if '×' in name:
            text = name.split('×')
            return f"{content[0]}·[PVP {text[0]}丨PVP {text[1]}]"
        if await extend.local(data, 1007) <= await extend.local(data, 1080):
            data = await submit.connect(url=f"{bot.domain}/app/getequipment",
                                        data={'name': name, 'user': session.self_id})
            if data['code'] == 200:
                result = f"[CQ:image,file={data['data']['pvp']},cache=false]"
                await extend.update(await common.value(session), 1007, 30)
            else:
                result = "找不到相关信息！"
        else:
            result = await extend.count(await extend.local(data, 1007))
        return result

    @staticmethod
    async def plan(session):
        data = await extend.select(await common.value(session))
        content = await common.subtext(session)
        if not content:
            return "请输入关键字！"
        name = await static.data(3, content[0])
        if not name:
            return "请输入正确的关键字！"
        if '×' in name:
            text = name.split('×')
            return f"{content[0]}·[绝境 {text[0]}丨绝境 {text[1]}]"
        if await extend.local(data, 1008) <= await extend.local(data, 1080):
            data = await submit.connect(url=f"{bot.domain}/app/getholes", data={'name': name})
            if data['code'] == 200:
                result = f"龙门绝境·推荐奇穴\n{data['data']['Despair']}"
                await extend.update(await common.value(session), 1008, 30)
            else:
                result = "找不到相关信息！"
        else:
            result = await extend.count(await extend.local(data, 1008))
        return result

    @staticmethod
    async def battle(session):
        data = await extend.select(await common.value(session))
        content = await common.subtext(session)
        if not content:
            return "请输入关键字！"
        name = await static.data(3, content[0])
        if not name:
            return "请输入正确的关键字！"
        if '×' in name:
            text = name.split('×')
            return f"{content[0]}·[绝境 {text[0]}丨绝境 {text[1]}]"
        if await extend.local(data, 1009) <= await extend.local(data, 1080):
            data = await submit.connect(url=f"{bot.domain}/app/getHoles", data={'name': name})
            if data['code'] == 200:
                result = f"战场任务·推荐奇穴\n{data['data']['Battle']}"
                await extend.update(await common.value(session), 1009, 30)
            else:
                result = "找不到相关信息！"
        else:
            result = await extend.count(await extend.local(data, 1009))
        return result

    @staticmethod
    async def heighten(session):
        data = await extend.select(await common.value(session))
        content = await common.subtext(session)
        if not content:
            return "[CQ:image,file=https://oss.nicemoe.cn/content/reinforcement/reinforcement.jpg,cache=false]"
        name = await static.data(3, content[0])
        if not name:
            return "请输入正确的关键字！"
        if '×' in name:
            text = name.split('×')
            return f"{content[0]}·[小药 {text[0]}丨小药 {text[1]}]"
        if await extend.local(data, 1010) <= await extend.local(data, 1080):
            data = await submit.connect(url=f"{bot.domain}/app/getheighten", data={'name': name})
            if data['code'] == 200:
                result = f"{name}·推荐药品\n增强食品:{data['data']['HeightenFood']}\n辅助食品:{data['data']['AuxiliaryFood']}\n增强药品:{data['data']['HeightenDrug']}\n辅助药品:{data['data']['AuxiliaryDrug']}"
                await extend.update(await common.value(session), 1010, 30)
            else:
                result = "找不到相关信息！"
        else:
            result = await extend.count(await extend.local(data, 1010))
        return result

    @staticmethod
    async def macro(session):
        data = await extend.select(await common.value(session))
        content = await common.subtext(session)
        if not content:
            return "请输入关键字！"
        name = await static.data(3, content[0])
        if not name:
            return "请输入正确的关键字！"
        if '×' in name:
            text = name.split('×')
            return f"{content[0]}·[宏 {text[0]}丨宏 {text[1]}]"
        if await extend.local(data, 1011) <= await extend.local(data, 1080):
            result = await submit.connect(url=f"{bot.domain}/app/getmacro", data={'name': name})
            await extend.update(await common.value(session), 1011, 30)
        else:
            result = await extend.count(await extend.local(data, 1011))
        return result

    @staticmethod
    async def macros(event):
        data = await extend.select(event['group_id'])
        content = str(event['message'])[:-1].strip()
        if not content:
            return "请输入关键字！"
        name = await static.data(3, content)
        if not name:
            return "请输入正确的关键字！"
        if '×' in name:
            text = name.split('×')
            return f"{content}·[{text[0]}宏丨{text[1]}宏]"
        if await extend.local(data, 1011) <= await extend.local(data, 1080):
            result = await submit.connect(url=f"{bot.domain}/app/getmacro", data={'name': name})
            await extend.update(event['group_id'], 1011, 30)
        else:
            result = await extend.count(await extend.local(data, 1011))
        return result

    @staticmethod
    async def prices(session):
        data = await extend.select(await common.value(session))
        content = await common.subtext(session)
        if not content:
            return "请输入关键字！"
        if await extend.local(data, 1012) <= await extend.local(data, 1080):
            data = await submit.connect(url=f"{bot.domain}/app/getprice", data={'name': content[0]})
            if data['code'] == 200:
                result, data = "", data['data'][0]
                for each in data[:5]:
                    itemtime = f"20{each['tradeTime'].replace('/', '-')}"
                    price, itemname, saleCode, = each['price'], each['itemname'], each['saleCode']
                    saleCode = '收'
                    if '出' in saleCode:
                        saleCode = '出'
                    exterior = f"{each['exterior']}·{itemname}"
                    result += f"{itemtime} 有人 {price:.0f} {saleCode}了 {exterior}\n"
                result = result.strip()
                await extend.update(await common.value(session), 1012, 30)
            else:
                result = "请输入正确的关键字！"
        else:
            result = await extend.count(await extend.local(data, 1012))
        return result

    @staticmethod
    async def price(session):
        data = await extend.select(await common.value(session))
        content = await common.subtext(session)
        if not content:
            return "请输入关键字！"
        if await extend.local(data, 1013) <= await extend.local(data, 1080):
            data = await submit.content(
                url=f"https://m.dololo.top/getAllItem/bjsj/0/2019-11-29/1/{content[0]}/x/x/x/x/x/0")
            data = data['content']
            result = ""
            if len(data) > 0:
                for each in data[:5]:
                    date, price, buyer, itemname = each['bjsj'], each['jg'], each['lx'], each['wpqc']
                    result += f"{date} 有人 {price:.0f} {buyer} {itemname}\n"
                result = result.strip()
                await extend.update(await common.value(session), 1013, 30)
            else:
                result = "请输入正确的关键字！"
        else:
            result = await extend.count(await extend.local(data, 1013))
        return result

    @staticmethod
    async def method(session):
        data = await extend.select(await common.value(session))
        content = await common.subtext(session)
        if not content:
            return "请输入关键字！"
        if await extend.local(data, 1014) <= await extend.local(data, 1080):
            data = await submit.connect(url=f"{bot.domain}/app/getmethod", data={'name': content[0]})
            if data['code'] == 200:
                data = data['data']
                result = f"{content[0]}·前置条件\n触发方式:{data['method']}\n满足条件:{data['need']}\n其他可能:{data['other']}\n物品奖励:{data['reward']}"
                await extend.update(await common.value(session), 1014, 30)
            else:
                result = "请输入正确的关键字！"
        else:
            result = await extend.count(await extend.local(data, 1014))
        return result

    @staticmethod
    async def achievement(session):
        data = await extend.select(await common.value(session))
        content = await common.subtext(session)
        if not content:
            return "请输入关键字！"
        name = content[0].replace('[', '').replace(']', '')
        if await extend.local(data, 1015) <= await extend.local(data, 1080):
            data = await submit.content(url="https://helper.jx3box.com/api/achievement/search",
                                        params={'keyword': name})
            data = data['data']['achievements']
            if len(data) > 0:
                item = data[0]['ID']
                result = f"[{data[0]['Name']}]·对应地址:https://jx3api.com/api/jump.php?id={item}"
                await extend.update(await common.value(session), 1015, 30)
            else:
                result = "请输入正确的关键字！"
        else:
            result = await extend.count(await extend.local(data, 1015))
        return result

    @staticmethod
    async def exam(session):
        data = await extend.select(await common.value(session))
        content = await common.subtext(session)
        if not content:
            return "请输入关键字！"
        question = content[0]
        if await extend.local(data, 1016) <= await extend.local(data, 1080):
            data = await submit.connect(url=f"{bot.domain}/app/getexam", data={'question': question})
            if data['code'] == 200:
                result = ""
                data = data['data']
                for i in range(min(2, len(data))):
                    result += "Q：{}\nA：{}\n\n".format(data[i]['question'], data[i]['answer'])
                result = f"{result.strip()}\n还有（{len(data) - 2}）项，输入更多关键词以便精准查找..."
                await extend.update(await common.value(session), 1016, 10)
            else:
                result = "请输入正确的关键字！"
        else:
            result = await extend.count(await extend.local(data, 1016))
        return result

    @staticmethod
    async def travel(session):
        data = await extend.select(await common.value(session))
        content = await common.subtext(session)
        if not content:
            return "请输入关键字！"
        name = content[0]
        if await extend.local(data, 1017) <= await extend.local(data, 1080):
            data = await submit.connect(url=f'{bot.domain}/app/gettravel', data={'map': name})
            if data['code'] == 200:
                data = data['data']
                result = f"[CQ:image,file={data[0]['imagePath']}]\n家具 : {data[0]['name']}\n品质 : {data[0]['qualityLevel']}\n需要家园等级 : {data[0]['levelLimit']}\n风水评分 : {data[0]['geomanticScore']}\n观赏评分 : {data[0]['viewScore']}\n实用评分 : {data[0]['practicalScore']}\n坚固评分 : {data[0]['hardScore']}\n趣味评分 : {data[0]['interestingScore']}"
                await extend.update(await common.value(session), 1017, 30)
            else:
                result = "请输入正确的关键字！"
        else:
            result = await extend.count(await extend.local(data, 1017))
        return result

    @staticmethod
    async def furniture(session):
        data = await extend.select(await common.value(session))
        content = await common.subtext(session)
        if not content:
            return "请输入关键字！"
        if await extend.local(data, 1018) <= await extend.local(data, 1080):
            data = await submit.connect(url=f"{bot.domain}/app/getfurniture", data={'name': content[0]})
            if data['code'] == 200:
                data = data['data']
                result = f"装饰属性·{content[0]}\n[CQ:image,file={data['imagePath']}]\n来源 : {data['source']}\n品质 : {data['qualityLevel']}\n价格 : {data['architecture']}\n需要家园等级 : {data['levelLimit']}\n风水评分 : {data['geomanticScore']}\n观赏评分 : {data['viewScore']}\n实用评分 : {data['practicalScore']}\n坚固评分 : {data['hardScore']}\n趣味评分 : {data['interestingScore']}"
                await extend.update(await common.value(session), 1018, 30)
            else:
                result = '请输入正确的关键字！'
        else:
            result = await extend.count(await extend.local(data, 1018))
        return result

    @staticmethod
    async def announcement(session):
        data = await extend.select(await common.value(session))
        if await extend.local(data, 1019) <= await extend.local(data, 1080):
            data = await submit.connect(url=f"{bot.domain}/app/getannounce")
            if data['code'] == 200:
                data = data['data']
                result = ""
                for each in data[:3]:
                    result += f"标题：{each['title']}\n链接：{each['url']}\n\n"
                result = result.strip()
                await extend.update(await common.value(session), 1019, 30)
            else:
                result = "找不到相关信息！"
        else:
            result = await extend.count(await extend.local(data, 1019))
        return result

    @staticmethod
    async def adventure(session):
        data = await extend.select(await common.value(session))
        content = await common.subtext(session)
        if not content:
            return "请输入关键字！"
        if len(content) == 1:
            server = await static.data(0, data)
            advent = await static.data(4, content[0])
        else:
            server = await static.data(1, content[0])
            advent = await static.data(4, content[1])
        if not server:
            return "请输入正确的服务器！"
        if not advent:
            return "请输入正确的关键字！"
        if await extend.local(data, 1020) <= await extend.local(data, 1080):
            data = await submit.connect(url=f"{bot.domain}/app/getserendipity",
                                        data={'server': server, 'serendipity': advent})
            if data['code'] == 200:
                result = ""
                for each in data['data'][:5]:
                    timeArray = time.localtime(each['time'])
                    otherStyleTime = time.strftime("%m月%d日 %H:%M", timeArray)
                    result += f"\n————————————————\n玩家：{each['name']} \n时间：{otherStyleTime}"
                result = f"[{server}·{advent}]{result}"
                await extend.update(await common.value(session), 1020, 30)
            else:
                result = "找不到相关信息！"
        else:
            result = await extend.count(await extend.local(data, 1020))
        return result

    @staticmethod
    async def personal(session):
        data = await extend.select(await common.value(session))
        content = await common.subtext(session)
        if not content:
            return "请输入关键字！"
        if len(content) == 1:
            server = await static.data(0, data)
            name = content[0]
        else:
            server = await static.data(1, content[0])
            name = content[1]
        if not server:
            return "请输入正确的服务器！"
        if not name:
            return "请输入正确的关键字！"
        if await extend.local(data, 1021) <= await extend.local(data, 1080):
            data = await submit.connect(url=f"{bot.domain}/app/getserendipity", data={'server': server, 'name': name})
            if data['code'] == 200:
                result = ""
                data = data['data']
                for i in range(len(data)):
                    timeArray = time.localtime(data[i]['time'])
                    otherStyleTime = time.strftime("%m月%d日 %H:%M", timeArray)
                    if await static.data(4, data[i]['serendipity']):
                        result += f"\n————————————————\n奇遇：{data[i]['serendipity']} \n时间：{otherStyleTime}"
                result = f"[{server}·{name}]{result}"
                await extend.update(await common.value(session), 1021, 30)
            else:
                result = "找不到相关信息！"
        else:
            result = await extend.count(await extend.local(data, 1021))
        return result

    @staticmethod
    async def music(session):
        data = await extend.select(await common.value(session))
        content = await common.subtext(session)
        if not content:
            return "请输入关键字！"
        if await extend.local(data, 1022) <= await extend.local(data, 1080):
            params = {'format': 'json', 'w': content[0]}
            data = await submit.content(url='https://c.y.qq.com/soso/fcgi-bin/client_search_cp', params=params)
            result = f"[CQ:music,type=qq,id={data['data']['song']['list'][0]['songid']},content={data['data']['song']['list'][0]['singer'][0]['name']} <{list(bot.config.NICKNAME)[0]}>]"
            await extend.update(await common.value(session), 1022, 30)
        else:
            result = await extend.count(await extend.local(data, 1022))
        return result

    @staticmethod
    async def netease(session):
        data = await extend.select(await common.value(session))
        content = await common.subtext(session)
        if not content:
            return "请输入关键字！"
        if await extend.local(data, 1023) <= await extend.local(data, 1080):
            data = await submit.connect(url="http://music.163.com/api/search/pc", data={'s': content[0], 'type': 1})
            result = f"[CQ:music,type=163,id={data['result']['songs'][0]['id']}]"
            await extend.update(await common.value(session), 1023, 30)
        else:
            result = await extend.count(await extend.local(data, 1023))
        return result

    @staticmethod
    async def world(session):
        data = await extend.select(await common.value(session))
        if await extend.local(data, 1024) <= await extend.local(data, 1080):
            data = await submit.connect(url=f"{bot.domain}/app/getrandom")
            if data['code'] == 200:
                result = data['data']['text']
                await extend.update(await common.value(session), 1024, 15)
            else:
                result = "找不到相关信息！"
        else:
            result = await extend.count(await extend.local(data, 1024))
        return result

    @staticmethod
    async def gest(session):
        data = await extend.select(await common.value(session))
        content = await common.subtext(session)
        if not content:
            return "请输入关键字！"
        name = await static.data(3, content[0])
        if not name:
            return "请输入正确的关键字！"
        if '×' in name:
            text = name.split('×')
            return f"{content[0]}·[阵眼 {text[0]}丨阵眼 {text[1]}]"
        if await extend.local(data, 1025) <= await extend.local(data, 1080):
            data = await submit.connect(url=f"{bot.domain}/app/getgest", data={'name': name})
            if data['code'] == 200:
                result = f"{data['data']['name']}·{data['data']['skillName']}"
                temp = ""
                for data in data['data']['descs']:
                    temp += f"{data['name']}:{data['desc']}\n"
                result = f"{result}\n{temp.strip()}"
                await extend.update(await common.value(session), 1025, 30)
            else:
                result = "找不到相关信息！"
        else:
            result = await extend.count(await extend.local(data, 1025))
        return result

    @staticmethod
    async def pendant(session):
        data = await extend.select(await common.value(session))
        content = await common.subtext(session)
        if not content:
            return "请输入关键字！"
        if await extend.local(data, 1026) <= await extend.local(data, 1080):
            data = await submit.connect(url=f"{bot.domain}/app/getPendant", data={'name': content[0]})
            if data['code'] == 200:
                data = data['data']
                result = f"挂件详情·{data['Name']}\n挂件类型：{data['Type']}\n使用特效：{data['Use']}\n挂件说明：{data['Explain']}\n挂件出自：{data['Obtain']}"
                await extend.update(await common.value(session), 1026, 30)
            else:
                result = "找不到相关信息！"
        else:
            result = await extend.count(await extend.local(data, 1026))
        return result

    @staticmethod
    async def dog(session):
        data = await extend.select(await common.value(session))
        if await extend.local(data, 1029) <= await extend.local(data, 1080):
            data = await submit.connect(url=f"{bot.domain}/extend/getdog")
            if data['code'] == 200:
                result = data['data']['text']
                await extend.update(await common.value(session), 1029, 10)
            else:
                result = "找不到相关信息！"
        else:
            result = await extend.count(await extend.local(data, 1029))
        return result

    @staticmethod
    async def explain(session):
        data = await extend.select(await common.value(session))
        if await extend.local(data, 1048) <= await extend.local(data, 1080):
            result = bot.config.EXPLAIN_URL
            await extend.update(await common.value(session), 1049, 30)
        else:
            result = await extend.count(await extend.local(data, 1049))
        return result

    @staticmethod
    async def lock(session):
        data = await extend.select(await common.value(session))
        content = await common.subtext(session)
        if not content:
            return "请输入服务器！"
        else:
            server = await static.data(1, content[0])
        if not server:
            return "请输入正确的服务器！"
        if await extend.local(data, 1050) <= await extend.local(data, 1080):
            await extend.lock(server, await common.value(session))
            await extend.update(await common.value(session), 1050, 86400)
            result = f"{server}  绑定完成！"
        else:
            result = await extend.count(await extend.local(data, 1050))
        return result
