"""
__author__:'vacada'
__description__:'安装并使用 requests、bs4 库，爬取猫眼电影（）的前 10 个电影名称、电影类型和上映时间，
                 并以 UTF-8 字符集保存到 csv 格式的文件中'
__mtime__:2020/6/27
"""
import re
import requests
import pandas
from bs4 import BeautifulSoup as bs


"""
获取猫眼电影数据
"""
# 猫眼电影url
url = 'https://maoyan.com/films?showType=3&limit=10'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'

# 请求头
headers = {
    'user-agent':user_agent,
    'Cookie': '__mta=88956580.1593192289431.1593243945233.1593247312300.7; uuid_n_v=v1; uuid=EDCC79B0B7D111EA8E55532676AF0F4A91C38840844C4E56A78131022CA6AA38; _csrf=2b5900ea9bc84f4fc0e616ffde12df7d6a5ab18a331887d1613215150bbf58fb; _lxsdk_cuid=172f1a91125c8-020aaa766cf1c9-4353760-e1000-172f1a91125a9; _lxsdk=EDCC79B0B7D111EA8E55532676AF0F4A91C38840844C4E56A78131022CA6AA38; mojo-uuid=ca1cd0836607633a0b439066c00045e6; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22172f4b4d06b67-0ec6f7fc9a197b-73236134-924000-172f4b4d06c331%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22172f4b4d06b67-0ec6f7fc9a197b-73236134-924000-172f4b4d06c331%22%7D; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593245921,1593246930,1593250077,1593250091; mojo-session-id={"id":"4f500c87a58b18c10922163480b5b507","time":1593254133774}; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593254138; mojo-trace-id=2; __mta=88956580.1593192289431.1593247312300.1593254137883.8; _lxsdk_s=172f558a7c8-4ea-630-746%7C%7C5'
}

response = requests.get(url, headers=headers)

bs_info = bs(response.text, 'html.parser')

"""
爬取电影信息
"""
movie_name = []       # 电影名称
movie_tag = []        # 电影类型
movie_time = []       # 上映时间

for movies in bs_info.find_all('div', attrs={'class':'movie-hover-info'}):
    # 爬取电影名称
    for names in movies.find_all('span', attrs={'class':'name'}):
        movie_name.append(names.text)

    for tags in movies.find_all('div', attrs={'class':'movie-hover-title'}):
        if '类型' in tags.text:
            tag = re.split(r'[\s]+',tags.text)[2]
            movie_tag.append(tag)
    
    # 爬取上映时间
    for times in movies.find_all('div', attrs={'class':'movie-hover-title movie-hover-brief'}):
        # 正则匹配上映日期
        time = re.split(r'[\s]+',times.text)[2]
        movie_time.append(time)

"""
写入csv
"""
data = {
    '电影名称': movie_name,
    '类型': movie_tag,
    '上映时间': movie_time,
}

movie_data = pandas.DataFrame(data=data)
movie_data.to_csv('./movie.csv', encoding='utf8', index=False)