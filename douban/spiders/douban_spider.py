import scrapy
from scrapy import Spider
from douban.items import DoubanMovieItem
from bs4 import BeautifulSoup
import re

class DoubanTopMovieSpider(Spider):
    
    name = 'DoubanTopMovie'
    headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'                
            }
                
    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield scrapy.Request(url,headers=self.headers)
                                        
    def parse(self,response):
        item = DoubanMovieItem()
                                
        soup = BeautifulSoup(response.text,'lxml')
        movies = soup.findAll('div',{'class':'item'})
      
        n = 0
        for movie in movies: 
            item['name'] = movie.find('span',{'class','title'}).get_text()     
            item['url'] = movie.find('a')['href']
            item['score'] = movie.find('span',{'class','rating_num'}).get_text()
            n=n+1
            yield item
            
        print(n)
        next_url = soup.find('span',{'class','next'}).find('a')['href']
        print(type(next_url),next_url)
        if next_url:    
            url = 'https://movie.douban.com/top250' + next_url
            yield scrapy.Request(url,headers=self.headers)
