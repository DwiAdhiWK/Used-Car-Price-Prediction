import streamlit as st
import pandas as pd
import pickle


def run():
# Load All Files

    with open('model_xbg_r.pkl', 'rb') as file:
        full_process = pickle.load(file)
    # distance = st.number_input(label='input your distance here',min_value=0.0,max_value=7.5)
    
    manufacturer_name = st.text_input(label='input nama manufaktur mobil')
    model_name = st.text_input(label = 'input nama model mobil')
    transmission = st.selectbox(label = 'input jenis transmisi',options= ['mechanical','automatic'])
    color = st.selectbox(label = 'input warna mobil',options= ['silver', 'blue', 'red', 'black', 'grey', 'other', 'brown',
       'white', 'green', 'violet', 'orange', 'yellow'])
    engine_capacity = st.number_input(label='input kapasitas mesin',min_value=0.0,max_value=4.5)
    engine_fuel = st.selectbox(label = 'input bahan bakar mesin',options= ['gasoline', 'gas', 'diesel', 'hybrid-petrol', 'hybrid-diesel',
       'electric'])
    engine_type = st.selectbox(label = 'input jenis mesin',options= ['gasoline', 'diesel', 'electric'])
    body_type = st.selectbox(label = 'input jenis badan mobil',options= ['universal', 'suv', 'sedan', 'hatchback', 'liftback', 'minivan',
       'minibus', 'van', 'pickup', 'coupe', 'cabriolet', 'limousine'])
    drivetrain = st.selectbox(label = 'input jenis drivetrain',options= ['all', 'front', 'rear'])
    odometer_value = st.number_input(label='input odometer',min_value=0.0)
    year_produced = st.number_input(label='input tahun produksi',min_value=0.0)
    number_of_photos = st.number_input(label='input berapa banyak foto',min_value=0.0)
    up_counter = st.number_input(label='input up counter',min_value=0.0)
    duration_listed = st.number_input(label='input durasi listed',min_value=0.0)
    has_warranty = st.radio(label="Apakah mobil punya garansi?", options=["True", "False"])
    is_exchangeable = st.radio(label="Apakah mobil dapat di tukar tambah?", options=["True", "False"])
    state = st.selectbox(label = 'input status mobil',options= ['owned', 'emergency', 'new'])
    manufacturer_region = st.text_input(label='input region mobil')
    engine_has_gas = st.radio(label="Apakah mobil ada bensin?", options=["True", "False"])
    car_age = 2025 - year_produced

    # surge_multiplier = st.selectbox(label='choose your surge_multiplier here',optionss=[1.  , 1.25, 2.5 , 2.  , 1.75, 1.5 , 3.  ])
    # name = st.selectbox(label='choose your cab name here',optionss=['Shared', 'Lux', 'Lyft', 'Lux Black XL', 'Lyft XL', 'Lux Black',
    #    'UberXL', 'Black', 'UberX', 'WAV', 'Black SUV', 'UberPool'])
    # product_id = st.selectbox(label='choose your product id here',optionss=['lyft_line', 'lyft_premier', 'lyft', 'lyft_luxsuv', 'lyft_plus',
    #    'lyft_lux', 'uber_line', 'uber_premier', 'uber', 'uber_luxsuv',
    #    'uber_plus', 'uber_lux'])
    
    st.write('In the following is the result of the data you have input : ')
    
    data_inf = pd.DataFrame({
        'manufacturer_name': manufacturer_name,
        'model_name': model_name,
        'transmission': transmission,
        'color': color,
        'engine_fuel': engine_fuel,
        'engine_type': engine_type,
        'engine_capacity': engine_capacity,
        'body_type': body_type,
        'drivetrain': drivetrain,
        'odometer_value': odometer_value,
        'year_produced': year_produced,
        'number_of_photos': number_of_photos,
        'up_counter': up_counter,
        'duration_listed': duration_listed,
        'has_warranty': has_warranty==True,
        'is_exchangeable': is_exchangeable==True,
        'state': state,
        'manufacturer_region': manufacturer_region,
        'engine_has_gas': engine_has_gas==True,
        'car_age': car_age
    }, index=[0])
  
    data_display = data_inf.copy()
    data_display.columns = [col.replace('_', ' ').title() for col in data_display.columns]

    st.dataframe(data_display, use_container_width=True)

    # Predict when button is clicked
    if st.button(label='Predict'):
        y_pred_inf = full_process.predict(data_inf)
        st.metric(label="Berikut adalah prediksi harga mobil:", value=f"${y_pred_inf[0]:,.2f}")

    # If your data is a classification, you can follow the example below 
        # if y_pred_inf[0] == 0:
        #     st.write('Pasien tidak terkena jantung')
        #     st.markdown("[Cara Cegah Serangan Jantung](https://www.siloamhospitals.com/informasi-siloam/artikel/cara-cegah-serangan-jantung-di-usia-muda)")

        # else:
        #     st.write('Pasien kemungkinan terkena jantung')
        #     st.markdown("[Cara Hidup Sehat Sehabis Terkena Serangan Jantung](https://lifestyle.kompas.com/read/2021/11/09/101744620/7-pola-hidup-sehat-setelah-mengalami-serangan-jantung?page=all)")
