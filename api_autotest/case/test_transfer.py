# coding=utf-8
import unittest,requests,json,time
from common import logger, commons,config


class Transfer(unittest.TestCase):
    def setUp(self):
        self.log = logger.Log()

    # @retry(stop_max_attempt_number=5,wait_fixed=2000)
    def test_transfer(self):
        self.log.info("--------test is begin--------")
        try:
            # 获取登录token
            r = commons.database(config.database, "'登录'")
            token = commons.get_token(r)
            # 构造请求参数
            rs = commons.database(config.database, "'转账'")
            url = str(rs[0][1]).split(';')
            # print(rs[0][1], rs[0][2])
            headers = eval(rs[0][4])
            headers.update({
                "X-API-TOKEN": token
            })
            # 获取全部场馆余额
            url_allbalance = config.h5_url + url[0]
            self.log.info("获取余额请求url:{}".format(url_allbalance))
            self.log.info("获取余额请求header:{}".format(headers))
            re_allbalance = requests.get(url=url_allbalance, headers=headers).json()
            self.log.info("获取余额请求结果:{}".format(re_allbalance))
            assert 6000 == re_allbalance['status_code']
            #一键回收
            url_recycle = config.h5_url + url[1]
            self.log.info("一键回收请求url:{}".format(url_recycle))
            self.log.info("一键回收请求header:{}".format(headers))
            re_recycle = requests.get(url=url_recycle, headers=headers).json()
            self.log.info("一键回收请求结果:{}".format(re_recycle))
            assert 6000 == re_recycle['status_code']
            #转账到天博体育
            url_transfer = config.h5_url + url[2]
            body = rs[0][2]
            self.log.info("转账到天博体育请求url:{}".format(url_transfer))
            self.log.info("转账到天博体育请求header:{}".format(headers))
            self.log.info("转账到天博体育请求参数:{}".format(body))
            re_transfer = requests.post(url=url_transfer, data=body, headers=headers).json()
            self.log.info("转账到天博体育请求结果:{}".format(re_transfer))
            assert 6000 == re_transfer['status_code']
            time.sleep(5)
            re_recycle2 = requests.get(url=url_recycle, headers=headers).json()
            self.log.info("回收用户余额到中心钱包:{}".format(re_recycle2))
            assert 6000 == re_recycle2['status_code']
            self.log.info("--------test is pass--------")
        except Exception as e:
            self.log.error("错误的参数:{}".format(e))
            raise
        self.log.info("----------end----------")
        time.sleep(5)

if __name__ == "__main__":
    unittest.main()
