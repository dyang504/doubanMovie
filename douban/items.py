# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

from peewee import *

db = MySQLDatabase("douban",host='localhost',user='root',passwd = '123456')

class DoubanMovieItem(scrapy.Item):
        name = scrapy.Field()
        url = scrapy.Field()
        score = scrapy.Field()
                    
class Movie(Model):
        id = PrimaryKeyField()
        name = CharField(verbose_name='Movie Name',max_length=50,null=False,unique=False)
        url = CharField(verbose_name="Detail link",null=False)
        score = FloatField(verbose_name="Rate",null=False,unique=False)
                                            
class Meta:
        database = db
