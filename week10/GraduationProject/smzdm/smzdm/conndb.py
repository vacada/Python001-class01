# coding=utf-8
import pymysql
from scrapy.utils.project import get_project_settings   # 导入settings配置


class ConnDB:
    # 从settings获取数据库连接信息和sql
    def __init__(self):
        settings = get_project_settings()       
        self.dbparams = dict(
            host = settings['MYSQL_HOST'],
            port = settings['MYSQL_PORT'],
            user = settings['MYSQL_USER'],
            password = settings['MYSQL_PASSWORD'],
            db = settings['MYSQL_DB'],
            charset='utf8',
        )
        self.sql = settings['PHONE_SQL']
    
    # 连接数据库并写入
    def run(self, item):
        # 获取写入数据源
        data = (item['phone_rank'], item['phone_name'], item['phone_comment'], item['comment_page'])
        print(data)

        # 数据库连接
        try:
            db = pymysql.connect(**self.dbparams)
            # 建立游标
            cursor = db.cursor()
            print("数据库连接成功！")
        except Exception as e:
            print(f'数据库连接错误：{e}')

        # 写入数据库
        try:
            cursor.execute(self.sql, data)
            cursor.close()
            db.commit()
            print(f'数据库写入操作成功')
        except Exception as e:
            db.rollback()
            print(f"数据库写入错误：{e}")
        db.close()

if __name__ == "__main__":
    db = ConnDB()
    db.run(item)

