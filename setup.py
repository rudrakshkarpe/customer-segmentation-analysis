import streamlit as st
import app.customer_segmentation as WebApp

st.sidebar.title('Menu')
Page_user = st.sidebar.selectbox(

'Choice',['Prediction for Customer Segmentation'] 
)

if Page_user == 'Prediction for Customer Segmentation':
    WebApp.code()
