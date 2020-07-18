from bs4 import BeautifulSoup
from requests_html import HTMLSession

from citrys_scraping.models import ProductItem

session = HTMLSession()
user_agent = ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) '
              'Gecko/20100101 Firefox/50.0')

RELEVANT_PRICE = 25000
RELEVANT_NAME = 'Apple iPhone'


def find_iphone(url):
    request_page = session.get(url, headers={'User-Agent': user_agent})
    request_page.html.render()
    request_page = request_page.html.html
    soup = BeautifulSoup(request_page, features="lxml")
    print('skraper')
    all_products_carts = soup.find_all('div', {'class': 'product-card'})
    for product_cart in all_products_carts:
        try:
            cart = product_cart.find('div', {'class': 'product-card__name'})
            product_name = cart.find('a').get('title')
            if RELEVANT_NAME in product_name:
                product_item_link = 'https://www.citrus.ua/' + cart.find('a').get('href')
                product_image_link = product_cart.find('img', {'title': product_name}).get('data-src')
                product_price = int(product_cart.find('span', {'class': 'price'}).text.replace(' ', ''))
                product_cashback = int(product_cart.find('span', {'class': 'value'}).text.strip(' ₴'))

                # all_iphones.append({'name': product_name,
                #                       'link': product_item_link,
                #                       'image_link': product_image_link,
                #                       'prise': product_prise,
                #                       'cashback': product_cashback,
                #                       'product_html': cart})
                ProductItem.objects.get_or_create(
                    name=product_name,
                    type='iPhone',
                    link=product_item_link,
                    image_link=product_image_link,
                    price=product_price,
                    cashback=product_cashback,
                    product_html=cart
                )


        except AttributeError:
            print('attribute error')


def find_notebook(url):
    request_page = session.get(url, headers={'User-Agent': user_agent})
    request_page.html.render()
    request_page = request_page.html.html
    soup = BeautifulSoup(request_page, features="lxml")
    all_products_carts = soup.find_all('div', {'class': 'product-card'})
    print('skraper')
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

                # all_notebooks.append({'name': product_name,
                #                       'link': product_item_link,
                #                       'image_link': product_image_link,
                #                       'prise': product_prise,
                #                       'cashback': product_cashback,
                #                       'specifications': product_specifications,
                #                       'product_html': cart})
                ProductItem.objects.get_or_create(
                    name=product_name,
                    type='Notebook',
                    link=product_item_link,
                    image_link=product_image_link,
                    price=product_price,
                    cashback=product_cashback,
                    specifications=product_specifications,
                    product_html=cart
                )

        except AttributeError:
            print('attribute error')
