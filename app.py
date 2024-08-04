'''import pandas as pd
import pickle as pk
import streamlit as st

# Load the model
model = pk.load(open('model.pkl', 'rb'))

# Set up the Streamlit app
st.header('Car Price Prediction ML Model')

# Load and preprocess data
data = pd.read_csv('Cardetails.csv')

def get_brand_name(car_name):
    return car_name.split(' ')[0].strip()

data['name'] = data['name'].apply(get_brand_name)

# Load mappings
brand_mapping = {brand: idx + 1 for idx, brand in enumerate(data['name'].unique())}
fuel_mapping = {fuel: idx + 1 for idx, fuel in enumerate(data['fuel'].unique())}
seller_type_mapping = {seller: idx + 1 for idx, seller in enumerate(data['seller_type'].unique())}
transmission_mapping = {transmission: idx + 1 for idx, transmission in enumerate(data['transmission'].unique())}
owner_mapping = {owner: idx + 1 for idx, owner in enumerate(data['owner'].unique())}

# Create user input widgets
name = st.selectbox('Select Car Brand', data['name'].unique())
year = st.slider('Car Manufactured Year', 1994, 2024)
km_driven = st.slider('No of kms Driven', 11, 200000)
fuel = st.selectbox('Fuel type', data['fuel'].unique())
seller_type = st.selectbox('Seller Type', data['seller_type'].unique())
transmission = st.selectbox('Transmission Type', data['transmission'].unique())
owner = st.selectbox('Owner Type', data['owner'].unique())
mileage = st.slider('Car Mileage', 10, 40)
engine = st.slider('Engine CC', 700, 5000)
max_power = st.slider('Max Power', 0, 200)
seats = st.slider('No of Seats', 5, 10)



# Prediction
if st.button("Predict"):

    # Prepare input data
    input_data = {
        'name': brand_mapping[name],
        'year': year,
        'km_driven': km_driven,
        'fuel': fuel_mapping[fuel],
        'seller_type': seller_type_mapping[seller_type],
        'transmission': transmission_mapping[transmission],
        'owner': owner_mapping[owner],
        'mileage': mileage,
        'engine': engine,
        'max_power': max_power,
        'seats': seats
    }
   
    input_df = pd.DataFrame([input_data])

    # Display input data for debugging
    st.write("Input Data for Prediction:")
    st.write(input_df)

    # Make prediction
    car_price = model.predict(input_df)

    # Display result
    st.markdown(f'Car Price is going to be ₹{car_price[0]:,.2f}')

    '''

import pandas as pd
import pickle
import streamlit as st

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

# Set up the Streamlit app
st.set_page_config(page_title='Car Price Prediction', layout='wide')

# App header and description
st.title('🚗 Car Price Prediction ML Model')
st.markdown("""
This application predicts the price of a car based on various features.
Please provide the details of the car, and the model will estimate the price.
""")

# Load and preprocess data
data = pd.read_csv('Cardetails.csv')

def get_brand_name(car_name):
    return car_name.split(' ')[0].strip()

data['name'] = data['name'].apply(get_brand_name)

# Load mappings
brand_mapping = {brand: idx + 1 for idx, brand in enumerate(data['name'].unique())}
fuel_mapping = {fuel: idx + 1 for idx, fuel in enumerate(data['fuel'].unique())}
seller_type_mapping = {seller: idx + 1 for idx, seller in enumerate(data['seller_type'].unique())}
transmission_mapping = {transmission: idx + 1 for idx, transmission in enumerate(data['transmission'].unique())}
owner_mapping = {owner: idx + 1 for idx, owner in enumerate(data['owner'].unique())}

# Layout for input widgets
with st.sidebar:
    st.header('Enter Car Details')
    name = st.selectbox('Select Car Brand', data['name'].unique())
    year = st.slider('Car Manufactured Year', 1994, 2024)
    km_driven = st.slider('No of kms Driven', 11, 200000)
    fuel = st.selectbox('Fuel Type', data['fuel'].unique())
    seller_type = st.selectbox('Seller Type', data['seller_type'].unique())
    transmission = st.selectbox('Transmission Type', data['transmission'].unique())
    owner = st.selectbox('Owner Type', data['owner'].unique())
    mileage = st.slider('Car Mileage (km/l)', 10, 40)
    engine = st.slider('Engine CC', 700, 5000)
    max_power = st.slider('Max Power (bhp)', 0, 200)
    seats = st.slider('No of Seats', 5, 10)

# Prediction section
st.header('📊 Prediction Result')
if st.button("Predict"):
    # Prepare input data
    input_data = {
        'name': brand_mapping[name],
        'year': year,
        'km_driven': km_driven,
        'fuel': fuel_mapping[fuel],
        'seller_type': seller_type_mapping[seller_type],
        'transmission': transmission_mapping[transmission],
        'owner': owner_mapping[owner],
        'mileage': mileage,
        'engine': engine,
        'max_power': max_power,
        'seats': seats
    }
   
    input_df = pd.DataFrame([input_data])

    # Display input data for debugging
    st.write("### Input Data for Prediction:")
    st.dataframe(input_df)

    # Make prediction
    car_price = model.predict(input_df)

    # Display result
    st.write("### Predicted Car Price:")
    st.markdown(f'**Estimated Price:** ₹{car_price[0]:,.2f}')

