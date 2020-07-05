"""
__author__:'vacada'
__description__:'使用requests模拟【石墨文档】登录'
__mtime__:2020/7/4
"""


import requests
from fake_useragent import UserAgent
from configparser import ConfigParser

# 忽略ssl验证和禁用服务器缓存
ua = UserAgent(verify_ssl=False, use_cache_server=False)

# 获取cookie请求头
pre_headers = {
    'User-Agent': ua.random,
    'Referer': 'https://shimo.im/welcome',
}

# 模拟登录请求头
headers = {
    'User-Agent': ua.random,
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'Referer': 'https://shimo.im/login?from=home',
    'x-requested-with': 'XmlHttpRequest',
    'x-source':	'lizard-desktop',
}


# 会话对象：在同一个Session实例发出的所有请求之间保持cookie
s = requests.session()

# 从配置文件读取石墨文档模拟登录数据
cfg = ConfigParser()
cfg.read('config.ini')
login_url = cfg.get('shimo', 'login_url')
form_data = {
    'email': cfg.get('shimo', 'login_email'),
    'mobile': cfg.get('shimo', 'login_mobile'),
    'password': cfg.get('shimo', 'login_password'),
}

# 登陆前获取cookie
pre_login = cfg.get('shimo', 'pre_login_url')
pre_resp = s.get(pre_login, headers=pre_headers)

# 模拟登录
login_response = s.post(login_url, data=form_data, headers=headers, cookies=s.cookies)
print(login_response.text)
print(login_response.status_code)


