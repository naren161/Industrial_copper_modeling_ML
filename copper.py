import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load the dataset to get unique values
df = pd.read_csv(r"E:\Naren Baskar\indus new\Industrial_Copper_proper.csv")

# Load the pre-trained regression model for price prediction
with open(r'E:\Naren Baskar\indus new\regression_model.pkl', 'rb') as model_file:
    reg_model = pickle.load(model_file)

# Load the pre-trained classification model for status prediction
with open(r'E:\Naren Baskar\indus new\Classification_model_copper.pkl', 'rb') as status_model_file:
    status_model = pickle.load(status_model_file)

# Extract unique values for various fields
customer_ids = df['customer'].unique().tolist()
country_codes = df['country'].unique().tolist()
item_types = df['item_type'].unique().tolist()
applications = df['application'].unique().tolist()
product_refs = df['product_ref'].unique().tolist()
status = df['status'].unique().tolist()

# Set up the Streamlit page
st.set_page_config(page_title="Copper Price and Status Prediction", layout="wide")
st.header("Copper Price and Status Prediction")

# Create tabs for Price Prediction and Status Prediction
t1, t2 = st.tabs(["Price Prediction", "Status Prediction"])

# Price Prediction Tab
with t1:
    st.subheader("Predict Selling Price")
    customer = st.selectbox('Customer ID', customer_ids, key='customer_price')
    quantity_tons = st.number_input('Quantity in Tons', min_value=0.0, key='quantity_price')
    country = st.selectbox('Country Code', country_codes, key='country_price')
    item_type = st.selectbox('Item Type', item_types, key='item_type_price')
    application = st.selectbox('Application Code', applications, key='application_price')
    thickness = st.number_input('Thickness of Copper', min_value=0.0, key='thickness_price')
    width = st.number_input('Width of Copper', min_value=0.0, key='width_price')
    product_ref = st.selectbox('Product Reference', product_refs, key='product_ref_price')
    no_of_days = st.number_input('Number of Days for Delivery', min_value=1, key='no_of_days_price')
    status = st.selectbox(label="**Enter the Value for STATUS**", options=[0, 1])

    # Predict button
    if st.button("Predict Price"):
        # Prepare input data for price prediction
        input_data_price = np.array([[quantity_tons, customer, country, item_type, 
                                       application, thickness, width, product_ref, no_of_days,status]])

        # Make price prediction
        predicted_log_price = reg_model.predict(input_data_price)

        # Convert from log scale to original scale
        predicted_price = np.exp(predicted_log_price)

        # Output the predicted selling price
        st.write(f"The predicted selling price is: {predicted_price[0]:.2f}")
    
    
# Status Prediction Tab
with t2:
    st.subheader("Predict Status")
    customer = st.selectbox('Customer ID', customer_ids, key='customer_status')
    quantity_tons = st.number_input('Quantity in Tons', min_value=0.0, key='quantity_status')
    country = st.selectbox('Country Code', country_codes, key='country_status')
    item_type = st.selectbox('Item Type', item_types, key='item_type_status')
    application = st.selectbox('Application Code', applications, key='application_status')
    thickness = st.number_input('Thickness of Copper', min_value=0.0, key='thickness_status')
    width = st.number_input('Width of Copper', min_value=0.0, key='width_status')
    product_ref = st.selectbox('Product Reference', product_refs, key='product_ref_status')
    no_of_days = st.number_input('Number of Days for Delivery', min_value=1, key='no_of_days_status')
    selling_price = st.number_input('Selling Price', min_value=0.0, key='selling_price_status')

    # Predict button
    if st.button("Predict Status"):
        # Prepare input data for status prediction
        input_data_status = np.array([[quantity_tons, customer, country, 
                                        item_type, application, thickness, width, product_ref, selling_price, no_of_days]])

        # Make status prediction
        predicted_status = status_model.predict(input_data_status)
        status_message = "The predicted status is Won" if predicted_status[0] == 1 else "The predicted status is Lost"
        st.write(status_message)