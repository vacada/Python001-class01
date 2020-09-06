import pymysql
import pandas as pd
import json

from snownlp import SnowNLP


MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = '111111'
MYSQL_DB = 'graduation_project'
        

class ConnDB:
    def __init__(self):     
        self.dbparams = dict(
            host = MYSQL_HOST,
            port = MYSQL_PORT,
            user = MYSQL_USER,
            password = MYSQL_PASSWORD,
            db = MYSQL_DB,
            charset='utf8mb4',
        )
        self.db = None
        self.cursor = None
    
    # 数据库连接
    def connect(self):
        try:
            self.db = pymysql.connect(**self.dbparams)
            # 建立游标
            self.cursor = self.db.cursor()
            print("数据库连接成功！")
        except Exception as e:
            print(f'数据库连接错误：{e}')
    
    @property
    def count(self):
        self.cursor.execute('SELECT COUNT(DISTINCT phone_rank) FROM phones')
        return self.cursor.fetchone()[0]

    # 查询数据
    def select_data(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # 写入数据
    def insert_data(self, sql, data):
        try:
            if type(data[0]) == tuple:
                # 批量写入
                self.cursor.executemany(sql, data)
            else:
                self.cursor.execute(sql, data)
            self.db.commit()
            print(f'写入完成')
        except Exception as e:
            self.db.rollback()
            print(f"错误：{e}")

    # 关闭数据库连接
    def close(self):
        self.cursor.close()
        self.db.close()
        print(f'关闭数据库连接')


class Clearn:
    def __init__(self):
        self.phone_rank = None
        self.phone_name = ''

    # 清洗评论信息    
    def clearn(self, datas):
        _comments = []
        _sql_data = []
        for data in datas:
            self.phone_rank = data[1]
            self.phone_name = data[2]
            phone_comments = data[3]
            input_time = data[5]
            comment_data = json.loads(phone_comments)
            for comment in comment_data:
                _comments.append(comment['comment'])
                list(map(lambda x: _comments.append(x), comment['comment_reply']))
        # 去重
        _comments = list(set(_comments))

        # 处理写入sql数据
        for comment in _comments:
            l = []
            l.append(self.phone_rank)
            l.append(self.phone_name)
            l.append(comment)
            l.append(self._sentiment(comment))
            l.append(input_time)
            _sql_data.append(tuple(l))
        return _sql_data
        
    # 对评论进行语义倾向
    def _sentiment(self, comment):
        s = SnowNLP(comment)
        return s.sentiments

if __name__ == "__main__":
    cdb = ConnDB()
    cl = Clearn()
    cdb.connect()
    for i in range(1, cdb.count+1):
        select_sql = f"SELECT * FROM `phones` WHERE `phone_rank` = '{i}'"
        data = cdb.select_data(select_sql)
        sql_data = cl.clearn(data)
        insert_sql = f"INSERT INTO `comments` (`phone_rank`, `phone_name`, `comment`, `comment_analysis`, `input_time`) VALUES (%s, %s, %s, %s, %s)"
        cdb.insert_data(insert_sql, sql_data)
    cdb.close()
