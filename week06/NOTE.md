# week04学习笔记

+ django项目启动
	+ 创建项目
			django-admin startproject [项目名称]
	+ 创建应用程序
			python manage.py startapp [应用名称]
	+ 启动django
			python manage.py runserver
	+ 结束django
			ctrl+c
+ django settings.py
	+ DEBUG = TRUE 调试模式
	+ 常规修改
		+ 数据库选择
		+ 加入自己的app
+ django url调度器
	+ 项目url指向应用的url，应用url调度相应的视图，方便维护
	+ url匹配
		+ 类型匹配
				path('<int:year>', view.myyear),
		+ 正则匹配
				re_path('?P<year>[0-9{4}.html', view.myyear),
		+ 自定义匹配
			+ 导入 register_converter
					django.urls import register_converter
			+ 导入自定义匹配文件
					from . import [模块]
			+ 定义 register_converter
					register_converter([模块].[类], 'name')
			+ 定义过滤器
					path('<name: year>', view.myyear)
+ 模块和包
	+ 以.py结尾的python程序就是模块
	+ 包是存放多个模块的目录
	+ __inint__文件在导入包后优先运行
+ django view视图
	+ 快捷函数
			render()
			redirect()
			get_object_or_404()
+ django ORM
	+ 创建模型
			编辑 models.py 文件，改变模型
			运行 python manage.py makemigrations 为模型的改变生成迁移文件
			运行 python manage.py migrate 来应用数据库迁移

