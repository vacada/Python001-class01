# Scrapy settings for smzdm project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'smzdm'

SPIDER_MODULES = ['smzdm.spiders']
NEWSPIDER_MODULE = 'smzdm.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'smzdm (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3

# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
  'Cookie':'__ckguid=Flo4VtNJ1GSOpjoiGgHLJ2; __jsluid_s=7aa68eb2eb2fb185256914365c04060d; device_id=196108996515986984151620088ab333968c1cfd0a0a02cd76745b7cc9; zdm_qd=%7B%22referrer%22%3A%22https%3A%2F%2Fu.geekbang.org%2Flesson%2F18%3Farticle%3D273014%22%7D; _ga=GA1.2.1130356619.1598698418; __gads=ID=6552bc282f85daa8:T=1598713753:S=ALNI_MajJAzr8gQhBOoF2y0K3XESBQ0sIw; wt3_sid=%3B999768690672041; smzdm_ea=200; smzdm_ec=06; Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1598716629,1598716689,1598716699,1598716748; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217439d9ec5348c-0cfed43eab1fab-3323766-921600-17439d9ec542e8%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217439d9ec5348c-0cfed43eab1fab-3323766-921600-17439d9ec542e8%22%7D; wt3_eid=%3B999768690672041%7C2159871437500128325%232159871761500065991; _gid=GA1.2.1331451618.1598969500; Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58=1598969528; amvid=a3a4013ff54039f75d43ebf7856783f8',
  'Sec-Fetch-Dest': 'document',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-Site': 'none',
  'Sec-Fetch-User': '?1',
  'Upgrade-Insecure-Requests': '1',
}
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'smzdm.middlewares.SmzdmSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'smzdm.middlewares.SmzdmDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'smzdm.pipelines.SmzdmPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = '111111'
MYSQL_DB = 'graduation_project'
PHONE_SQL = 'INSERT INTO `phones` (`phone_rank`, `phone_name`, `phone_comment`, `comment_page`) VALUES (%s, %s, %s, %s)'

