# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class National_Park_ProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ParkName = scrapy.Field()
    Location = scrapy.Field()
    Longtitude = scrapy.Field()
    Latitude = scrapy.Field()
    Stars = scrapy.Field()
    Reviews = scrapy.Field()
    Site = scrapy.Field()   
    Facility_Area = scrapy.Field()
    SiteType = scrapy.Field()
    Maximum_Number_of_People = scrapy.Field()
    Equiplength_or_Driveway = scrapy.Field()
    Pets= scrapy.Field()
    