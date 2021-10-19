import scrapy  
from scrapy.crawler import Crawler
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
import pandas as pd

links, names = [], []

class RestroGenerator(scrapy.Spider):
  name = 'RestroGenerator'
  def parse(self, response):
    global links, names
    data = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "sc-1mo3ldo-0", " " ))]//div//div//*[contains(concat( " ", @class, " " ), concat( " ", "jumbo-tracker", " " ))]//div').extract()
    for val in data:
      try: 
        val = val[val.index('<a href="')+len('<a href="'):]
        link = val[:val.index('" class="')]
        val = val[val.index('<h4 class="')+len('<h4 class="'):]
        name = val[val.index('">')+2:val.index('</h4><div class="')]
        links.append(link)
        names.append(name)
      except:
        pass

urls = ['https://www.zomato.com/manipal']

process = CrawlerProcess({'USER_AGENT': 'Mozilla/5.0'})
process.crawl(RestroGenerator, start_urls=urls)
process.start()

df = pd.DataFrame({'names': names, 'links': ['https://www.zomato.com'+i for i in links]})
df.to_csv("Scraped_Restaurants.csv", index=False, mode='a')