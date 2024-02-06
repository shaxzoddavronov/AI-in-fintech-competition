import streamlit as st
import time
import tensorflow as tf
import numpy as np
import pandas as pd
import joblib
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import WordPunctTokenizer
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

def ChatBot():
    st.image('chatbot.png') 
    st.title('Chatbot')
    data=pd.read_csv('question_answer.csv')
    model=tf.keras.models.load_model('best_model.h5')
    vectorizer=joblib.load('tfidf_vectorizer.jbl')

    def get_prep_words(sample_quest):
        tokenizer=WordPunctTokenizer()
        tokenized=tokenizer.tokenize(sample_quest)
        lemmatizer=WordNetLemmatizer()
        stop_words=stopwords.words('english')
        stop_words.extend(['?','!',"'"])
        non_stop_words=[word.lower() for word in tokenized if word not in stop_words]
        base_words=[lemmatizer.lemmatize(word) for word in non_stop_words]
        return ' '.join(base_words)

    if 'messages' not in st.session_state:
        st.session_state.messages=[]

    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.markdown(message['content'])

    if prompt:=st.chat_input('Type here...'):
        with st.chat_message('user'):
            st.markdown(prompt)
        st.session_state.messages.append({'role':'user','content':prompt})
        sentence_prep=get_prep_words(prompt)
    if prompt:
        vectorized_prompt=vectorizer.transform([sentence_prep]).toarray()
        tag_value=np.argmax(model.predict(vectorized_prompt))
        answer=np.random.choice(np.array(data[data.label_tag==tag_value].answer))
#response = f"Bot: {prompt}"

        with st.chat_message("assistant"):
            message_placeholder=st.empty()
            full_response=""
            assistant_response=answer
            for chunk in assistant_response.split():
                full_response += chunk+" "
                time.sleep(0.05)
                message_placeholder.markdown(full_response+"▌")
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({'role':'assistant','content':full_response})

if __name__=="__main__":
    ChatBot() 