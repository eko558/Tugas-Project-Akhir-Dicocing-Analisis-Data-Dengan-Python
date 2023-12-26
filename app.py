import numpy as py
import pandas as pd
import streamlit as st
import matplotlib as plt

st.title('Dashboard Sederhana')
st.header('Project Akhir Analisis Data Dengan Python')
st.text('Oleh : M. Eko Cahyono (Selasa, 26 Desember 2023)')

st.text('''Analisis ini dilakukan pada dataset layanan bikecycle sharing
(sewa sepeda). Adapun dataset yang dimaksud adalah sebagai berikut''')

bikeCycleHour_df = pd.read_csv("https://raw.githubusercontent.com/eko558/Bikecycle_df/main/hour.csv")
bikeCycleHour_df['season'] = bikeCycleHour_df['season'].astype(object)
bikeCycleHour_df['datetime'] = pd.to_datetime(bikeCycleHour_df['datetime'])
bikeCycleHour_df['month'] = bikeCycleHour_df['datetime'].dt.strftime('%B')
bikeCycleHour_df['year'] = bikeCycleHour_df['datetime'].dt.year
bikeCycleHour_df['month_num'] = bikeCycleHour_df['datetime'].dt.month
bikeCycleHour_df['day number'] = bikeCycleHour_df['datetime'].dt.dayofweek
bikeCycleHour_df['day of week'] = bikeCycleHour_df['datetime'].dt.strftime('%A')
bikeCycleHour_df['total riders'] = bikeCycleHour_df['casual'] + bikeCycleHour_df['registered']

#Kami definisikan musim terlebih dahulu
pembagianMusim = {1: "Winter",
                  2: "Spring",
                  3: "Summer",
                  4: "Fall"}
bikeCycleHour_df['season'] = bikeCycleHour_df['season'].map(pembagianMusim)
bikeCycleHour_df = bikeCycleHour_df[bikeCycleHour_df['registered'] >0]
bikeCycleHour_df['total riders'] = bikeCycleHour_df['casual'] + bikeCycleHour_df['registered']
bikeCycleHour_df['hour'] = bikeCycleHour_df['datetime'].dt.hour
bikeCycleHour_df = bikeCycleHour_df[bikeCycleHour_df['year']==2011]
bikeCycleHour_df['mean_month'] = bikeCycleHour_df['month'].map(bikeCycleHour_df.groupby('month')['total riders'].median())
monthDict = []
for i in enumerate(bikeCycleHour_df['month'].unique(),1):
  monthDict.append(i)
monthDict = dict(monthDict)

st.write(bikeCycleHour_df)

st.title('')

st.header('Pertanyaan 1')
st.text('''Apakah perubahan musim mempengaruhi jumlah pengguna layanan sewa sepeda ?''')

st.header('')
st.image("https://raw.githubusercontent.com/eko558/Picture-for-dicoding-analysis/main/Pengguna%20dan%20Perubahan%20Suhu.png")
st.header('')
st.text('''Berdasarkan grafik diatas, dapat diketahui bahwa hadirnya musim dingin mempengaruhi 
turunya suhu, sehingga dengan menurunya suhu terjadi penurunan pula pada 
jumlah pengguna layanan sewa sepeda''')

st.title('')
st.header('Pertanyaan 2')
st.text('Kapankah pengguna non subscription (casual rider) paling banyak menggunakan layanan ?')

st.header('')
st.image("https://raw.githubusercontent.com/eko558/Picture-for-dicoding-analysis/main/Pengguna%20Biasa.png")
st.header('')

st.text('''Berdasarkan grafik diatas dapat diketahui bahwa hari sabtu diantara pukul 14.00 
hingga 15.00 merupakan pilihan terbaik pengguna non subscription (casual ridings
untuk mengakses layanan sewa sepeda)''')