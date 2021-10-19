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
    data = response.css('.jcWdhP').extract()
    for val in data:
      val = val[:val.index('</div><div class="')]
      val = val[val.rindex('">')+2:].strip()
      ratings.append(val)

url, name = sys.argv[1].strip(), ' '.join(sys.argv[2:]).strip()
urls = [url]

process = CrawlerProcess({'USER_AGENT': 'Mozilla/5.0'})
process.crawl(RankingGenerator, start_urls=urls)
process.start()
df = pd.DataFrame({'name':[name], 'ratings': ratings})
if not os.path.exists('links.csv'):
  header = True
else:
  header = False
df.to_csv("ratings.csv", index=False, mode='a', header=header)