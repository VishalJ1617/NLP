from flask import Flask, render_template, request
import joblib
from keras.preprocessing.text import Tokenizer
from nltk.corpus import stopwords
import string
from nltk import pos_tag
import re


app = Flask(__name__)
stop_words=stopwords.words('english')

# fit a tokenizer
def create_tokenizer(lines):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(lines)    
    return tokenizer

tokenizer = joblib.load('tokenizer.bin')

def clean_doc(doc):
    #Split ino tokens by white space
    tokens=doc.split()
    #Prepare regax for char filtering
    re_punc=re.compile('[%s]' % re.escape(string.punctuation))
    #remove punctuation from each words
    tokens=[re_punc.sub('',w)for w in tokens]
    #remove remaining tokens that are not alphabetic
    tokens=[word for word in tokens if word.isalpha()]
    #filter out stop words
    stop_words=set(stopwords.words('english'))
    tokens=[w for w in tokens if not w in stop_words]
    #Filter out short tokens
    tokens=[word for word in tokens if len(word)>1]
    return tokens

def predict_sentiment(review):
    #clean
    token = clean_doc(review)
    #convert to line
    line = ' '.join(token)
    #encode
    encoded = tokenizer.texts_to_matrix((line), mode = 'binary')
    #predict sentiment
    yhat = sentiment_analyser.predict(encoded, verbose = 0)
    # retrieve predicted percentage and label
    percent_pos = yhat[0,0]
    if round(percent_pos) == 0:
        return (1 - percent_pos), 'NEGATIVE'
    return percent_pos, 'POSITIVE'


sentiment_analyser = joblib.load('Sentiment_model.bin')  #

@app.route('/') #
def student(): #
    return render_template('L10_Homepage_sentiment_analysis.html')  #

@app.route('/SentimentFinder', methods = ['GET', 'POST'])
def result():
    if request.method == 'POST':
        message = {}
        message['message'] =  request.form['message']
        per, review = predict_sentiment(message['message'])
        message['percentage'] = per
        message['review'] = review
    return render_template('L10_Sentiment_analysis_output.html',data=message)  #


if __name__ == '__main__':
    app.run(debug = True)