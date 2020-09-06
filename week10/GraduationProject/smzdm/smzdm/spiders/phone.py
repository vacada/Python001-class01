import scrapy
import json

from ..items import SmzdmItem

class PhoneSpider(scrapy.Spider):
    name = 'phone'
    allowed_domains = ['smzdm.com']
    start_urls = ['http://smzdm.com/']

     # 重写start_requests
    def start_requests(self):
        url = f'https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1'
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)
    
    # 解析排行榜手机列表信息
    def parse(self, response):
        phones = scrapy.Selector(response=response).xpath(f'//*[@id="feed-main-list"]/li')[:10]
        __count = 1
        for phone in phones:
            phone_name = phone.xpath(f'./div/div[2]/h5/a/text()').extract()[0]
            comment_link = phone.xpath(f'./div/div/div/div/a[2]/@href').extract()[0]
            item = SmzdmItem()
            item['phone_rank'] = __count
            item['phone_name'] = phone_name
            item['comment_link'] = comment_link
            item['comment_page'] = 1
            __count += 1
            yield scrapy.Request(url=comment_link, meta={'item': item}, callback=self.parse2)

    # 解析手机评论信息
    def parse2(self, response):
        item = response.meta['item']
        comments = scrapy.Selector(response=response).xpath(f'//*[@id="commentTabBlockNew"]//*[@class="comment_list"]')
        _comment_list = []
        for comment in comments:
            _comment = {}
            _comment['grey'] = comment.xpath(f'./div/span/text()').extract()[0]
            comment_data = comment.xpath(f'./div/div[@class="comment_conWrap"]//p/span')
            _comment['comment'] = comment_data.xpath('string(.)').extract()[0].strip()
            reply_data = comment.xpath(f'./div/div[@class="blockquote_wrap"]//p/span')
            # _comment['comment_reply'] = reply_data.xpath('string(.)').extract().strip()
            _comment['comment_reply'] = list(map(lambda x: x.strip(), reply_data.xpath('string(.)').extract()))
            _comment_list.append(_comment)
        item['phone_comment'] = json.dumps(_comment_list)

        yield item

        # 翻页
        try:
            pagedown = scrapy.Selector(response=response).xpath(f'//*[@id="comment"]/div[1]//li[@class="pagedown"]/a/@href').extract()[0]
        except:
            pass
        else:
            item['comment_page'] += 1
            yield scrapy.Request(url=pagedown, meta={'item': item}, callback=self.parse2)