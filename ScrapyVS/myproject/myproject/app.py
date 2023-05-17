from flask import Flask, render_template
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from myproject.items import ScrapyvsItem
from myspider import MySpider

app = Flask(__name__)
scrapy = ScrapyvsItem(app)


@app.route('/')
def home():
    process = CrawlerProcess(get_project_settings())
    process.crawl(MySpider)
    process.start()

    return render_template('home_page.html')


@app.route('/search')
def search():
    return render_template('search_bar.html')


if __name__ == '__main__':
    app.run()
