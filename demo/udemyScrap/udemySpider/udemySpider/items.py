# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UdemyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id=scrapy.Field()
    title=scrapy.Field()
    url=scrapy.Field()
    image_url=scrapy.Field()
    published_title=scrapy.Field()
    tracking_id=scrapy.Field()
    headline=scrapy.Field()



class AllCourseItem(scrapy.Item):
    avg_rating=scrapy.Field()
    avg_rating_recent=scrapy.Field()
    content_info=scrapy.Field()
