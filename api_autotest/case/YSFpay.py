# coding=utf-8
import unittest,requests,json,time
from common import logger, commons,config
import urllib.parse

class YSFpay(unittest.TestCase):
    def setUp(self):
        self.log = logger.Log()

    # @retry(stop_max_attempt_number=5,wait_fixed=2000)
    def YSFpay(self):
        try:
            self.log.info("--------test is begin--------")
            # 获取登录token
            r = commons.database(config.database, "'登录'")
            token = commons.get_token(r)
            # 构造请求参数
            rs = commons.database(config.database, "'银联云闪付存款'")
            url = str(rs[0][1]).split(';')
            print(type(rs[0][2]), rs[0][2])
            body = urllib.parse.urlencode(eval(rs[0][2]))
            print(url)
            print(body)
            url_pay = config.h5_url + url[0]
            headers = eval(rs[0][4])
            headers.update({
                "X-API-TOKEN": token
            })
            self.log.info("存款请求url:{}".format(url_pay))
            self.log.info("存款请求数据:{}".format(body))
            self.log.info("存款请求header:{}".format(headers))
            #提交存款
            re = requests.post(url=url_pay, data=body, headers=headers).json()
            self.log.info("存款请求结果:{}".format(re))
            assert 6000 == re['status_code']
            #查询存款订单状态
            # url_getnum =

            self.log.info("--------test is pass--------")
        except Exception as e:
            self.log.error("错误的参数:{}".format(e))
            raise
        self.log.info("----------end----------")
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()