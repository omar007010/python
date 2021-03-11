# coding=utf-8
import unittest,requests,json,time
from common import logger, commons,config


class Feedback(unittest.TestCase):
    def setUp(self):
        self.log = logger.Log()

    # @retry(stop_max_attempt_number=5,wait_fixed=2000)
    def test_feedback(self):
        self.log.info("--------test is begin--------")
        try:
            # 获取登录token
            r = commons.database(config.database, "'登录'")
            token = commons.get_token(r)
            # 构造请求参数
            rs = commons.database(config.database, "'意见反馈'")
            url = str(rs[0][1]).split(';')
            headers = eval(rs[0][4])
            headers.update({
                "X-API-TOKEN": token
            })
            # 获取反馈列表
            url_feedbacktypelist = config.h5_url + url[0]
            self.log.info("获取反馈列表请求url:{}".format(url_feedbacktypelist))
            self.log.info("获取反馈列表请求header:{}".format(headers))
            re_feedbacktypelist = requests.get(url=url_feedbacktypelist, headers=headers).json()
            self.log.info("获取反馈列表请求结果:{}".format(re_feedbacktypelist))
            assert 6000 == re_feedbacktypelist['status_code']
            #意见反馈
            url_feedback = config.h5_url + url[1]
            headers.update({
                "Content-Length": "610"
            })
            body = rs[0][2]
            self.log.info("意见反馈请求url:{}".format(url_feedback))
            self.log.info("意见反馈请求header:{}".format(headers))
            self.log.info("意见反馈请求body:{}".format(body))
            re_feedback = requests.post(url=url_feedback, data=eval(body), headers=headers).json()
            self.log.info("意见反馈请求结果:{}".format(re_feedback))
            assert 6000 == re_feedback['status_code']
            self.log.info("--------test is pass--------")
        except Exception as e:
            self.log.error("错误的参数:{}".format(e))
            raise
        self.log.info("----------end----------")
        time.sleep(5)

if __name__ == "__main__":
    unittest.main()
