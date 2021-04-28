# -*- coding: utf-8 -*

"""
@Software : PyCharm
@File : config.py
@Author : 梦影
@Time : 2021/04/25 19:28:51
"""

from nonebot.default_config import *
from datetime import timedelta

HOST = '0.0.0.0'  # NoneBot 的 HTTP 和 WebSocket 服务端监听的 IP／主机名。
PORT = 1888  # NoneBot 的 HTTP 和 WebSocket 服务端监听的端口。
DEBUG = False  # 是否以调试模式运行，生产环境需要设置为 False 以提高性能。
SUPERUSERS = {22282320, 3321056200}  # 超级用户的 QQ 号，用于命令的权限检查。
NICKNAME = {'萌萌'}  # 机器人的昵称，用于辨别用户是否在和机器人说话。
COMMAND_START = {'', '/', '!', '／', '！'}  # 命令的起始标记，用于判断一条消息是不是命令。
ACCESS_TOKEN = ''  # 需要和 CQHTTP 插件的配置中的 access_token 相同。
COMMAND_SEP = {'.'}  # 命令的分隔标记，用于将文本形式的命令切分为元组（实际的命令名）。
SESSION_RUN_TIMEOUT = timedelta(seconds=10)  # 命令会话的运行超时时长，超时后会话将被移除，命令处理函数会被异常所中断。此时用户可以调用新的命令，开启新的会话。None 表示不超时。
SHORT_MESSAGE_MAX_LENGTH = 50  # 短消息的最大长度。默认情况下（only_short_message 为 True），自然语言处理器只会响应消息中纯文本部分的长度总和小于等于此值的消息。
SESSION_RUNNING_EXPRESSION = '很抱歉,有故障惹！'  # 当有命令会话正在运行时，给用户新消息的回复。
ROBOT_LIST = [15853655, 256865536, 1938255364, 536069770]  # 已连接 NoneBot 的机器人 QQ 号，用于主动推送消息。
ROBOT_EXIT_TIME = 7  # 已授权 QQ群 到期后退群时间(天)。
RANDOM_MAX_VALUE = 2  # NoneBot 随机文字(骚话)、语音(骚话) 触发几率。
NLPCHAT_MAX_VALUE = 3  # NoneBot 随机聊天 触发几率。
SMS_PHONE = 18500000000  # BOT掉线后接收短信通知的号码
NLPCHAT_APPID = 1000000000  # 腾讯AI 开放平台 智能闲聊 的 APPID，请勿开启画像，用于智能聊天。（留空可能会报错）
NLPCHAT_APPKEY = ''  # 腾讯AI 开放平台 智能闲聊 的 APPKEY，请勿开启画像，用于智能聊天。（留空可能会报错）
ALIYUN_APPKEY = ''  # 阿里云 智能语音交互 的 APPKEY 用于语音合成（留空可能会报错）
ALIYUN_ACCESS = ''  # 阿里云 智能语音交互 的 ACCESS 用于语音合成（留空可能会报错）
ALIYUN_SECRET = ''  # 阿里云 智能语音交互 的 SECRET 用于语音合成（留空可能会报错）
DATA_DOMAIN = 'https://www.jx3api.com'  # NoneBot 功能数据 API 地址
EXPLAIN_URL = 'https://docs.qq.com/doc/DTEhJTUZNeUJHY2Ni?pub=1&dver=2.1.0'  # 使用说明链接，推荐腾讯在线文档

MYSQL_CONFIG = {  # NoneBot 数据记录配置。
    'host': '127.0.0.1',  # 连接主机名。
    'user': 'root',  # 用户账号
    'password': 'ret.content',  # 用户密码
    'db': 'nonebot',  # 数据库名
    'port': 3306,  # 连接端口
    'charset': 'utf8',  # 数据编码
    'minsize': 10,  # 连接池最小值
    'maxsize': 20,  # 连接池最大值
    'autocommit': True,  # 自动提交模式
}
