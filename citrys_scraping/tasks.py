from __future__ import absolute_import, unicode_literals
from celery import Celery, shared_task
from .scraper import find_notebook, find_iphone
import time

app = Celery()

url_iphone = 'https://www.citrus.ua/'
url_notebook = 'https://www.citrus.ua/noutbuki-i-ultrabuki/'


@app.task
def scrape_cur():
    print('task')
    find_notebook(url_notebook)
    # find_iphone()
    return


@shared_task
def scrape_async():
    print('task')
    find_notebook(url_notebook)
    # find_iphone()
    return


@app.task
def some():
    print('som')
    time.sleep(3)
    print('fin')
