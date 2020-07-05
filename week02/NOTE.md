# week2学习笔记
1. 异常捕获
	+ try（正常操作）...except(发送异常执行)
	+ try...except...else(如果没有异常执行)
	+ try...finally(退出try时总会执行)
	+ raise 触发异常
	+ 自定义异常
	```python
		class UserInputError(Exception):
			def __init__(self, ErrorInfo):
				super().__init__(self, ErrorInfo)
				self.errorinfo = ErrorInfo
			def __str__(self):
				return self.errorinfo

		userinput = 'a'

		try:
			if (not userinput.isdigit()):
				raise UserInputError('用户输入错误')
		except UserInputError as ue:
			print(ue)
		finally:
			del userinput
	```
	+ 异常美化库：pretty_errors
	+ with...as上下文(常见with打开文件)
	
2. 操作数据库
	+ 操作mysql数据库的三方库： pymysql
	+ 操作完成需要关闭游标和关闭连接
	+ fechone和fechall
		- fechone()返回单个的元组，也就是一条记录(row)，如果没有结果 , 则返回 None
		- fechall()返回多个元组，即返回多条记录(rows),如果没有结果,则返回 ()
	+ execute和executemany
		- execute 插入单条数据
		- executeman批量插入数据
3. 反爬虫
	+ 模拟请求头像
		- 模拟user-agent时，需随机生成
		- 模拟referer
		- 石墨requests模拟登录时，头部需包含如下内容
		```python
		headers = {
			'User-Agent': ua.random,
			'sec-fetch-site': 'same-origin',
			'sec-fetch-mode': 'cors',
			'sec-fetch-dest': 'empty',
			'Referer': 'https://shimo.im/login?from=home',
			'x-requested-with': 'XmlHttpRequest',
			'x-source':	'lizard-desktop',
		}
		```
	+ 模拟cookie
		- 借助requests 会话保持cookie
		- 借助selenium 操作后获取用户cookie
	+ 模拟用户点击
		- 借助基于webdriver协议的selenium模拟用户操作
		- webdrvier需要下载和浏览器版本一致的exe文件
		- 使用pipenv时，webdriver需放在./scripts文件内
	+ 三方库：
		- fake_useragent 随机生成user-agent
		- selenium 模拟浏览器操作
4. 验证码识别
	+ 三方库：
		- brew install leptonica
		- brew install tesseract
		- pip install pillow（图片处理）
		- pip install pytessseract（pytesseract是Python的一个OCR识别库）
	+ 图片字符识别流程
		- 下载图片
		- 灰度图片（pytesseract对黑白图片的识别处理测试还可以，但是对彩色图片识别率不是很高）
		- 二值化
		- 借助pytesteract(切分,旋转)完成
5. 爬虫中间件s
	+ 自定义中间件
		- 中间件开启在settings的DOWNLOADER_MIDDLEWARES参数
		- 自定义中间件在middlewares.py文件重写
		- 随机代理IP
		- 随机User-agent
6. 分布式爬虫
	+ scrapy不支持分布式
	+ 分布式需借助Redis实现队列和管道的共享
	+ 三方库：scrapy-redis
		- 使用RedisSpider类取代了Spider类
		- Scheduler的queue由redis实现
		- item pipline由 Redis实现
	+ daemonize yes 保证终端关闭不被结束
