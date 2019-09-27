from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


client = language.LanguageServiceClient()

# text
def google_nltk(texts):
    scores = []
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
    return scores

if __name__ == '__main__':
    #pass in the username of the account you want to download
    google_nltk(["This is bad", "excellent", "iphone 11 is horrible"])
    