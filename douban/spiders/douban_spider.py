import scrapy
from scrapy import Spider
from douban.items import DoubanMovieItem
from bs4 import BeautifulSoup

class DoubanTopMovieSpider(Spider):
    
    name = 'DoubanTopMovie'
    headers = {
                        'User-Agent':'Mozilla/5.0(Windows NT 10.0;Win64;x64)'
                            }
                
    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield scrapy.Request(url,headers=self.headers)
                                        
    def parse(self,response):
        item = DoubanMoviewItem()
                                
        soup = BeautifulSoup(response.text,'lxml')
        movies = soup.findAll('div',{'class':'item'})                                                                        
                                                                                    
                                                                                
        for movie in movies: 
            item['name'] = movie.find('span',{'class','title'}).get_text()     
            item['url'] = movie.find('a')['href']
            item['score'] = movie.find('span',{'class','rating_num'}).get_text()
            
            yield item
            
        next_url = soup.find('span',{'class','next'}).find('a')['href']
        if next_url:    
            url = 'https://movie.douban.com/top250' + next_url 
            yield scrapy.Request(url,headers=self.headers)
