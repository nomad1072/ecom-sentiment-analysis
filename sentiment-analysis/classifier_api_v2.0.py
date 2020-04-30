from flask import Flask, jsonify, request
# from flask_cors import CORS, cross_origin
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from textblob import TextBlob
import json

# load model and saved variables
'''
Logistic Regression Classifier - Accuracy: 85.06
'''
with open('./LogReg_SA_K3.pickle', 'rb') as f:
    clf = pickle.load(f)

# count vectorizer
with open('./LogReg_SA_K3_vectorizer.pickle', 'rb') as f:
    vectorizer = pickle.load(f)

def sentiment(review):
    features = vectorizer.transform([review])
    if clf.predict(features) == 2:
        return 'Positive'
    elif clf.predict(features) == 1:
        return 'Neutral'
    else:
        return 'Negative'

def sentiment_score(review):
    return TextBlob(review).sentiment.polarity

app = Flask(__name__)
# CORS(app)

@app.route('/api/v1/sentiment/', methods=['POST'])
def senitmentAnalysis():
    '''
    data = ['marketplace', 'customer_id', 'review_id', 'product_id',
            'product_parent', 'product_title', 'product_category', 'star_rating',
            'helpful_votes', 'total_votes', 'vine', 'verified_purchase',
            'review_headline', 'review_body', 'review_date', 'body_polarity',
            'label']
    '''
    data = request.json['data']
    review = data['review_body']

    # sentiment analysis
    pred = sentiment(review)
    pred_score = sentiment_score(review)

    pred_data = {
        'Sentiment': pred,
        'Score': pred_score
    }

    return json.dumps(pred_data)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port='5000')
