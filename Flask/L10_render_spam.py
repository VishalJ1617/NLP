from flask import Flask, render_template, request
import joblib
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string
from nltk import pos_tag

app = Flask(__name__)
stop=stopwords.words('english')
wnl=WordNetLemmatizer()

def clean_text(text):
    tokens1=word_tokenize(text)
    tokens2=[i.lower() for i in tokens1 if i.isalpha() or i.isdigit()]
    tokens3=[i for i in tokens2 if i not in stop]
    tokens4=[]
    tags=pos_tag(tokens3)
    for word in tags:
        if word[1].startswith('N'):
            tokens4.append(wnl.lemmatize(word[0],pos='n'))
        if word[1].startswith('V'):
            tokens4.append(wnl.lemmatize(word[0],pos='v'))
        if word[1].startswith('R'):
            tokens4.append(wnl.lemmatize(word[0],pos='r'))
        if word[1].startswith('J'):
            tokens4.append(wnl.lemmatize(word[0],pos='a'))
    return tokens4


classifier=joblib.load('model.bin')
tfidf=joblib.load('vectorizer.bin')

@app.route('/')
def student():
    return render_template('L10_Homepage_spam.html')

@app.route('/spamfinder', methods = ['GET', 'POST'])
def result():
    if request.method == 'POST':
        data= dict(request.form)
        message = tfidf.transform([data['message']])
        data['result']=classifier.predict(message)[0]
    return render_template('L10_spam_output.html',data=data)


if __name__ == '__main__':
    app.run(debug = True)