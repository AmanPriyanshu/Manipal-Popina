import scrapy  
from scrapy.crawler import Crawler
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
import pandas as pd
import sys
import os

links = []

class OrderGenerator(scrapy.Spider):
  name = 'OrderGenerator'
  def parse(self, response):
    global links
    body = str(response.body)
    link = body[body.index('www.google.com/maps/dir/?')+len('www.google.com/maps/dir/?'):]
    link = 'https://www.google.com/maps/dir/?api=1&destination='+link[link.index('destination=')+len('destination='):link.index('" target="_blank"')]
    links.append(link)

url, name = sys.argv[1].strip(), ' '.join(sys.argv[2:]).strip()

urls = [url]

process = CrawlerProcess({'USER_AGENT': 'Mozilla/5.0'})
process.crawl(OrderGenerator, start_urls=urls)
process.start()
df = pd.DataFrame({'name':[name], 'link': links})
if not os.path.exists('links.csv'):
  header = True
else:
  header = False
df.to_csv("links.csv", index=False, mode='a', header=header)