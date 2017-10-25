from National_Park_Project.items import National_Park_ProjectItem 
from scrapy import Spider

class National_Park_ProjectSpider(Spider):
    name = "National_Parks_List"
    allowed_urls = ['https://en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_national_parks_of_the_United_States']
  
    def parse(self,response):
        review_t = response.xpath('//table[starts-with(@class,"wikitable")]//tr')

        for i in review_t: 
            ParkName = i.xpath('.//th/a/@title').extract_first()
            Location = i.xpath('.//td[2]/a/@title').extract_first()
            #Longtitude = i.xpath('.//tr//td[2]/small/span/span/a/span[3]/span/span/text()').extract()
            Number_of_Visitors = i.xpath('.//td[5]//text()').extract_first()
            #Equiplength_or_Driveway = i.xpath('(./td)[5]/text()').extract()
            #Pets =i.xpath("(./td/div[@class='amenitiesicons']/img)[3]/@title").extract()
        
            item = National_Park_ProjectItem()
            item['ParkName']=ParkName
            item['Location']= Location
            item['Number_of_Visitors']= Number_of_Visitors
            #item['Latitude']= ['37.739442']
            #item['Stars'] = ['4.5']
            #item['Reviews'] = ['879']
            #item['Site'] = Site
            #item['Facility_Area'] = Facility_Area
            #item['SiteType'] =SiteType
            #item['Maximum_Number_of_People'] = Maximum_Number_of_People
            #item['Equiplength_or_Driveway'] = Equiplength_or_Driveway
            #item['Pets'] = Pets

            yield item


