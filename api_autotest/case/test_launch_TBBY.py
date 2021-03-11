# coding=utf-8
import unittest,requests,json,time
from common import logger, commons,config


class Launch_TBBY(unittest.TestCase):
    def setUp(self):
        self.log = logger.Log()

    # @retry(stop_max_attempt_number=5,wait_fixed=2000)
    def test_launch_TBBY(self):
        self.log.info("--------test is begin--------")
        try:
            # 获取登录token
            r = commons.database(config.database, "'登录'")
            token = commons.get_token(r)
            # 构造请求参数
            rs = commons.database(config.database, "'天博捕鱼场馆加载'")
            url = config.h5_url + rs[0][1]
            body = rs[0][2]
            headers = eval(rs[0][4])
            headers.update({
                "X-API-TOKEN": token
            })
            self.log.info("请求url:{}".format(url))
            self.log.info("请求body:{}".format(body))
            self.log.info("请求header:{}".format(headers))
            re = requests.post(url=url, data=body, headers=headers).json()
            self.log.info("请求结果:{}".format(re))
            assert 6000 == re['status_code']
            self.log.info("--------test is pass--------")
        except Exception as e:
            self.log.error("错误的参数:{}".format(e))
            raise
        self.log.info("----------end----------")
        time.sleep(5)

if __name__ == "__main__":
    unittest.main()
