import streamlit as st
from PIL import Image
import joblib
import pandas as pd

model = joblib.load("model.jbl")

def loan_prediction(lang):
    img1 = Image.open('approved.png')
    img1 = img1.resize((700, 400))
    st.image(img1, use_column_width=False)
    st.title(lang['title'])

    # full name
    fn = st.text_input(lang['fullname'])

    # Number of dependents
    no_of_dependents = st.number_input(lang['dependents'], value=0)

    # education feature
    edu_display = ('Not Graduate', 'Graduate')
    edu_options = list(range(len(edu_display)))
    education = st.radio(lang['education'], edu_options, format_func=lambda x: edu_display[x])

    # employment feature
    emp_display = ('No', 'Yes')
    emp_options = list(range(len(emp_display)))
    self_employed = st.radio(lang['employment'], emp_options, format_func=lambda x: emp_display[x])

    # applicant income
    income_annum = st.number_input(lang['annual_income'], value=0)

    # Amount of loan
    loan_amount = st.number_input(lang['loan_amount'], value=0)

    # Term of loan
    loan_term = st.number_input(lang['loan_term'], value=0)

    # Cibil score
    cibil_score = st.number_input(lang['cibil_score'], value=0)

    # Residential assets value
    residential_assets_value = st.number_input(lang['residential_assets'], value=0)

    # Commercial assets value
    commercial_assets_value = st.number_input(lang['commercial_assets'], value=0)

    # Luxury assets value
    luxury_assets_value = st.number_input(lang['luxury_assets'], value=0)

    # Bank assets value
    bank_asset_value = st.number_input(lang['bank_assets'], value=0)

    if st.button(lang['submit']):
        # features
        data = {
            'no_of_dependents': no_of_dependents,
            'education': education,
            'self_employed': self_employed,
            'income_annum': income_annum,
            'loan_amount': loan_amount,
            'loan_term': loan_term,
            'cibil_score': cibil_score,
            'residential_assets_value': residential_assets_value,
            'commercial_assets_value': commercial_assets_value,
            'luxury_assets_value': luxury_assets_value,
            'bank_asset_value': bank_asset_value
        }

        index = [1]
        features = pd.DataFrame(data, index=index)
        ans = model.predict(features)[0]

        if ans == 0:
            st.error(f"Sorry {fn}, your request is rejected!")
        else:
            st.success(f"Congratulations {fn}, your request is approved!")




