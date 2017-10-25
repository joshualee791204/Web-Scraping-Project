from National_Park_Project.items import National_Park_ProjectItem 
from scrapy import Spider

class National_Park_ProjectSpider(Spider):
    name = "Yosemite_Crane_Flat"
    allowed_urls = ['https://www.recreation.gov']
    start_urls = ['https://www.recreation.gov/campsitePaging.do?contractCode=NRSO&parkId=70930&startIdx='+str(i) for i in range(0,175,25)]
  
    def parse(self,response):
        review_t = response.xpath("//tr[@class='br']")

        for i in review_t:
        #top_list = response.xpath('//*[@id="HEADING"]/text()').extract()
        #rating = response.xpath('//*[@id="taplc_location_detail_overview_attraction_0"]/div[1]/div[2]/div[2]/div[2]/div[1]/span/text()').extract_first() 
    
            Site = i.xpath('./td/div/a/text()').extract()
            Facility_Area = i.xpath('(./td)[2]/text()').extract()
            SiteType = i.xpath('(./td)[3]/text()').extract()
            Maximum_Number_of_People = i.xpath('(./td)[4]/text()').extract()
            Equiplength_or_Driveway = i.xpath('(./td)[5]/text()').extract()
            Pets =i.xpath("(./td/div[@class='amenitiesicons']/img)[3]/@title").extract()

        #for review in reviews:
        #   raw_review = review.xpath('.//div[@class="review-body with-review-wrapper"]/text()').extract()
        #   raw_review = ''.join(raw_review).strip()
            item = National_Park_ProjectItem()
            item['ParkName']=['Yosemite']
            item['Location']= ['Crane Flat Campground']
            item['Longtitude']= ['-119.799632']
            item['Latitude']= ['37.748084']
            item['Stars'] = ['3.9']
            item['Reviews'] = ['1797']
            item['Site'] = Site
            item['Facility_Area'] = Facility_Area
            item['SiteType'] =SiteType
            item['Maximum_Number_of_People'] = Maximum_Number_of_People
            item['Equiplength_or_Driveway'] = Equiplength_or_Driveway
            item['Pets'] = Pets

            yield item


