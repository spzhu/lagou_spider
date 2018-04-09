# -*- coding: utf-8 -*-
import hashlib

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import LagouspiderItem, LagouItemLoader


class LagouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = ['http://www.lagou.com/']
    # start_urls = ['https://www.lagou.com/zhaopin/Python/']

    rules = (
        Rule(LinkExtractor(allow=r'zhaopin/.*'), follow=True),
        # Rule(LinkExtractor(allow=r'gongsi/\d+\.html'), follow=True),
        Rule(LinkExtractor(allow=r'jobs/\d+\.html'), callback='parse_item', follow=True),
    )


    def parse_item(self, response):
        loader = LagouItemLoader(LagouspiderItem(), response=response)
        loader.add_value('crawl_url', response.url)
        m = hashlib.md5()
        m.update(response.url.encode("utf8"))
        loader.add_value('crawl_url_id', m.hexdigest())
        loader.add_xpath('job_name', '//div[@class="job-name"]/@title')
        loader.add_xpath('salary', '//span[@class="salary"]/text()')
        loader.add_xpath('city', '//dd[@class="job_request"]/p/span[2]/text()')
        loader.add_xpath('work_year', '//dd[@class="job_request"]/p/span[3]/text()')
        loader.add_xpath('degree_need', '//dd[@class="job_request"]/p/span[4]/text()')
        loader.add_xpath('job_nature', '//dd[@class="job_request"]/p/span[5]/text()')
        loader.add_xpath('labels', '//li[@class="labels"]/text()')
        loader.add_xpath('publish_time', '//p[@class="publish_time"]/text()')
        loader.add_xpath('job_advantage', '//dd[@class="job-advantage"]/p/text()')
        loader.add_xpath('job_desc', '//dd[@class="job_bt"]/div/p/text()')
        loader.add_css('job_addr', '.work_addr')
        loader.add_xpath('company_name', '//h2[@class="fl"]/text()')
        company_info = response.xpath('//ul[@class="c_feature"]/li')
        company_loader = loader.nested_xpath('//ul[@class="c_feature"]')
        for i, li in enumerate(company_info):
            if li.xpath('./i[@class="icon-glyph-fourSquare"]'):
                company_loader.add_xpath('industry_field', './li[{}]/text()'.format(i+1))
            else:
                company_loader.add_value('industry_field', ' ')
            if li.xpath('./i[@class="icon-glyph-trend"]'):
                company_loader.add_xpath('finance_stage', './li[{}]/text()'.format(i+1))
            else:
                company_loader.add_value('finance_stage', ' ')
            if li.xpath('./i[@class="icon-glyph-figure"]'):
                company_loader.add_xpath('company_size', './li[{}]/text()'.format(i+1))
            else:
                company_loader.add_value('company_size', ' ')
            if li.xpath('./i[@class="icon-glyph-home"]'):
                company_loader.add_xpath('company_url', './li[{}]/a/@href'.format(i+1))
            else:
                company_loader.add_value('company_url', ' ')
        return loader.load_item()
