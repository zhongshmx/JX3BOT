# -*- coding: utf-8 -*

"""
@Software : PyCharm
@File : database.py
@Author : 梦影
@Time : 2021/04/25 19:29:28
"""

import traceback
import aiomysql
from nonebot.log import logger


class MySql:
    def __init__(self):
        self.coon = None
        self.pool = None

    async def initpool(self, bot):
        try:
            logger.debug("mysql will connect mysql~")
            __pool = await aiomysql.create_pool(**bot.MYSQL_CONFIG)
            return __pool
        except:
            logger.error('mysql connect error.', exc_info=True)

    async def getCurosr(self):
        conn = await self.pool.acquire()
        # 返回字典格式
        cur = await conn.cursor(aiomysql.DictCursor)
        return conn, cur

    async def query(self, query, param=None):
        """
        查询操作
        :param query: sql语句
        :param param: 参数
        :return:
        """
        conn, cur = await self.getCurosr()
        try:
            await cur.execute(query, param)
            return await cur.fetchall()
        except:
            logger.error(traceback.format_exc())
        finally:
            if cur:
                await cur.close()
            # 释放掉conn,将连接放回到连接池中
            await self.pool.release(conn)

    async def execute(self, query, param=None):
        """
        增删改 操作
        :param query: sql语句
        :param param: 参数
        :return:
        """
        conn, cur = await self.getCurosr()
        try:
            await cur.execute(query, param)
            if cur.rowcount == 0:
                return False
            else:
                return True
        except:
            logger.error(traceback.format_exc())
        finally:
            if cur:
                await cur.close()
            # 释放掉conn,将连接放回到连接池中
            await self.pool.release(conn)


async def MySqlInit(bot, socketList):  # 数据库初始化
    table = {
        "main": "CREATE TABLE  `main`(`ID`  INT(12) NOT NULL AUTO_INCREMENT PRIMARY KEY, `Value` BIGINT(20) NOT NULL UNIQUE, `Main` VARCHAR(20), `Relet` BIGINT(20), `Users` BIGINT(20), `Robot` BIGINT(20), `CD.1001` BIGINT(20) DEFAULT 0, `CD.1002` BIGINT(20) DEFAULT 0, `CD.1003` BIGINT(20) DEFAULT 0, `CD.1004` BIGINT(20) DEFAULT 0, `CD.1005` BIGINT(20) DEFAULT 0, `CD.1006` BIGINT(20) DEFAULT 0, `CD.1007` BIGINT(20) DEFAULT 0, `CD.1008` BIGINT(20) DEFAULT 0, `CD.1009` BIGINT(20) DEFAULT 0, `CD.1010` BIGINT(20) DEFAULT 0, `CD.1011` BIGINT(20) DEFAULT 0, `CD.1012` BIGINT(20) DEFAULT 0, `CD.1013` BIGINT(20) DEFAULT 0, `CD.1014` BIGINT(20) DEFAULT 0,`CD.1015` BIGINT(20) DEFAULT 0, `CD.1016` BIGINT(20) DEFAULT 0, `CD.1017` BIGINT(20) DEFAULT 0, `CD.1018` BIGINT(20) DEFAULT 0, `CD.1019` BIGINT(20) DEFAULT 0, `CD.1020` BIGINT(20) DEFAULT 0, `CD.1021` BIGINT(20) DEFAULT 0, `CD.1022` BIGINT(20) DEFAULT 0, `CD.1023` BIGINT(20) DEFAULT 0, `CD.1024` BIGINT(20) DEFAULT 0, `CD.1025` BIGINT(20) DEFAULT 0, `CD.1026` BIGINT(20) DEFAULT 0, `CD.1027` BIGINT(20) DEFAULT 0, `CD.1028` BIGINT(20) DEFAULT 0, `CD.1029` BIGINT(20) DEFAULT 0, `CD.1030` BIGINT(20) DEFAULT 0, `CD.1031` BIGINT(20) DEFAULT 0, `CD.1032` BIGINT(20) DEFAULT 0, `CD.1033` BIGINT(20) DEFAULT 0, `CD.1034` BIGINT(20) DEFAULT 0, `CD.1035` BIGINT(20) DEFAULT 0, `CD.1036` BIGINT(20) DEFAULT 0, `CD.1037` BIGINT(20) DEFAULT 0, `CD.1038` BIGINT(20) DEFAULT 0, `CD.1039` BIGINT(20) DEFAULT 0, `CD.1040` BIGINT(20) DEFAULT 0, `CD.1041` BIGINT(20) DEFAULT 0, `CD.1042` BIGINT(20) DEFAULT 0, `CD.1043` BIGINT(20) DEFAULT 0, `CD.1044` BIGINT(20) DEFAULT 0, `CD.1045` BIGINT(20) DEFAULT 0, `CD.1046` BIGINT(20) DEFAULT 0, `CD.1047` BIGINT(20) DEFAULT 0, `CD.1048` BIGINT(20) DEFAULT 0, `CD.1049` BIGINT(20) DEFAULT 0, `CD.1050` BIGINT(20) DEFAULT 0)",
        "status": "CREATE TABLE  `status`(`id`  INT(12) NOT NULL AUTO_INCREMENT PRIMARY KEY, `server` VARCHAR(20) NOT NULL, `status` INT(12) NOT NULL DEFAULT 1)",
        "switch": "CREATE TABLE  `switch`(`id` INT(12) NOT NULL AUTO_INCREMENT PRIMARY KEY, `value` BIGINT(20) NOT NULL UNIQUE, `random` BIGINT(20) DEFAULT 0, `news` BIGINT(20) DEFAULT 0, `nlpchat` BIGINT(20) DEFAULT 0, `scheduler` BIGINT(20) DEFAULT 0, `member` VARCHAR(255))",
    }
    for n in table:
        sql = f"SHOW TABLES LIKE '%{n}%'"
        if await bot.client.query(sql):
            continue
        await bot.client.execute(table[n])
        logger.critical(f"MySQL > 创建数据表[{n}]成功！")
    for i in socketList:
        sql = "SELECT * FROM `status` WHERE `server` = %s"
        if await bot.client.query(sql, i):
            continue
        sql = "INSERT INTO `status`(`server`) VALUES (%s)"
        await bot.client.execute(sql, i)
        logger.critical(f"MySQL > 插入数据值[{i}]成功！")
