
# LANGKAH MENJALANKAN DASHBOARD SEDERHANA DARI PROJECT AKHIR ANALISIS DATA DENGAN PYTHON
### Disusun oleh M. Eko Cahyono (Selasa, 26 Desember 2023)

##

#### INFORMASI AWAL
Dikarenakan processor serta RAM laptop penyusun yang rendah, maka penyusunan dashboard sederhana dilakukan dengan menggunakan Google Colabs. Adapun penjelasan agar dapat menjalankan streamlit dengan Google Colabs adalah sebagai berikut

##

### A. Setting Evirontment
```sh
! pip install streamlit -q
import numpy as py
import pandas as pd
import streamlit as st
import matplotlib as plt
```

##
### B. Run Streamlit App
```sh
! streamlit run app.py & npx localtunnel --port 8501
```

##
### C. Detail Run Streamlit to Google Colab

##### 1. Create New Notebook to Google Colab
#####
![alt text](https://raw.githubusercontent.com/eko558/Cara-Akses-Dashboard/main/Buat%20Notepad%20Baru.png)
#####
#####
##### 2. Upload File (App)
#####
![alt text](https://raw.githubusercontent.com/eko558/Cara-Akses-Dashboard/main/upload%20file%20py.png)
#####
##### 3. Input Code Berikut
####
##### a. Install Streamlit
####

```sh
! pip install streamlit -q
```

#####
##### b. Ip Detector Widget
####
```sh
!wget -q -O - ipv4.icanhazip.com
```
#####
##### c. Streamlite Run Code
####
```sh
! streamlit run app.py & npx localtunnel --port 8501
```

#### Perhatikan Gambar Berikut
####
##### (Sebelum di run)
![alt text](https://raw.githubusercontent.com/eko558/Cara-Akses-Dashboard/main/input%20code%20berikut.png)
####
##### (Sesudah di run satu per satu)
![alt text](https://raw.githubusercontent.com/eko558/Cara-Akses-Dashboard/main/Run%20satu-satu%202.png)

### 
#### 4. Copy IP Adress
![alt text](https://raw.githubusercontent.com/eko558/Cara-Akses-Dashboard/main/copy%20IP.png)
### 
#### 5. Klik Link yang ditampilkan
![alt text](https://raw.githubusercontent.com/eko558/Cara-Akses-Dashboard/main/Click%20Link.png)
### 
#### 6. Paste IP Adress Pada Box dan Tombol 'Click to Submit' 
![alt text](https://raw.githubusercontent.com/eko558/Cara-Akses-Dashboard/main/paste%20ip%20disini.png)

# 
Sekian langkah menjalankan dashboard sederhana melalui google colab. saya ucapkan terimakasih



