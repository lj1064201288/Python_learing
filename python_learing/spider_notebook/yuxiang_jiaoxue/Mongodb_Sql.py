import pymongo

class Mongo_DB():
    # 初始化数据库名称与集合名称
    def __init__(self, dataname, collection):
        self.dataname = dataname
        self.collection = collection

    # 打开数据库
    def open_data(self):
        self.client = pymongo.MongoClient(host='localhost', port=27017)
        self.db = self.client[self.dataname]

    # 插入数据
    def insert_data(self, datas):
        self.db[self.collection].insert(dict(datas))



    # 删除数据
    def delete_data(self, value):
        self.db.self.collection.delete_many(value)

    # 关闭数据库
    def close_data(self):
        self.client.close()

