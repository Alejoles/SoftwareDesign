import json


def hello(event, context):

    response = {
        "statusCode": 200,
        "body": "Hola laboratorio 10"
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
