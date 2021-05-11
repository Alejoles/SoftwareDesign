import boto3


client = boto3.resource(
    'sqs',
    aws_access_key_id='AKIAXII2BKO7O3P2CDEP',
    aws_secret_access_key='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',
    region_name='us-east-1'
)


queue = client.get_queue_by_name(
    QueueName="urosario_test"
)


for message in queue.receive_messages(WaitTimeSeconds=1):
    print(message.body)
