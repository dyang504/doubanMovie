# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanPipeline(object):
    def process_item(self, item, spider):
        if Movie.table_exists() == False:
            Movie.create_table() 
        mv = Movie(name=item['name'],url=item['url'],score = item['score'])
                                                    
        mv.save()
                                                                 
        return item
