# Judul Project
Penerapan machine learning regresi untuk memprediksi harga mobil bekas dari inklan mobil di Belarus

## Repository Outline
- app.py - Main page deploy
- cars.csv - dataset projek
- eda.py - halaman eda deploy
- model_xbg_r.pkl - pipeline yang best
- model.py - halaman model buat prediksi deploy
- notebook_inference.ipynb - notebook data inference
- P1M2_dwi_adhi_conceptual.txt - jawaban 3 soal conceptual
- P1M2_dwi_adhi_ipynb - notebook utama projek
- requirements.txt - library buat deploy
- README.md - Penjelasan gambaran umum project
- url.txt- link dataset dan deploy

## Problem Background
Di Belarus, pasar mobil bekas memiliki banyak peminat, terutama karena daya beli masyarakat yang menurun. Akibatnya, semakin banyak orang yang memilih untuk membeli mobil bekas dibandingkan mobil baru.

Namun, menentukan harga mobil bekas bukanlah hal yang mudah, terutama bagi mereka yang tidak memiliki pengetahuan tentang otomotif, karena tidak ada standar harga yang jelas.

Oleh karena itu, saya sebagai Data Analyst akan membangun sebuah model prediksi harga mobil bekas untuk membantu masyarakat dalam menentukan harga yang wajar, baik saat ingin menjual maupun membeli mobil.

## Project Output
Output dari projek ini adalah dari 5 model yang digunakan, XgBoost Regressor paling baik untuk memprediksi harga mobil bekas dan sebuah aplikasi penerapan model di Hugging Face.

## Data
Dataset terdiri dari 38532 baris dan 30 kolom.

## Method
Dalam proyek ini, saya menggunakan lima metode regresi dari algoritma machine learning, yaitu:

- KNeighborsRegressor
- Support Vector Regression (SVR)
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor

Setelah melakukan evaluasi terhadap semua model, saya memilih model dengan performa terbaik berdasarkan metrik evaluasi R² dan RMSE

## Stacks
- Python
- pandas, numpy, scipy, plotly-express, pickle, matplotlib, seaborn, sklearn feature-engine, xgboost.

## Reference
https://www.kaggle.com/datasets/lepchenkov/usedcarscatalog/data
---