
import pickle 
import pandas as pd
import streamlit as st
from pathlib import Path
import os


def header():
    current_directory = Path(__file__).parent 
    file = open(os.path.join(current_directory, 'trained_model.sav'), 'rb') # rb for read binary
     
    loaded_model = pickle.load(file)
    
    st.write("""
    ## Customer segmentation prediction""")    
    return loaded_model



def point_prediction(input_data, loaded_model):
    prediction = loaded_model.predict(input_data)

    if prediction == 0:
        st.markdown(''' #### Group 1 Profile:
                        ''')
        st.write("""In this group, the average quantity of goods ordered is approximately 27.5, with an average price of around $100 per item.Total purchases amount to roughly 3000 dollars, with the majority of transactions occurring in December.Classic cars are the most frequently purchased product line within this group, and agreements with individuals tend to be of medium to small scale.""")

    elif prediction == 1:
        st.markdown(''' #### Group 2 Profile:
                        ''')
        st.write("""This group typically orders an average quantity of goods around 45, with most purchases falling in the $100 price range. Total purchases amount to about 4000 dollars, with a higher frequency of transactions in December.Classic cars are the most popular product line within this group, and agreements are generally of medium size.""")

    else:
        st.markdown(''' #### Group 3 Profile:
                        ''')
        st.write("""In this group, the average quantity of merchandise ordered is around 30, with purchases primarily in the $65 price range. Total purchases amount to approximately 1600 dollars, with a preference for buying in December. Vintage cars are the most frequently purchased product line within this group, and agreements are typically small.""")
    
    
def code():
    loaded_model = header()

    form = st.form(key='dados')
    
    QUANTITYORDERED = form.number_input('How many products does the customer typically order?', key='1', min_value=0, value=45, step=1)
    
    PRICEEACH = form.number_input('Approximately, how much does each product cost?', value=100, key='2')
    
    STATUS = form.selectbox("What is the typical status of the customer's orders?", ['Shipped', 'Cancelled', 'Resolved', 'On Hold', 'In Process', 'Disputed'], key='3')
    
    MONTH_ID = form.number_input('In which month are orders usually placed?', key='4', min_value=0, max_value=12, value=12, step=1)
    
    PRODUCTLINE = form.selectbox("Which product line does the customer usually purchase from?", ['Classic Cars', 'Vintage Cars', 'Motorcycles', 'Planes', 'Trucks and Buses', 'Ships', 'Trains'], key='5')
    
    MSRP = form.number_input("Is the manufacturer's suggested retail price known to the customer?", value=100, key=6)
    
    COUNTRY = form.selectbox("Which country is the customer from? If not listed, select the closest one.", ['USA', 'Spain', 'France', 'Australia', 'UK', 'Italy', 'Finland', 'Norway', 'Singapore', 'Canada', 'Denmark', 'Germany', 'Sweden', 'Austria', 'Japan', 'Belgium', 'Switzerland', 'Philippines', 'Ireland'], key=7)
    
    DEALSIZE = form.selectbox("How large is the deal?", ['Medium', 'Small', 'Large'], key=8)
    
    form.form_submit_button('Add')

    SALES = QUANTITYORDERED * PRICEEACH

    data = [[QUANTITYORDERED, PRICEEACH, SALES, STATUS, MONTH_ID, PRODUCTLINE, MSRP, COUNTRY, DEALSIZE]]
    columns = ['QUANTITYORDERED', 'PRICEEACH', 'SALES', 'STATUS', 'MONTH_ID', 'PRODUCTLINE', 'MSRP', 'COUNTRY', 'DEALSIZE']

    df = pd.DataFrame(data=data, columns=columns)

    if st.button('Result'):
        point_prediction(df, loaded_model)

if __name__ == '__main__':
    code()		
