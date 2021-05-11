import boto3
from contextlib import closing

client = boto3.client("polly")


response = client.synthesize_speech(
    OutputFormat = 'mp3',
    LanguageCode = "es-MX",
    Text = "Hola",
    TextType = "text",
    VoiceId = "Cristiano"
)


print(response)

if "AudioStream" in response:
    with closing(response["AudioStream"]) as stream:
        output = "prolly-test.mp3"
        try:
            with open(output, "wb") as file:
                file.write(stream.read())
        except Exception as e:
            print(e)
