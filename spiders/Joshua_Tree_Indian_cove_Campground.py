from National_Park_Project.items import National_Park_ProjectItem 
from scrapy import Spider

class National_Park_ProjectSpider(Spider):
    name = "Joshua_Tree_Indian_Cove_Campground"
    allowed_urls = ['https://www.recreation.gov']
    start_urls = ['https://www.recreation.gov/campsitePaging.do?contractCode=NRSO&parkId=70952&startIdx='+str(i) for i in range(0,125,25)]
  
    def parse(self,response):
        review_t = response.xpath("//tr[@class='br']")

        for i in review_t: 
    
            Site = i.xpath('./td/div/a/text()').extract()
            Facility_Area = i.xpath('(./td)[2]/text()').extract()
            SiteType = i.xpath('(./td)[3]/text()').extract()
            Maximum_Number_of_People = i.xpath('(./td)[4]/text()').extract()
            Equiplength_or_Driveway = i.xpath('(./td)[5]/text()').extract()
            Pets =i.xpath("(./td/div[@class='amenitiesicons']/img)[3]/@title").extract()
        
            item = National_Park_ProjectItem()
            item['ParkName']=['Joshua Tree']
            item['Location']= ['Indian Cove Campground']
            item['Longtitude']= ['-116.159443']
            item['Latitude']= ['34.094906']
            item['Stars'] = ['4.7']
            item['Reviews'] = ['899']
            item['Site'] = Site
            item['Facility_Area'] = Facility_Area
            item['SiteType'] =SiteType
            item['Maximum_Number_of_People'] = Maximum_Number_of_People
            item['Equiplength_or_Driveway'] = Equiplength_or_Driveway
            item['Pets'] = Pets

            yield item
