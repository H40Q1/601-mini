from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


client = language.LanguageServiceClient()

# text
text1 = u'test text here!'
text2 = u'try the second one'
text3 = u'I feel good today'
texts=[]
texts.append(text1)
texts.append(text2)
texts.append(text3)
scores=[]
for text in texts:
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    #sentiment feedback
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    print('Text: {}'.format(text))
    print("Sentiment Score:", sentiment.score)
 
    scores.append(sentiment.score)


    #sentiment level
    if sentiment.score <=1 and sentiment.score>=0.7:
        print("Sentiment level: Very Happy")

    elif sentiment.score <0.7 and sentiment.score>=0.3:
        print("Sentiment level: Happy")

    elif sentiment.score<0.3 and sentiment.score>=-0.3:
        print("Sentiment level: OK")

    else:
        print("Sentiment level: Disatified")

