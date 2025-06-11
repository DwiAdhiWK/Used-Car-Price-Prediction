import streamlit as st
import deployment.eda as eda
import deployment.model as model


page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploration Data Analysis', 'Model Prediksi'])

if page == 'Home Page':
    st.header('Welcome Page') 
    st.write('')
    st.write('Milestone 2')
    st.write('Nama      : Dwi Adhi Widigda Kartomihardjo')
    st.write('Batch     : FTDS-027')
    st.write('Tujuan Milestone    : Melakukan analisis terhadap harga mobil bekas untuk membuat model yang dapat memprediksi harga mobil bekas')
    st.write('')
    st.caption('Silahkan pilih menu lain di Select Box pada sebelah kiri layar anda untuk memulai!')
    st.write('')
    st.write('')
    with st.expander("Latar Belakang"):
        st.caption('Di Belarus, pasar mobil bekas cukup banyak peminatnya selain itu juga karena daya beli masyarakat menurun orang lebih memili membeli mobil bekas. Untuk menentukan harga mobil bekas untuk orang yang tidak mengerti mobil sulit karena tidak ada patokan nya. Saya sebagai data analyst akan membuat model untuk memprediksi harga mobil bekas untuk mempermudah orang-orang yang ingin menjual atau membeli mobil')

    with st.expander("Problem Statement"):
            st.caption('Saya sebagai data analyst akan membuat model regresi untuk memprediksi harga jual mobil bekas. Sasaran nya adalah untuk mencapai nilai RMSE lebih kecil dari 1500 dollar dan nilai R2 sebesar 0.85 saat test data nya. Saya akan menggunakan 39000 baris data mobil bekas dari kaggle dan waktu analisis ini dikerjakan selama 2 minggu.')

    with st.expander("Kesimpulan"):
        st.caption('Kesimpulan yang dapat dibentuk dari projek ini adalah: ')
        st.caption('Dalam pengerjaan projek 5 model digunakan sebagai konsiderasi model regresi yang digunakan untuk memprediksi harga mobil bekas. Model-model itu adalah KNeighborsRegressor, Support Vector Regression, Decision Tree, Random Forest Regression, dan XgBoost Regressor. Setelah setiap model di evaluasi model yang dipilih untuk memprediksi harga mobil bekas adalah Xgboost Regressor. Model ini menghasil kan nilai R2 train sebesar 0.91 dan test sebesar 0.89. Nilai R2 dari model ini lebih besar daripada standar R2 di problem statement tetapi prediksi yang dibuat model ini masih kurang dari standar di problem statement. Error prediksi harga mobil bekas menghasilkan nilai di antara 1800-2100 dolar tetapi standar di promblem statemen sebanyak 1500 dolar. Perbedaan ini bisa terjadi karena beberapa seperti outlier yang ada di data atau fitur yang digunakan masih kurang.')
elif page == 'Exploration Data Analysis':
    eda.run()
else:
     model .run()