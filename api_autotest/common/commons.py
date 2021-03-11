#coding=utf-8
import sqlite3
import requests
import json
from common import config,logger

def get_token(result):
    """
    获取登录token
    :param r: 查询结果集
    :return:token
    """
    try:
        url = config.h5_url + str(result[0][1])
        logger.Log().info("登录url:{}".format(url))
        headers = eval(result[0][4])
        logger.Log().info("登录header:{}".format(headers))
        body = eval(result[0][2])
        logger.Log().info("登录body:{}".format(body))
        re = requests.post(url=url, headers=headers, data=json.dumps(body)).json()
        logger.Log().info("登录结果:{}".format(re))
        return re['data']['token']
    except Exception as e:
        logger.Log().info("登录异常:{}".format(e))
        raise


def database(database, scenes):
    """
    数据库查询数据
    :param database:数据库文件路径
    :param scenes:场景名称
    :return:查询结果集
    """
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        sql = "SELECT * FROM testscenes WHERE scenes=" + scenes + ';'
        cur.execute(sql)
        result = cur.fetchall()
        conn.close()
        return result
    except Exception as e:
        logger.Log.info("数据库异常:{}".format(e))
        raise

if __name__ == '__main__':
    result = database(config.database, "'登录'")
    respones = get_token(result)
    logger.Log().info("获取token成功 :{}".format(respones))