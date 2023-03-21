from re import X
from celery import Celery
from random import randint

app = Celery(broker='redis://127.0.0.1:6379/0')

@app.task(bind = True, max_retry=3, default_retry_delay=2, autoretry_for = (ZeroDivisionError, ValueError))
def exibir(self):
    x = randint(1,9)
    if x > 7:
        return x
    else:
        raise ValueError('Erro')
    # x = randint(1, 10)
    # if x > 5:
    #     return 'OK'
    # else: 
    #     self.retry()
    #     raise Exception('Erro')
