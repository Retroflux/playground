# This example shows regional isolation of data

import boto3

# note that this is what is overriding the region, causing the LexiconNotFoundException
# This is because there is no lexicon in the eu-west-2 region currently. Add it with
#    aws polly put-lexicon --name awsLexicon --content file://aws-lexicon.xml --region eu-west-2
#        aws polly put-lexicon: indicates a push of a lexicon to a server
#        --name awsLexicon: gives the file a name
#        --content file://aws-lexicon.xml: points to the file that needs to be pushed
#        --region eu-west-2: specifies the region to push to, overriding the default (us-east-1)
# Running this command and then this script removes the issues.
polly = boto3.client('polly', region_name="eu-west-2")
result1 = polly.synthesize_speech(Text='Hello AWS',
                                 OutputFormat='mp3',
                                 VoiceId='Joanna',
                                 LexiconNames=['awsLexicon']) #remove this to run it without the lexicon
result2 = polly.synthesize_speech(Text='Hello AWS on the Web',
                                 OutputFormat='mp3',
                                 VoiceId='Joanna',
                                 LexiconNames=['awsLexiconBig']) #remove this to run it without the lexicon

#Without lexicon checking
# result = polly.synthesize_speech(Text='Hello AWS After Lexicon Delete!',
#                                  OutputFormat='mp3',
#                                  VoiceId='Aditi')

# Read the bytes from the Audio Stream in the response
audio = result1['AudioStream'].read()

with open("helloaws.mp3","wb") as file:
    file.write(audio)

audio = result2['AudioStream'].read()

with open("helloawsBig.mp3","wb") as file:
    file.write(audio)


# with open("helloawsWithoutLexicon.mp3","wb") as file:
#     file.write(audio)