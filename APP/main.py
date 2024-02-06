import streamlit as st
from page1 import loan_prediction
from page2 import chatBot
from language import english_translator,uzbek_translator,russian_translator

def main():
    st.sidebar.title('Select Language/Tilni Tanlang')
    lang_select=st.sidebar.radio('Languages',['en','ru','uz'])
    def choose_project(language):
        st.sidebar.title(language['sidebar title'])
        pages = [language['page_1'],language['page_2']]
        selection = st.sidebar.radio(language['sidebar ratio'], pages)
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        if selection==pages[0]:
            lang=english_translator()
            if lang_select=='ru': lang=russian_translator()
            elif lang_select=='uz': lang=uzbek_translator()
            loan_prediction(lang)
        else:
            lang=english_translator()
            if lang_select=='ru': lang=russian_translator()
            elif lang_select=='uz': lang=uzbek_translator() 
            chatBot()
    language=english_translator()        
    if lang_select=='ru':
        language=russian_translator()        
    elif lang_select=='uz':
        language=uzbek_translator()
        
    choose_project(language)
if __name__ == "__main__":
    main()