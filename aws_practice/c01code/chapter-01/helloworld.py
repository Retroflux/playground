# This example shows a basic API call to AWS

# Load the AWS Python SDK
import boto3

# Configure Polly client *implicitly*
polly = boto3.client('polly')

# Call the Amazon Polly Web Service
result1 = polly.synthesize_speech(Text='Hello World!',
                                 OutputFormat='mp3',
                                 VoiceId='Matthew')
result2 = polly.synthesize_speech(Text='Hello Virtual World!',
                                 OutputFormat='mp3',
                                 VoiceId='Kendra')

# Save the Audio File
audio = result1['AudioStream'].read()
with open("helloworld.mp3","wb") as file:
    file.write(audio)
audio = result2['AudioStream'].read()
with open("hellovirtualworld.mp3","wb") as file:
    file.write(audio)