'''
MySQL数据库的API
写入创建数据库方法,创建表格方法,插入方法,查找方法,更新与删除方法
'''

from pymysql import connect


# 构建类
class Mysql_API(object):
    def __init__(self):
        self.host = 'localhost'
        self.port = 3306
        self.user = 'root'
        self.password = '123456'
        self.db = connect(host=self.host, user=self.user, password=self.password, port=self.port)
        self.cursor = self.db.cursor()

    def create_sql(self, database):
        try:
            self.database = database
            sql = 'create database ' + database + ' default character set utf8'
            self.cursor.execute(sql)
        except Exception as e:
            print(e.args)

    # 创建数据表
    def create_table(self, table):
        try:
            self.cursor.execute('use ' + self.database)
            sql = 'create table if not exists ' + table + '(park_id INT UNSIGNED AUTO_INCREMENT, ' \
                                                          'name varchar(200) not null, ' \
                                                          'locatlat float, ' \
                                                          'locatlng float, ' \
                                                          'address varchar(200), '\
                                                          'area varchar(200), ' \
                                                          'uid varchar(200) not null, ' \
                                                          'city varchar(200),' \
                                                          'PRIMARY KEY (park_id))'
            self.cursor.execute(sql)
        except Exception as e:
            print(e.args)

    # 插入数据
    def insert_data(self, db, table, data):
        self.cursor.execute('use ' + db)
        keys = ','.join(data.keys())
        values = ','.join(['%s'] * len(data))
        sql = 'insert into %s (%s) values (%s)' %(table, keys, values)
        try:
            self.cursor.execute(sql, tuple(data.values()))
            self.db.commit()
        except Exception as e:
            print(e.args)
            self.db.rollback()

        finally:
            self.cursor.close()
            self.db.close()

# sql = Mysql_API()
# data = {
#      'name': '石家庄植物园',
#      'locatlat': 38.112403,
#      'locatlng': 114.388762,
#      'address': '河北省石家庄市鹿泉区植物园街60号',
#      'area': '鹿泉区',
#      'uid': '51fd37a48d769517b5147f83',
#      'city': '石家庄市'
#     }
# sql.create_sql('park')
# sql.create_table('park')
# sql.insert_data('park', 'park', data)
