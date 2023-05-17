import scrapy
from myproject.items import ScrapyvsItem
from scrapy.utils.project import get_project_settings


class MySpider(scrapy.Spider):
    name = "myspider"
    allowed_domains = ["developer.uspto.gov"]
    start_urls = [
        "https://developer.uspto.gov/products/bdss/get/ajax?data=%7B%22name%22%3A%22TRTDXFAP%22%7D"]

    def parse(self, response):
        links = response.json()['productFiles'][1:]
        for link in links:
            fileitem = ScrapyvsItem()
            fileitem['file_urls'] = [link['fileDownloadUrl']]
            yield fileitem
