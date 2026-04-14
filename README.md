# 🚀 Bitcoin Price Analysis & Forecasting

## 📊 Project Overview

This project focuses on analyzing Bitcoin price trends and predicting future prices using Time Series Forecasting techniques. It covers the complete data pipeline from data preprocessing to visualization and forecasting.

---

## 🎯 Objectives

* Analyze historical Bitcoin price data
* Understand trends, patterns, and volatility
* Build forecasting models to predict future prices
* Create an interactive dashboard for visualization

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
├── data/                  # Dataset
├── notebooks/             # Jupyter notebooks for analysis
├── src/
│   └── app.py             # Streamlit dashboard
├── requirements.txt
├── README.md
├── dashboard.png          # Screenshot of dashboard
```

---

## 🔍 Steps Performed

### 1. Data Cleaning

* Removed unnecessary rows
* Handled missing values
* Converted data into proper numeric format

### 2. Time Series Preparation

* Created a date column
* Converted data into time-based format

### 3. Exploratory Data Analysis (EDA)

* Visualized price trends
* Calculated moving averages (MA_3, MA_5)
* Analyzed volatility (risk)
* Generated correlation matrix

### 4. Forecasting Models

#### 🔹 ARIMA Model

* Used for basic time series forecasting
* Predicted short-term future prices

#### 🔹 Prophet Model

* Advanced forecasting model
* Captures trend and patterns automatically
* Provides more realistic predictions

---

## 📈 Dashboard

An interactive dashboard was created using Streamlit that displays:

* Bitcoin price trend
* Moving averages
* Forecast predictions

---

## 🖼️ Dashboard Preview

![Dashboard](dashboard.png)

---

## ▶️ How to Run the Project

1. Install required libraries:

```bash
pip install -r requirements.txt
```

2. Run the dashboard:

```bash
streamlit run src/app.py
```

---

## 📊 Results

* Successfully analyzed Bitcoin price trends
* Built forecasting models (ARIMA & Prophet)
* Developed an interactive dashboard for visualization

---

## 💡 Key Learnings

* Time Series Analysis fundamentals
* Forecasting using ARIMA and Prophet
* Data visualization techniques
* Building dashboards using Streamlit

---

## 🚀 Future Improvements

* Add LSTM model for deep learning prediction
* Use real-time cryptocurrency API
* Deploy dashboard online

---
