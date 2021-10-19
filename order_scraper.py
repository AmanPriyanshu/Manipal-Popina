import scrapy  
from scrapy.crawler import Crawler
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
import pandas as pd
import sys

names, prices = [], []

class OrderGenerator(scrapy.Spider):
  name = 'OrderGenerator'
  def parse(self, response):
    global prices, names
    data = response.css('.cYGeYt').extract()
    for val in data:
      try:
        val = val[val.index('<h4 class="')+len('<h4 class="'):]
        name = val[val.index('">')+2:val.index('</h4>')]
        val = val[val.index('</span></div><div class="')+len('</span></div><div class="'):]
        val = val[val.index('"><span class="')+len('"><span class="'):]
        price = val[val.index('">')+2:val.index('</span')]
        names.append(name)
        prices.append(price)
      except:
        pass

url, name = sys.argv[1].strip(), '_'.join(sys.argv[2:]).strip()

urls = [url]

process = CrawlerProcess({'USER_AGENT': 'Mozilla/5.0'})
process.crawl(OrderGenerator, start_urls=urls)
process.start()

df = pd.DataFrame({'names': names, 'prices': [float(''.join([j for j in i if j.isdigit() or j=='.'])) for i in prices]})
df.to_csv("./restros/"+name+".csv", index=False)