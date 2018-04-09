# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

from twisted.enterprise import adbapi


# 同步方式
class LagouspiderPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            user='root',
            passwd='root',
            db='lagou',
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = """INSERT INTO jobs(job_name, salary, city, work_year, degree_need, job_nature, labels,
        publish_time, job_advantage, job_desc, job_addr, company_name, finance_stage, company_size, company_url,
        crawl_url, crawl_url_id, industry_field) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s) ON DUPLICATE KEY UPDATE salary=VALUES(salary), job_advantage=VALUES(job_advantage),
        job_desc=VALUES(job_desc)
        """
        values = (
            item["job_name"],
            item["salary"],
            item["city"],
            item["work_year"],
            item["degree_need"],
            item["job_nature"],
            item["labels"],
            item["publish_time"],
            item["job_advantage"],
            item["job_desc"],
            item["job_addr"],
            item["company_name"],
            item["finance_stage"],
            item["company_size"],
            item["company_url"],
            item["crawl_url"],
            item["crawl_url_id"],
            item["industry_field"],
        )
        # 使用VALUES实现传值
        self.cursor.execute(insert_sql, values)
        self.conn.commit()
        return item


# 异步方式插入mysql
class MysqlTwistedPipeline:
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    # 自定义组件或扩展很有用的方法: 这个方法名字固定, 是会被scrapy调用的。
    # 这里传入的cls是指当前的MysqlTwistedPipline class
    def from_settings(cls, settings):
        dbparms = dict(
            host="127.0.0.1",
            port=3306,
            db="lagou",
            user="root",
            passwd="root",
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
        )
        # 连接池ConnectionPool
        # def __init__(self, dbapiName, *connargs, **connkw):
        dbpool = adbapi.ConnectionPool("pymysql", **dbparms)

        # 此处相当于实例化pipeline, 要在init中接收。
        return cls(dbpool)

    def process_item(self, item, spider):
        # 使用twisted将mysql插入变成异步执行：参数1：我们自定义一个函数,里面可以写我们的插入逻辑
        query = self.dbpool.runInteraction(self.do_insert, item)
        # 添加自己的处理异常的函数
        query.addErrback(self.handle_error, item, spider)
        return item

    def do_insert(self, cursor, item):
        # 执行具体的插入
        # 根据不同的item 构建不同的sql语句并插入到mysql中
        insert_sql, params = item.get_insert_sql()
        cursor.execute(insert_sql, params)

    def handle_error(self, failure, item, spider):
        # 处理异步插入的异常
        with open("errors.log", 'w') as f:
            f.write(repr(failure)+'\n')
        print(failure)
