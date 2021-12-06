import scrapy  
from scrapy.crawler import Crawler
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
import pandas as pd
import sys
import os

numbers = []
url, name = sys.argv[1].strip(), ' '.join(sys.argv[2:]).strip()
url = url.replace('/order', '')
#url = 'https://www.zomato.com/manipal/hangyo-ctf-eshwar-nagar'
urls = [url]

class OrderGenerator(scrapy.Spider):
  name = 'OrderGenerator'
  def parse(self, response):
    global numbers, name
    body = str(response.body)
    number = body[body.index('"telephone":"')+len('"telephone":"'):]
    numbers.append(number[:number.index('","')])
    df = pd.DataFrame({'name':[name], 'nos':numbers})
    df.to_csv("numbers.csv", mode='a', header=False, index=False)

process = CrawlerProcess({'USER_AGENT': 'Mozilla/5.0'})
process.crawl(OrderGenerator, start_urls=urls)
process.start()