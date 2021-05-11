import time
import boto3
from celery import Celery
from celery.schedules import crontab

app = Celery(
    name="tasks",
    broker="redis://localhost:6379",
    backend="db+sqlite:///db.sqlite3"
)


client = boto3.resource(
    'sqs',
    aws_access_key_id='AKIAXII2BKO7O3P2CDEP',
    aws_secret_access_key='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',
    region_name='us-east-1'
)


@app.task()
def process_data_a(a, b):
    queue = client.get_queue_by_name(
        QueueName="urosario_test"
    )
    for message in queue.receive_messages(WaitTimeSeconds=1):
        print(message.body)
        message.delete()
    return a + b


@app.task()
def process_data_b(a, b):
    time.sleep(8)
    return a + b


def process():
    print("Procesando...")
    process_data_a.delay(5, 5)
    process_data_b.delay(3, 8)
    print("Le avisaremos al terminar...")


# Modelo que notifica cada cierto tiempo

app.conf.beat_schedule = {
    'add-every': {
        'task': 'main.process_data_a',
        'schedule': crontab(minute='*/1'),
        'args': (7, 4)
    }
}
