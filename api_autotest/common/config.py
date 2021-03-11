"""
配置文件
"""
#h5域名
h5_url = 'http://pre-h5.theyyone.com/'
#h5登录header
headers_login = {
  'Accept-Encoding': 'gzip, deflate',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Client-Type': 'h5',
  'Connection': 'keep-alive',
  'Content-Length': '100',
  'Content-Type': 'application/json',
  'Host': 'pre-h5.theyyone.com',
  'Origin': 'http://pre-h5.theyyone.com',
  'Referer': 'http://pre-h5.theyyone.com/entry/login',
  'User_Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
}
#h5header
headers = {
  'Accept': 'application/json',
  'Accept-Encoding': 'gzip, deflate',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'client-Type': 'h5',
  'Connection': 'keep-alive',
  'Content-Length': '0',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Host': 'pre-h5.theyyone.com',
  'Referer': 'http://pre-h5.theyyone.com/app/mine',
  'User_Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
}
#数据库文件
database = r'D:\接口自动化\api_autotest\data\test.db'

#bot
token = '1594415629:AAG5mcKgIRcmC0laq0c8xv6pwiAOr3CLG7o'