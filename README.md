# 🚀 Bitcoin Price Analysis & Forecasting

## 📊 Project Overview

This project focuses on analyzing Bitcoin price trends and predicting future prices using Time Series Forecasting techniques. It covers the complete pipeline from data cleaning to visualization and forecasting using ARIMA and Prophet models.

---

## 🎯 Objectives

* Analyze historical Bitcoin price data
* Understand trends and volatility
* Build forecasting models
* Create an interactive dashboard

---

## 🛠️ Technologies Used

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Statsmodels (ARIMA)
* Prophet
* Streamlit

---

## 📂 Project Structure

```
crypto-time-series-project/
│
├── data/
├── notebooks/
├── src/
│   └── app.py
├── assets/
│   ├── dashboard.png
│   ├── price_trend.png
│   ├── moving_avg.png
│   ├── volatility.png
│   ├── forecast.png
├── requirements.txt
├── README.md
```

---

## 🔍 Steps Performed

### 1. Data Cleaning

* Removed unnecessary rows
* Handled missing values
* Converted data types

### 2. Exploratory Data Analysis (EDA)

* Visualized price trends
* Calculated moving averages (MA_3, MA_5)
* Analyzed volatility
* Performed correlation analysis

### 3. Forecasting Models

#### 🔹 ARIMA

* Used for basic time series forecasting

#### 🔹 Prophet

* Used for advanced forecasting with trend detection

---

## 📈 Dashboard Features

* Price Trend Visualization
* Moving Average Analysis
* Volatility Analysis
* Forecast Predictions

---

## 🖼️ Project Screenshots

### 📊 Dashboard

<img width="1543" height="866" alt="Dashboard" src="https://github.com/user-attachments/assets/c1b274e9-ca7a-4cbc-82a1-c3ea37371487" />

--- 
### 📈 Price Trend

<img width="958" height="707" alt="Bitcoinprice" src="https://github.com/user-attachments/assets/442a38c4-3f0c-4d72-b48b-ad0fe945ef44" />

---

### 📊 Moving Average


<img width="914" height="674" alt="MovingAverage " src="https://github.com/user-attachments/assets/91fefac2-31e2-456c-81e3-bcbe32a509c0" />

---

### HeatMap 

<img width="1916" height="1020" alt="HeatMap" src="https://github.com/user-attachments/assets/c47f8c40-bce2-403c-86fd-c7c2ef095eb6" />

---

### 🔮 Forecast (Prophet)

<img width="1919" height="1021" alt="BitCoin Forecast Prophet" src="https://github.com/user-attachments/assets/15bf4b5e-3b7f-4c01-8ba1-541af755ca48" />

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run src/app.py
```

---

## 📊 Results

* Successfully analyzed Bitcoin trends
* Built ARIMA & Prophet models
* Created interactive dashboard

---

## 💡 Key Learnings

* Time Series Analysis
* Forecasting techniques
* Data visualization
* Streamlit dashboard development

---

## 🚀 Future Improvements

* Add LSTM model
* Use real-time API data
* Deploy dashboard online
