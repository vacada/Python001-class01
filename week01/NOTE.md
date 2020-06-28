# 第一周学习笔记
## Scrapy学习
+ 创建Scrapy项目
	1.pip 安装scrapy三方库
	2.运行环境执行 scrapy startproject [项目名称]
		scrapy startproject movies
	3.切换至【项目文件】【项目文件包】
		cd movies\movies
	4.运行环境执行 scrapy genspider [爬虫名字] [域名]
		scrapy genspider maoyan maoyan.com
+ 运行Scrapy项目
	运行环境执行 scrapy crawl [爬虫名字]
+ 设置headers配置
	+ 修改settng文件
		1.打开setting文件
		2.生效COOKIES_ENABLED参数
			一般把注释的COOKIES_ENABLED取消注释就可以
		3.生效DEFAULT_REQUEST_HEADERS参数
			把相关参数加入DEFAULT_REQUEST_HEADERS内
	+ 重写start_requests函数
		1.打开命名为爬虫名字的文件
		2.重写函数start_requests函数
		```python
		def start_requests(self):
			headers = {
				'Cookie': 'Test'
			}
			url = f'https://maoyan.com/films?showType=3&limit=%s' % LIMIT
			yield scrapy.Request(url=url, headers=headers, callback=self.parse, dont_filter=False)
```
+ 写入文件配置
	1.打开setting文件
	2.生效ITEM_PIPELINES参数

## Python学习
+ 字符串空格处理
	- strip()
		- strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
		``` python
		str = "00000003210Runoob01230000000"; 
		print str.strip( '0' );  # 去除首尾字符 0
		
		str2 = "   Runoob      ";   # 去除首尾空格
		print str2.strip();
		```
		- str.lstrip() ： 去除字符串左边的空格
		- str.rstrip() ： 去除字符串右边的空格
	- split()
		- split() 通过指定分隔符对字符串进行切片，如果第二个参数 num 有指定值，则分割为 num+1 个子字符串。
		- str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
		- num -- 分割次数。默认为 -1, 即分隔所有。
		- 不支持正则及多个切割符号，不感知空格的数量
		``` python
		str = "this is string example....wow!!!"
		print (str.split( ))       # 以空格为分隔符
		print (str.split('i',1))   # 以 i 为分隔符
		print (str.split('w'))     # 以 w 为分隔符
		
		# 输出
		['this', 'is', 'string', 'example....wow!!!']
		['th', 's is string example....wow!!!']
		['this is string example....', 'o', '!!!']
		```
	- re.split()
		- 支持正则及多个字符切割
		
+ Map高阶函数结合匿名函数的应用
	- 根据提供的函数对指定序列做映射
	- Python 3 返回迭代器
	``` python
	list = list(map(lambda x:x*2,[1,2,3,4,5]))
	print(list)
	# 输出
	[2, 4, 6, 8, 10]
	```

## 数据处理
+ 使用panda写入csv文件
	``` python
	    def process_item(self, item, spider):
			movie_name = item['movie_name']
			movie_tag = item['movie_tag']
			movie_time = item['movie_time']
			data = {
					'电影名称': movie_name,
					'类型': movie_tag,
					'上映时间': movie_time,
			}
			movie_data = pandas.DataFrame(data=data)
			movie_data.to_csv('./movie.csv', encoding='utf8', index=False)
			return item
	```

