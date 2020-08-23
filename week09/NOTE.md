Week09学习笔记
+ 常用功能
	+ 偏函数
		+ from functools import partial
		+ 注意：
			+ partial 第一个三叔必须是可调用对象
			+ 参数传递顺序是从左到右，但不能超过原函数参数个数
			+ 关键字参数会覆盖partial中定义好的参数
+ 为什么自定义的Model要继承models.Model
	+ 不需要显示定义主键
	+ 自动拥有查询管理器对象
	+ 可以使用ORM API 对数据库、表实现CRUD 
+ 元类
	+ 必须继承自type
	+ 自定义\_\_new__
	+ 必须返回类
+ 信号用途
	+ 发生事件，通知应用程序
	+ 支持若干信号发送者通知一组接收者
	+ 解耦
+ 中间件
	+ 全局改变输入或输出
	+ 轻量级的、低级的“插件系统”
	+ 对请求、响应处理的钩子框架
+ django生产环境部署转换器
	+ Nginx
	+ Tornado
	+ gunicon
		+ -b 设置IP、端口
		+ -w 设置进程
+ Celery
	+ Celery是分布式消息队列
	+ 使用Celery实现定时任务
	+ 如何使用
		1. Redis安装和启动
		2. 安装Celery
			+ pip install celery
			+ pip install redis==2.10.6
			+ pip install celery-with-redis
			+ pip install django-celery
		3. 添加App
			1. 创建应用
			'''python manage.py startapp djcron'''
			2. 加入APPS
			'''python
			INSTALL_APPS[
			'djcelery',
			'djcron',
			]
			'''
		4. 迁移生成表
		'''python manage.py migrate'''
		5. 配置django时区
		6. 在项目下建立celery.py
		