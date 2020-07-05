import scrapy
import re

from ..items import MaoyanItem

# 设置全局一页获取的数量
LIMIT = 10

# 自定义爬取失败
class SpliderError(Exception):
    def __init__(self, Errorinfo):
        super().__init__(self, Errorinfo)
        self.errorinfo = Errorinfo
    
    def __str__(self):
        return self.errorinfo

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com/films?showType=3']
    start_urls = ['https://maoyan.com/films?showType=3/']

    # def parse(self, response):
    #     pass

    # 重写start_requests
    def start_requests(self):
        url = f'https://maoyan.com/films?showType=3&limit=%s/ip' % LIMIT
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)
    
    # 解析函数
    def parse(self, response):
        # 获取爬取的每一个电影信息
        # print(response.text)
        # print(response.request.headers['user-agent'])
        movies = scrapy.Selector(response=response).xpath(f'//*[@id="app"]/div/div[2]/div[2]/dl/dd')
        try:
            if(movies == []):
                raise SpliderError("爬取失败")
        except SpliderError as se:
            print(se)
        except Exception as e:
            print("错误：%s" % e)
        else:
            for movie in movies:
                # 爬取电影名称信息
                movie_name = movie.xpath(f'//div[1]/div[2]/a/div/div[1]/span[1]/text()')
                # print(movie_name)

                # 爬取电影类型信息
                movie_tag = movie.xpath(f'//div[1]/div[2]/a/div/div[2]/text()[2]')
                # print(movie_tag)

                # 爬取上映时间信息
                movie_time = movie.xpath(f'//div[1]/div[2]/a/div/div[4]/text()[2]')
                # print(movie_time.extract())
                
                item = MaoyanItem()
                item['movie_name'] = movie_name.extract()
                # 去除字符串前后空格
                item['movie_tag'] = list(map(lambda x:x.strip(), movie_tag.extract()))                    
                item['movie_time'] = list(map(lambda x:x.strip(), movie_time.extract()))
            yield item