import streamlit as st
import pickle
import numpy as np
from streamlit_option_menu import option_menu

# Function to predict status
def predict_status(country, item_type, application, width, product_ref, quantity_tons_log, customer_log, thickness_log, selling_price_log, item_date_day, item_date_month, item_date_year, delivery_date_day, delivery_date_month, delivery_date_year):
    # Convert input values to integers
    item_date_day_int = int(item_date_day)
    item_date_month_int = int(item_date_month)
    item_date_year_int = int(item_date_year)
    delivery_date_day_int = int(delivery_date_day)
    delivery_date_month_int = int(delivery_date_month)
    delivery_date_year_int = int(delivery_date_year)
    
    # Load classification model
    with open(r"C:\Users\Happy\Desktop\Naren Baskar\New folder\Industrial_Classification_model.pkl","rb") as f:
        model_class = pickle.load(f)
    
    # Prepare user data for prediction
    user_data = np.array([[country, item_type, application, width, product_ref, quantity_tons_log, customer_log, thickness_log, selling_price_log,
                           item_date_day_int, item_date_month_int, item_date_year_int, delivery_date_day_int, delivery_date_month_int, delivery_date_year_int]])
    
    # Predict status
    y_pred = model_class.predict(user_data)
    
    return 1 if y_pred == 1 else 0

# Function to predict selling price
def predict_selling_price(country, status, item_type, application, width, product_ref, quantity_tons_log, customer_log, thickness_log, item_date_day, item_date_month, item_date_year, delivery_date_day, delivery_date_month, delivery_date_year):
    # Convert input values to integers
    item_date_day_int = int(item_date_day)
    item_date_month_int = int(item_date_month)
    item_date_year_int = int(item_date_year)
    delivery_date_day_int = int(delivery_date_day)
    delivery_date_month_int = int(delivery_date_month)
    delivery_date_year_int = int(delivery_date_year)
    
    # Load regression model
    with open(r"C:\Users\Happy\Desktop\Naren Baskar\New folder\Industrial_regression_model.pkl", "rb") as f:
        model_regg = pickle.load(f)
    
    # Prepare user data for prediction
    user_data = np.array([[country, status, item_type, application, width, product_ref, quantity_tons_log, customer_log, thickness_log,
                           item_date_day_int, item_date_month_int, item_date_year_int, delivery_date_day_int, delivery_date_month_int, delivery_date_year_int]])
    
    # Predict selling price
    y_pred = model_regg.predict(user_data)
    
    # Convert log price back to actual price
    actual_selling_price = np.exp(y_pred[0])
    
    return actual_selling_price

# Streamlit configuration
st.set_page_config(layout="wide")

# Title of the application
st.title(":blue[**INDUSTRIAL COPPER MODELING**]")

# Sidebar for navigation
with st.sidebar:
    option = option_menu('Naren', options=["PREDICT SELLING PRICE", "PREDICT STATUS"])

# Predict Status
if option == "PREDICT STATUS":
    st.header("PREDICT STATUS (Won / Lose)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        country = st.number_input("**Enter the Value for COUNTRY**", min_value=25.0, max_value=113.0, format="%0.2f")
        item_type = st.number_input("**Enter the Value for ITEM TYPE**", min_value=0.0, max_value=6.0, format="%0.2f")
        application = st.number_input("**Enter the Value for APPLICATION**", min_value=2.0, max_value=87.5, format="%0.2f")
        width = st.number_input("**Enter the Value for WIDTH**", min_value=700.0, max_value=1980.0, format="%0.2f")
        product_ref = st.number_input("**Enter the Value for PRODUCT_REF**", min_value=611728, max_value=1722207579, format="%0.0f")
        quantity_tons_log = st.number_input("**Enter the Value for QUANTITY_TONS (Log Value)**", min_value=-0.322, max_value=6.924, format="%0.15f")
        customer_log = st.number_input("**Enter the Value for CUSTOMER (Log Value)**", min_value=17.219, max_value=17.230, format="%0.15f")
        thickness_log = st.number_input("**Enter the Value for THICKNESS (Log Value)**", min_value=-1.715, max_value=3.282, format="%0.15f")
    
    with col2:
        selling_price_log = st.number_input("**Enter the Value for SELLING PRICE (Log Value)**", min_value=5.975, max_value=7.390, format="%0.15f")
        item_date_day = st.selectbox("**Select the Day for ITEM DATE**", list(range(1, 32)))
        item_date_month = st.selectbox("**Select the Month for ITEM DATE**", list(range(1, 13)))
        item_date_year = st.selectbox("**Select the Year for ITEM DATE**", ["2020", "2021"])
        delivery_date_day = st.selectbox("**Select the Day for DELIVERY DATE**", list(range(1, 32)))
        delivery_date_month = st.selectbox("**Select the Month for DELIVERY DATE**", list(range(1, 13)))
        delivery_date_year = st.selectbox("**Select the Year for DELIVERY DATE**", ["2020", "2021", "2022"])

    button = st.button(":violet[***PREDICT THE STATUS***]", use_container_width=True)

    if button:
        status = predict_status(country, item_type, application, width, product_ref, quantity_tons_log, customer_log, thickness_log, selling_price_log, item_date_day, item_date_month, item_date_year, delivery_date_day, delivery_date_month, delivery_date_year)
        
        if status == 1:
            st.write("## :green[**The Status is WON**]")
        else:
            st.write("## :red[**The Status is LOSE**]")

# Predict Selling Price
if option == "PREDICT SELLING PRICE":
    st.header("**PREDICT SELLING PRICE**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        country = st.number_input("**Enter the Value for COUNTRY**", min_value=25.0, max_value=113.0, format="%0.2f")
        status = st.number_input("**Enter the Value for STATUS**", min_value=0.0, max_value=8.0, format="%0.2f")
        item_type = st.number_input("**Enter the Value for ITEM TYPE**", min_value=0.0, max_value=6.0, format="%0.2f")
        application = st.number_input("**Enter the Value for APPLICATION**", min_value=2.0, max_value=87.5, format="%0.2f")
        width = st.number_input("**Enter the Value for WIDTH**", min_value=700.0, max_value=1980.0, format="%0.2f")
        product_ref = st.number_input("**Enter the Value for PRODUCT_REF**", min_value=611728, max_value=1722207579, format="%0.0f")
        quantity_tons_log = st.number_input("**Enter the Value for QUANTITY_TONS (Log Value)**", min_value=-0.322, max_value=6.924, format="%0.15f")
        customer_log = st.number_input("**Enter the Value for CUSTOMER (Log Value)**", min_value=17.219, max_value=17.230, format="%0.15f")
    
    with col2:
        thickness_log = st.number_input("**Enter the Value for THICKNESS (Log Value)**", min_value=-1.715, max_value=3.282, format="%0.15f")
        item_date_day = st.selectbox("**Select the Day for ITEM DATE**", list(range(1, 32)))
        item_date_month = st.selectbox("**Select the Month for ITEM DATE**", list(range(1, 13)))
        item_date_year = st.selectbox("**Select the Year for ITEM DATE**", ["2020", "2021"])
        delivery_date_day = st.selectbox("**Select the Day for DELIVERY DATE**", list(range(1, 32)))
        delivery_date_month = st.selectbox("**Select the Month for DELIVERY DATE**", list(range(1, 13)))
        delivery_date_year = st.selectbox("**Select the Year for DELIVERY DATE**", ["2020", "2021", "2022"])

    button = st.button(":violet[***PREDICT THE SELLING PRICE***]", use_container_width=True)

    if button:
        price = predict_selling_price(country, status, item_type, application, width, product_ref, quantity_tons_log, customer_log, thickness_log, item_date_day, item_date_month, item_date_year, delivery_date_day, delivery_date_month, delivery_date_year)
        
        st.write(f"## :green[**The Selling Price is :**] ${price:.2f}")
