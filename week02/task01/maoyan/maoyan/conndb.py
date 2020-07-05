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
        self.sql = settings['MOVIES_SQL']
    
    # 连接数据库并写入
    def run(self, item):
        # 获取写入数据源
        movie_name = item['movie_name']
        movie_tag = item['movie_tag']
        movie_time = item['movie_time']
        data = list(zip(movie_name, movie_tag, movie_time))

        # 数据库连接
        try:
            db = pymysql.connect(**self.dbparams)
            # 建立游标
            cursor = db.cursor()
            print("数据库连接成功！")
        except Exception as e:
            print(e)

        # 写入数据库
        try:
            if type(data[0]) == tuple:
                # 批量写入
                cursor.executemany(self.sql, data)
            else:
                cursor.execute(self.sql, data)
            cursor.close()
            db.commit()
        except Exception as e:
            db.rollback()
            print("错误：%s" % e)
        db.close()

if __name__ == "__main__":
    db = ConnDB()
    db.run(item)

