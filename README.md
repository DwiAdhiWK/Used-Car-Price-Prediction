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

## SMART and Problem Statement
Specific: Meningkatkan tingkat retensi pengguna jasa pengiriman makanan dengan cara meningkatkan faktor-faktor yang mempengaruhi kemauan user menggunakan jasa tersebut.

Measurable: Berhasil meningkatkan tingkat retensi user sebesar 70%

Achievable: Mengetahui faktor-faktor yang mempengaruhi user menggunakan jasa pengiriman makanan.

Relevant: Peningkatan tingkat retensi dapat diartikan pengguna lebih bersedia menggunakan jasa yang pada gilirannya meningkatkan pendapatan perusahaan.

Time-bound: Proses analisis dan visualisasi data dilakukan selama 2 minggu hari kerja.

Problem statement: Perusahaan mengalami penurunan pengunaan jasa pengiriman makan. Tim marketing mengestimasikan tingak retensi user sebesar 60%. Selain itu perusahaan kekurangan refensi agar user tetap menggunakan jasa. Saya sebagai data analyst yang berkerja diperusahaan pengiriman makanan di Bangalore ditugasakan meningkatkan retensi user.

## Project Output
Output dari projek ini adalah dari model dengan performa terbaik dari 5 model regresi akan digunakan untuk memprediksi harga mobil bekas dan sebuah aplikasi penerapan model di Hugging Face.

## Data
Dataset terdiri dari 38532 baris dan 30 kolom.

## Method
Dalam proyek ini, saya menggunakan lima metode regresi dari algoritma machine learning, yaitu:

- KNeighborsRegressor
- Support Vector Regression (SVR)
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor

Model dengan performa terbaik akan di pilih sebagai model prediksi.

## Model Evaluation

| Model                   | R² (Train) | R² (Test) |   Mean RMSE  | Std. Dev (σ) |
| :---------------------- | :--------: | :-------: | :----------: | :----------: |
| KNeighborsRegressor     |    0.893   |   0.832   |   2,617.02   |     95.00    |
| SVR                     |    0.256   |   0.266   |   5,723.16   |    142.67    |
| Decision Tree Regressor |    0.999   |   0.802   |   2,804.45   |     82.34    |
| Random Forest Regressor |    0.984   |   0.884   |   2,118.06   |     70.74    |
| **XGBoost Regressor**   |  **0.943** | **0.891** | **2,066.51** |   **83.73**  |

Model XgBoost Regressor menunjukan performa paling seimbang antara nilai R² train dan test serta nilai RMSE terendah, menandakan generalisasi yang baik. Model akan dilakukan tuning untuk meningkatkan performa.

## Hyperparameter Tuning

Hyperparameter Tuning yang digunakan adalah RandomizedSearchCV dan berikut adalah perbandingan model XGBoost sebelum dan setelah tuning:

| Model Version     | R² (Train) | R² (Test) | RMSE (Train) |  RMSE (Test) |
| :---------------- | :--------: | :-------: | :----------: | :----------: |
| **Before Tuning** |    0.932   |   0.893   |   1,534.43   |   2,091.23   |
| **After Tuning**  |  **0.915** | **0.890** | **1,868.13** | **2,108.94** |

Setelah dilakukan hyperparameter tuning, performa model sedikit menurun pada data train dan test — R² menurun dan RMSE meningkat.
Hal ini menunjukkan bahwa tuning berhasil mengurangi overfitting pada data training (karena R² train menurun), meskipun berdampak kecil pada akurasi test.
Model hasil tuning memiliki generalization yang lebih baik dan stabil, sehingga tetap dipilih untuk implementasi.

## Conclusion
Dalam proyek ini, lima model regresi digunakan untuk memprediksi harga mobil bekas, yaitu KNeighborsRegressor, Support Vector Regression (SVR), Decision Tree Regressor, Random Forest Regressor, dan XGBoost Regressor.

Setelah dilakukan evaluasi, model dengan performa terbaik adalah XGBoost Regressor, dengan nilai R² train sebesar 0.91 dan R² test sebesar 0.89.
Meskipun nilai R² tersebut melampaui standar yang ditetapkan pada problem statement, tingkat error (RMSE) prediksi masih sedikit lebih tinggi dari target — berada di kisaran 1,800–2,100 dolar, sedangkan target error di problem statement adalah 1,500 dolar.

Perbedaan ini kemungkinan disebabkan oleh:
- Kehadiran outlier dalam data
- Keterbatasan fitur yang digunakan pada model

Untuk peningkatan ke depan, model dapat dikembangkan dengan menambahkan lebih banyak fitur yang relevan, seperti merek ban, jenis velg (rim), atau tipe interior, agar XGBoost dapat mempelajari variasi harga dengan lebih baik.

## Stacks
- Python
- pandas, numpy, scipy, plotly-express, pickle, matplotlib, seaborn, sklearn feature-engine, xgboost.

## Reference
https://www.kaggle.com/datasets/lepchenkov/usedcarscatalog/data
---
