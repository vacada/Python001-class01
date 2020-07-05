"""
__author__:'vacada'
__description__:'使用selenium模拟【石墨文档】登录'
__mtime__:2020/7/4
"""
import time
from selenium import webdriver
from configparser import RawConfigParser

def simulation_login():

    # 读取配置文件
    cfg = RawConfigParser()
    cfg.read('config.ini')

    try:
        # 使用pipenv,webdriver需放在./Scripts内
        browser = webdriver.Chrome()

        # 从配置文件读取石墨文档模拟登录
        browser.get(cfg.get('shimo', 'pre_login_url'))
        time.sleep(2)

        browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input')\
                                    .send_keys(cfg.get('shimo', 'login_email'))
        browser.find_element_by_name('password').send_keys('shimo', 'login_password')
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button')\
                                    .click()
        # 获取cookies
        cookies = browser.get_cookies()
        print(cookies)
        time.sleep(30)
    except Exception as e:
        print(e)
    finally:
        browser.close()

def main():
    simulation_login()

if __name__ == "__main__":
    main()

    
