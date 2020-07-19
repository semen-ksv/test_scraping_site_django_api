from bs4 import BeautifulSoup
from requests_html import HTMLSession
from celery.utils.log import get_task_logger
from peewee import *

logger = get_task_logger(__name__)

db = PostgresqlDatabase('my_database', user='postgres')

session = HTMLSession()
user_agent = ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) '
              'Gecko/20100101 Firefox/50.0')

RELEVANT_PRICE = 25000
RELEVANT_NAME = 'Apple iPhone'

url_iphone = 'https://www.citrus.ua/'
url_notebook = 'https://www.citrus.ua/noutbuki-i-ultrabuki/'


class Citrys_scraping_productItem(Model):
    """Use the same table as ProdactItem model"""

    name = CharField(max_length=150)
    type = TextField()
    link = TextField()
    image_link = TextField()
    price = IntegerField()
    cashback = IntegerField()
    specifications = TextField(null=True)
    product_html = TextField()

    class Meta:
        database = db


def create_db():
    """Connect to database and create table if it doesn't exist"""
    db.connect()
    db.create_tables([Citrys_scraping_productItem])

def find_iphone(url):
    """pars Iphones from citrus.ua"""
    logger.info("Start parsing phone")
    request_page = session.get(url, headers={'User-Agent': user_agent})
    request_page.html.render()
    request_page = request_page.html.html
    soup = BeautifulSoup(request_page, features="lxml")
    all_products_carts = soup.find_all('div', {'class': 'product-card'})
    for product_cart in all_products_carts:
        try:
            cart = product_cart.find('div', {'class': 'product-card__name'})
            product_name = cart.find('a').get('title')
            product_price = int(product_cart.find('span', {'class': 'price'}).text.replace(' ', ''))
            if RELEVANT_NAME in product_name and product_price > RELEVANT_PRICE:
                product_item_link = 'https://www.citrus.ua/' + cart.find('a').get('href')
                product_image_link = product_cart.find('img', {'title': product_name}).get('data-src')

                product_cashback = int(product_cart.find('span', {'class': 'value'}).text.strip(' ₴'))

                Citrys_scraping_productItem.get_or_create(
                    name=product_name,
                    type='iPhone',
                    link=product_item_link,
                    image_link=product_image_link,
                    price=product_price,
                    cashback=product_cashback,
                    specifications='product_specifications',
                    product_html=cart
                )
        except AttributeError as e:
            print(e)
    logger.info("Finish parsing notebook")


def find_notebook(url):
    """pars notebook from citrus.ua"""
    logger.info("Start parsing single page")
    request_page = session.get(url, headers={'User-Agent': user_agent})
    request_page.html.render()
    request_page = request_page.html.html
    soup = BeautifulSoup(request_page, features="lxml")

    all_products_carts = soup.find_all('div', {'class': 'product-card'})

    for product_cart in all_products_carts:
        try:
            cart = product_cart.find('div', {'class': 'product-card__name'})
            product_price = int(product_cart.find('span', {'class': 'price'}).text.replace(' ', ''))
            if product_price > RELEVANT_PRICE:
                product_name = cart.find('a').get('title')
                product_item_link = 'https://www.citrus.ua/' + cart.find('a').get('href')
                product_image_link = product_cart.find('img', {'title': product_name}).get('data-src')

                product_cashback = int(product_cart.find('span', {'class': 'value'}).text.strip(' ₴'))
                product_specifications_html = product_cart.find('div', {'class': 'product-card__properties'})
                product_specifications_name = product_specifications_html.find_all('span', {'class': 'item__name'})
                product_specifications_value = product_specifications_html.find_all('span', {'class': 'item__value'})
                product_specifications = ''
                for name, value in zip(product_specifications_name, product_specifications_value):
                    product_specifications += f'{name.text} - {value.text}; '

                Citrys_scraping_productItem.get_or_create(
                    name=product_name,
                    type='Notebook',
                    link=product_item_link,
                    image_link=product_image_link,
                    price=product_price,
                    cashback=product_cashback,
                    specifications=product_specifications,
                    product_html=cart
                )
        except AttributeError as e:
            print(e)
    logger.info("Finish parsing single page")


def pars_all_pages_with_notebooks(url):
    """find last page in pagination and start parsing all page with notebooks"""

    logger.info("Start parsing notebook")
    request_page = session.get(url, headers={'User-Agent': user_agent})
    request_page.html.render()
    request_page = request_page.html.html
    soup = BeautifulSoup(request_page, features="lxml")
    pagination = soup.find('div', {'class': 'pagination-container'})
    last_item = pagination.find_all('li', {'class': 'skip'})[1].next.next.next
    last_page = int(last_item.find('a').text)

    for number in range(1, last_page+1):
        url = f'https://www.citrus.ua/noutbuki-i-ultrabuki/page_{str(number)}/'
        print(url)
        find_notebook(url)

    logger.info("Finish parsing notebook")


def main():

    """main function that start parsing all pages"""
    logger.info("Start scrap")
    create_db()
    find_iphone(url_iphone)
    pars_all_pages_with_notebooks(url_notebook)
    logger.info("Finish scraping")

