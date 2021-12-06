import scrapy  
from scrapy.crawler import Crawler
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
import pandas as pd
import sys
import os
import numpy as np

ratings = []

class RankingGenerator(scrapy.Spider):
  name = 'RankingGenerator'
  def parse(self, response):
    global ratings
    data = str(response.body)
    data = data.split('{"author":"')[1:]
    data[-1] = data[-1][:data[-1].index('</script>')]
    for i in data:
      name = i[:i.index('",')]
      description = i[i.index('"description":"')+len('"description":"'):]
      description = description[:description.index('",')]
      value = i[i.index('"ratingValue":')+len('"ratingValue":'):]
      value = value[:value.index(',"')]
      ratings.append([name, description, value])

url, name = sys.argv[1].strip(), ' '.join(sys.argv[2:]).strip()
urls = [url]

process = CrawlerProcess({'USER_AGENT': 'Mozilla/5.0'})
process.crawl(RankingGenerator, start_urls=urls)
process.start()
ratings = np.array(ratings)
df = pd.DataFrame({'r_name': np.array([name for _ in range(len(ratings))]), 'name': ratings.T[0], 'review': ratings.T[1], 'rating': ratings.T[2]})
df.to_csv("r.csv", index=False, mode='a', header=False)