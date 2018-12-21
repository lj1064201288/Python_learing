import pymysql, time
import pymongo

class Mysql_db(object):

    def __init__(self, host,user, password, port, db, table):
        '''
        MySQL初始化
        :param host: 数据库地址
        :param user: 数据库用户
        :param password: 数据库密码
        :param port: 端口
        :param db: 数据库名称
        :param table: 表格名称
        '''
        self.port = port
        self.host = host
        self.user = user
        self.db = db
        self.table = table
        self.password = password
        try:
            self.database = pymysql.connect(host=self.host, user=self.user, password=self.password, port=self.port)
            self.cursor = self.database.cursor()
            bool = self.cursor.execute('show databases like "{0}"'.format(self.db))
            if not bool:
                self.cursor.execute('create database {0} DEFAULT  CHARACTER SET utf8'.format(self.db))

            create_table_sql = 'CREATE TABLE IF NOT EXISTS {0} (ranking INT NOT NULL, name VARCHAR(255) NOT NULL,' \
                                'local VARCHAR NOT NULL, total DOUBLE NOT NULL, index_score DOUBLE NOT NULL)'.format(self.table)
            self.cursor.execute(create_table_sql)
            time.sleep(1)
        except pymysql.MySQLError as e:
            print(e.args)
    def insert_db(self, item):
        '''
        插入数据到数据库
        :param item: 数据
        :return:
        '''
        keys = ', '.join(item.keys())
        print(keys)
        values = ','.join(['%s'] * len(item))
        sql = 'insert into {0} ({1}) values ({2})'.format(self.table, keys, values)
        try:
            print(tuple(item.values()))
            self.cursor.execute(sql, tuple(item.values()))
            self.database.commit()
            print('插入成功')
        except pymysql.MySQLError as e:
            print(e.args)
            print('插入失败')
            self.database.rollback()

    def close_db(self):
        '''
        关闭数据库
        :return:
        '''
        self.database.close()





