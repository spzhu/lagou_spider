# -*- coding: utf-8 -*-

# Scrapy settings for lagouspider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'lagouspider'

SPIDER_MODULES = ['lagouspider.spiders']
NEWSPIDER_MODULE = 'lagouspider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh,zh-CN;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': '_ga=GA1.2.248481753.1515722633; user_trace_token=20180112100352-d66e08fe-f73c-11e7-8f87-525400f775ce; LGUID=20180112100352-d66e0fa1-f73c-11e7-8f87-525400f775ce; WEBTJ-ID=20180405160823-16294d97c71250-0d753f8a6484d1-3a75045d-1296000-16294d97c72727; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1522915704; JSESSIONID=ABAAABAAAFCAAEG6D2FEE010A10F8716FCA0DD38968349F; X_HTTP_TOKEN=24b8a3f6b86247bbc5fd6b4acd3da77c; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; gate_login_token=""; LG_LOGIN_USER_ID=25dabe49d2acdf47efd0c3b1c803be1ff08a2af44c7b72ec; _putrc=8A94674167064761; login=true; unick=%E6%9C%B1%E6%A3%AE%E9%B9%8F; TG-TRACK-CODE=index_navigation; gate_login_token=d91ef9c6054dc576b37d19cce7b77eb092eefee93489afdd; SEARCH_ID=fd197615db154b0098a25c4f56d96b6d; _gat=1; LGSID=20180406161100-0a80c55f-3972-11e8-b563-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; index_location_city=%E5%85%A8%E5%9B%BD; LGRID=20180406161125-19b5ffc4-3972-11e8-b73e-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1523002286',
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    'Referer': 'https://www.lagou.com/',
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'lagouspider.middlewares.LagouspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'lagouspider.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'lagouspider.pipelines.LagouspiderPipeline': 300,
    'lagouspider.pipelines.MysqlTwistedPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
