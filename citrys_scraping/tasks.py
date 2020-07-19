from __future__ import absolute_import, unicode_literals
from celery import shared_task, task
from .scraper import find_notebook, find_iphone



url_iphone = 'https://www.citrus.ua/'
url_notebook = 'https://www.citrus.ua/noutbuki-i-ultrabuki/'


@task
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


