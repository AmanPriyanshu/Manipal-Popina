import scrapy  
from scrapy.crawler import Crawler
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
import pandas as pd
import sys
import os

ratings = []

class RankingGenerator(scrapy.Spider):
  name = 'RankingGenerator'
  def parse(self, response):
    global ratings
    data = str(response.body)
    data = [i for i in data.split('{\\\\"name\\\\":\\\\"') if not i.startswith('restaurant') and len(i)>100][1:-1]
    data = [i.split('\\\\"url\\\\":\\\\"')[2] for i in data]
    data = [i[:i.index('}')-3] for i in data]
    ratings = data

url, name = sys.argv[1].strip(), ' '.join(sys.argv[2:]).strip()
urls = [url]

process = CrawlerProcess({'USER_AGENT': 'Mozilla/5.0'})
process.crawl(RankingGenerator, start_urls=urls)
process.start()

df = pd.DataFrame({'name': [name for _ in range(len(ratings))], 'links': ratings})
df.to_csv("r.csv", index=False, mode='a', header=False)