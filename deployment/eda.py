import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly_express as px

#membuat function untuk nantinya dipanggil di app.py
def run():
    st.title('Welcome to Explaration Data Analysis')
# #Memanggil data csv 
    df= pd.read_csv(r'cars.csv')
    df['car_age'] = 2025 - df['year_produced']

# #menampilakn 5 data teratas
#     st.table(df.head(5))


#menampilakn phik matrix
    # st.title('Distribusi Harga Mobil')
    # image = Image.open('charts1.jpg')
    # st.image(image, caption='figure 1')
    fig = plt.figure()
    sns.histplot(df['price_usd'], bins=50, kde=True)
    plt.title("Distribusi Harga Mobil")
    st.pyplot(fig)

#menampilkan penjelasan 
    with st.expander('Penjelasan'):
        st.caption('Cell berikut menggambarkan distribusi harga mobil bekas dalam histogram. Persebaran harga skew ke kiri dimana banyak mobil dijual dengan harga sekitar 5000 dolar. Semakin harga nya naik semakin sedikit mobil yang dijual. Bisa dibilang lebih banyak mobil umum yang dijual dibadingkan dengan mobil antik.')
    
    fig = plt.figure()
    df['manufacturer_name'].value_counts().head(10).plot(kind='bar')
    plt.title('Top 10 Brand Mobil')
    plt.xlabel('Brand')
    plt.ylabel('Count')
    st.pyplot(fig)

    with st.expander('Penjelasan'):
        st.caption('Cell ini menampilkan 10 brand mobil yang popular dijual. Volkswagen adalah brand yang paling sering dijual dengan sebanyak 4000 model dan Nissan di urutan ke 10 dengan sekitar 1500 model yang dijual. Sebanyak 8 mobil Eropa, 1 mobil Amerika, dan 1 mobil Jepang. Bisa dibilang mobil Eropa lebih banyak peminat nya dibandingkan mobil Amerika dan Jepang.')
    
    fig = plt.figure()
    sns.scatterplot(x='odometer_value', y='price_usd', data=df)
    plt.title("Odometer vs Harga")
    plt.xlabel('Odemeter')
    plt.ylabel('Harga')
    st.pyplot(fig)

    with st.expander('Penjelasan'):
        st.caption('Cell ini menampilkan hubungan antara kolom odometer_value dengan price_usd menggunakan scatterplot. Terlihat ada korelasi negatif dimana semakin tinggi odometer_value semakin rendah harga mobil yang dijual. Bisa dibilang semakin sering dan lama mobil digunakan bedasarkan jarak tempuh nya semakin murah harga mobil nya.')
    
    fig = plt.figure()
    sns.scatterplot(x='car_age', y='price_usd', data=df)
    plt.title("Umur Mobil vs Harga")
    plt.xlabel('Umur Mobil')
    plt.ylabel('Harga')
    st.pyplot(fig)

    with st.expander('Penjelasan'):
        st.caption('Cell ini menampilkan hubungan antara kolom car_age dengan price_usd menggunakan scatterplot. Bedasarkan scatterplot, banyak mobil dijual berurumur 10 sampai 30 tahun. Terlihat ada korelasi negatif dimana semakin tinggi car_age semakin rendah harga mobil yang dijual. Bisa dibilang semakin tua mobil, semakin murah harga mobil nya. Tetapi bedasarkan scarplot ada data point dimana umur mobil lebih dari 30 tahun tetapi harga jual nya lebih banyak. Bisa dibilang data point ini adalah mobil antik dimana umur tidak terlalu mempengaruhi harga jual.')
    
    # fig = plt.figure()
    body_type_vis = df.groupby('body_type')[['price_usd']].mean().reset_index()
    fig = px.pie(body_type_vis,values='price_usd',names='body_type',title='Proporsi Jenis Bentuk Mobil')
    st.plotly_chart(fig)

    with st.expander('Penjelasan'):
        st.caption('Cell ini menampilkan proporsi jenis mobil yang dijual. Terdapat 12 jenis mobil dan yang paling banyak adalah tipe suv sebanyak 14.3%, kedua adalah pickup 12.2%, dan ketiga adalah cabriolet atau roadster sebanyak 11.4%.')
    
    body_type_vis = df.groupby('drivetrain')[['price_usd']].mean().reset_index()
    fig = px.pie(body_type_vis,values='price_usd',names='drivetrain',title='Proporsi Jenis Drive Train Mobil')
    st.plotly_chart(fig)

    with st.expander('Penjelasan'):
        st.caption('Cell ini menampilkan proporsi jenis drive train yang dijual. Terdapat 3 jenis drive train yaitu all wheel drive, rear wheel drive dan front wheel drive. All wheel drive adalaha jenis drive train terbanyak dengan proporsi 54.2%. Front wheel dan Rear wheel memiliki proporsi yang hampir mirip. Bisa dibilang mobil dengan sistem all wheel drive lebih banyak peminat nya. Hal ini mungkin terkadi karena data di ambil di Belarus yang memiliki 4 musim. Mobil all wheel drive cenderung kokoh untuk banyak kondisi cuaca.')
    
    model_counts = df.groupby(['manufacturer_name', 'model_name']).size().reset_index(name='count')

    top_models = model_counts.sort_values(by='count', ascending=False).head(50)

    fig = px.treemap(
        top_models,
        path=['manufacturer_name', 'model_name'],  
        values='count',
        color='count',
        color_continuous_scale='viridis',
        title='Tree Map Tipe Model Untuk Setiap Brand'
    )
    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
    st.plotly_chart(fig)

    with st.expander('Penjelasan'):
        st.caption('Cell ini menampilkan Tree Map untuk brand mobil dengan model yang sering dijual. Bedasarkan tree map ini, mobil yang banyak dijual adalah mobil sedan seperti model Passat, Astra, dan Mondeo. ')
    
    
    

    

    





