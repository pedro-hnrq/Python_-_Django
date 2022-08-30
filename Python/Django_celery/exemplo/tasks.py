from celery import shared_task
from time import sleep

@shared_task
def minha_tarefa():
    sleep(5)
    return 'teste'