import streamlit as st
import pickle
from nltk.stem import PorterStemmer
import re


model = pickle.load(open('model.pkl','rb'))
tfidf = pickle.load(open('tfidf.pkl','rb'))

ps = PorterStemmer()

def stemming(text):
    lst = []
    text = re.sub(r'[^a-zA-Z0-9 ]'," ",text)
    for i in text.split():
        lst.append(ps.stem(i))
    return " ".join(lst)

st.title('Spam Classifier')

text = st.text_area("Enter the message below")
final = ""
if st.button("Predict"):
    transform = stemming(text)
    vector = tfidf.transform([transform])
    result = model.predict(vector)
    if result == 1:
        st.header('Spam')
    else:
        st.header('Not Spam')
        st.header('Not Spam')




