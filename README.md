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

![Dashboard](assets/dashboard.png)

---

### 📈 Price Trend

![Bitcoinprice](assets/bitcoinprice.png)

---

### 📊 Moving Average

![MovingAverage](assets/movingaverage.png)

---

### 📉 Volatility

![HeatMap](assets/heatmap.png)

---

### 🔮 Forecast (Prophet)

![BitCoinForecastProphet](assets/bitcoinforecastprophet.png)

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
