import datetime
import logging

from service_monitoring.celery import app

logger = logging.getLogger(__name__)


@app.task(queue="default")
def print_smth():
    logger.debug(f"Сейчас {datetime.datetime.hour} : {datetime.datetime.minute} ")
