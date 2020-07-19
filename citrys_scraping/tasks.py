from __future__ import absolute_import, unicode_literals
from celery import task
from .scraper import main
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)

@task
def scrape_cur():
    logger.info("Start task")
    main()
    return




