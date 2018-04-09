# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join
from w3lib.html import remove_tags


def remove_slash(value):
    if isinstance(value, str):
        return value.replace('/', '').strip()
    else:
        return value


def remove_blank(value):
    if isinstance(value, str):
        return value.strip()
    else:
        return value


def get_publish_time(value):
    return value.replace("\xa0", "").split(" ")[0].strip()


def get_job_addr(value):
    return [x for x in value.split('\n') if x.strip() != "查看地图"]


class LagouItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
    default_input_processor  = MapCompose(remove_blank)

    city_in           = MapCompose(remove_slash)
    work_year_in      = MapCompose(remove_slash)
    degree_need_in    = MapCompose(remove_slash)
    job_nature_in     = MapCompose(remove_slash)
    labels_in         = Join(", ")
    publish_time_in   = MapCompose(get_publish_time)
    job_advantage_out = Join('\n')
    job_desc_out      = Join('\n')
    job_addr_in       = MapCompose(remove_tags, get_job_addr, remove_blank)
    job_addr_out      = Join("")


class LagouspiderItem(scrapy.Item):
    # define the fields for your item here like:
    job_name       = scrapy.Field()
    salary         = scrapy.Field()
    city           = scrapy.Field()
    work_year      = scrapy.Field()
    degree_need    = scrapy.Field()
    job_nature     = scrapy.Field()
    labels         = scrapy.Field()
    publish_time   = scrapy.Field()
    job_advantage  = scrapy.Field()
    job_desc       = scrapy.Field()
    job_addr       = scrapy.Field()
    company_name   = scrapy.Field()
    finance_stage  = scrapy.Field()
    company_size   = scrapy.Field()
    company_url    = scrapy.Field()
    crawl_url      = scrapy.Field()
    crawl_url_id   = scrapy.Field()
    industry_field = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """INSERT INTO jobs(job_name, salary, city, work_year, degree_need, job_nature, labels,
        publish_time, job_advantage, job_desc, job_addr, company_name, finance_stage, company_size, company_url,
        crawl_url, crawl_url_id, industry_field) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s) ON DUPLICATE KEY UPDATE salary=VALUES(salary), job_advantage=VALUES(job_advantage),
        job_desc=VALUES(job_desc)
        """
        values = (
            self.get("job_name", ''),
            self.get("salary", ''),
            self.get("city", ''),
            self.get("work_year", ''),
            self.get("degree_need", ''),
            self.get("job_nature", ''),
            self.get("labels", ''),
            self.get("publish_time", ''),
            self.get("job_advantage", ''),
            self.get("job_desc", ''),
            self.get("job_addr", ''),
            self.get("company_name", ''),
            self.get("finance_stage", ''),
            self.get("company_size", ''),
            self.get("company_url", ''),
            self.get("crawl_url", ''),
            self.get("crawl_url_id", ''),
            self.get("industry_field", ''),
        )
        return insert_sql, values
