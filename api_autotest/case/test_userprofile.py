# coding=utf-8
import unittest,requests,json,time
from common import logger, commons,config


class Userprofile(unittest.TestCase):
    def setUp(self):
        self.log = logger.Log()

    # @retry(stop_max_attempt_number=5,wait_fixed=2000)
    def test_userprofile(self):
        self.log.info("--------test is begin--------")
        try:
            # 获取登录token
            r = commons.database(config.database, "'登录'")
            token = commons.get_token(r)
            # 构造请求参数
            rs = commons.database(config.database, "'获取、设置用户头像'")
            url = str(rs[0][1]).split(';')
            headers = eval(rs[0][4])
            headers.update({
                "X-API-TOKEN": token
            })
            # 获取用户头像
            url_getdefaultuserprofile = config.h5_url + url[0]
            self.log.info("获取用户头像请求url:{}".format(url_getdefaultuserprofile))
            self.log.info("获取用户头像请求header:{}".format(headers))
            re_getdefaultuserprofile = requests.post(url=url_getdefaultuserprofile, headers=headers).json()
            self.log.info("获取用户头像请求结果:{}".format(re_getdefaultuserprofile))
            assert 6000 == re_getdefaultuserprofile['status_code']
            #设置用户头像
            url_setuserprofile = config.h5_url + url[1]
            headers.update({
                "Content-Length": "23"
            })
            body = rs[0][2]
            self.log.info("设置用户头像请求url:{}".format(url_setuserprofile))
            self.log.info("设置用户头像请求header:{}".format(headers))
            self.log.info("设置用户头像请求body:{}".format(body))
            re_setuserprofile = requests.post(url=url_setuserprofile, data=eval(body), headers=headers).json()
            self.log.info("设置用户头像请求结果:{}".format(re_setuserprofile))
            assert 6000 == re_setuserprofile['status_code']
            self.log.info("--------test is pass--------")
        except Exception as e:
            self.log.error("错误的参数:{}".format(e))
            raise
        self.log.info("----------end----------")
        time.sleep(5)

if __name__ == "__main__":
    unittest.main()
