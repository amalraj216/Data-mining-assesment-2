import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

#https://www.bayut.com/to-rent/property/dubai/
#https://www.bayut.com/property/details-9232474.html
# no permit number in any fields

class Dataspider(CrawlSpider):
    name='Data'
    allowed_domains = ['bayut.com']
    start_urls =['https://www.bayut.com/to-rent/property/dubai/']

    rules = (
        Rule(LinkExtractor(allow='property/dubai/', deny='details')),
        Rule(LinkExtractor(allow='details'), callback='parse_item')
    )



    def parse_item(self, response):

        # abc = response.css('span._2fdf7fc5::text').getall()
        pull = response.css('span._2fdf7fc5')

        pulla = pull[2].css('::text').get()
        pullak = pull[1].css('::text').get()
        type = pull[0].css('::text').get()
        added = pull[5].css('::text').get()
        furnish = pull[3].css('::text').get()



        yield{
            'property_id':pulla,
            'purpose':pullak,
            'type':type,
            'added_on':added,
            'furnishing':furnish,
            # 'Type': response.css('span._2fdf7fc5::text').get(),
            'Price AED':response.css('span._2d107f6e::text').get(),
            'Location': response.css('div.e4fd45f0::text').get(),
            'bed_bath_size':response.css('span._140e6903::text').getall(), 
            'permit_number': 'none', 
            # 'Price AED':response.css('span._2d107f6e::text').get(),
            'agent_name': response.css('a.d2d04ff3::text').get(),
            'image_url':response.css('img._4a3dac18::attr(src)').get(),
            'breadcrumbs':response.css('span._43ad44d9::text').getall(),
            'amenities':response.css('span._7181e5ac::text').getall(),
            'description':response.css('span._3547dac9::text').getall()    

        }
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            