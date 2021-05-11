from typing import Optional
import boto3
from fastapi import Request
from fastapi import FastAPI
from pydantic import BaseModel


client = boto3.client(
    'sns',
    aws_access_key_id='AKIAXII2BKO7O3P2CDEP',
    aws_secret_access_key='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',
    region_name='us-east-1'
)


TOPIC_ARN = "arn:aws:sns:us-east-1:498807690174:scores_urosario"
ENDPOINT = 'https://327ccea522de.ngrok.io/listener'
app = FastAPI()


class Data(BaseModel):
    score: Optional[str] = None


def subscribe():
    response = client.subscribe(
        TopicArn=TOPIC_ARN,
        Protocol='https',
        Endpoint=ENDPOINT
    )
    return response


def confirm_subscribe(token):
    response = client.confirm_subscription(
        TopicArn=TOPIC_ARN,
        Token=token
    )
    return response


@app.get("/listener")
def read_root():
    print(publish())
    return {
        "subscribe": subscribe()
    }


@app.post("/listener", response_model=Data)
async def sus(request: Request, data: Data):
    print(dir(request.json))
    data = await request.json()
    print(data.get("Token"))
    if data.get("Token"):
        confirm_subscribe(data.get("Token"))
    else:
        print(data)
    return {"Hello": await request.json()}


def publish():
    response = client.publish(
        TopicArn=TOPIC_ARN,
        Message='("score_Alejandro": "123")',
        Subject='URosario Alejandro Uribe',
        MessageStructure='text'
    )
    print(response)


