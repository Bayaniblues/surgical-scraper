import scrapy
from ..items import SurgtechItem


class QuizSpider(scrapy.Spider):
    name = 'quiz'
    start_urls = ['https://gotestprep.com/certified-surgical-technologist-practice-test-1/']

    def parse(self, response):
        items = SurgtechItem()
        question = response.css('p strong , #question-container strong').extract()
        answer = response.css('.su-u-trim , .su-u-trim p').extract()

        items['scraped_question'] = question
        items['scraped_answer'] = answer

        yield items
