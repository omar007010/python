#coding=utf-8
import unittest
import os
import time
from common import HTMLTestRunner2,logger


# 当前脚本所在文件真实路径
cur_path = os.path.dirname(os.path.abspath(__file__))

def add_case(caseName="case", rule="test*.py"):
    '''第一步：加载所有的测试用例'''
    case_path = os.path.join(cur_path, caseName)  # 用例文件夹
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path, pattern=rule, top_level_dir=None)
    return discover


def run_case(all_case, reportName="report"):
    '''第二步：执行所有的用例，并把结果写入HTML测试报告'''
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = os.path.join(cur_path, reportName)  # 报告文件夹
    # 如果不存在就创建
    if not os.path.exists(report_path):
        os.mkdir(report_path)

    report_abspath = os.path.join(report_path, "天博" + now + ".html")
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner2.HTMLTestRunner(stream=fp, title="测试报告", description="用例执行情况")

    # 调用add_case返回值
    runner.run(all_case)  # discover
    fp.close()


def get_report_file(report_path):
    '''第三步：获取最新的测试报告'''
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    logger.Log().info("最新测试报告:" + lists[-1])
    # 找到最新生成的测试报告
    report_file = os.path.join(report_path, lists[-1])
    return report_file


if __name__ == "__main__":
    all_case = add_case()  # 1 加载用例
    run_case(all_case)  # 2 执行用例
    report_path = os.path.join(cur_path, "report")  # 用例文件
    report_file = get_report_file(report_path)  # 3 获取最新测试报告



