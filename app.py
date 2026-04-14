import streamlit as st
import pandas as pd

st.title(" Bitcoin Price Analysis Dashboard")
df = pd.read_csv('../data/bitcoin_ohlcv.csv', skiprows = 2)
# Rename columns manually
df.columns = ['Date', 'Price', 'Close', 'High', 'Low', 'Volume']

st.write("Dataset Preview")
st.dataframe(df.head())





# Price Trend Graph
import matplotlib.pyplot as plt 

st.subheader("Bitcoin Price Trend")

fig, ax = plt.subplots()

ax.plot(df['Date'], df['Close'])
ax.set_xlabel('Date')
ax.set_ylabel('Close Price')
ax.set_title('Bitcoin Closing Price')

st.pyplot(fig) 






# Moving Average 
# Create moving averages FIRST
df['MA_3'] = df['Close'].rolling(window=3).mean()
df['MA_5'] = df['Close'].rolling(window=5).mean()

st.subheader("Moving Average")

fig, ax = plt.subplots()

ax.plot(df['Date'], df['Close'], label='Close')
ax.plot(df['Date'], df['MA_3'], label='MA 3')
ax.plot(df['Date'], df['MA_5'], label='MA 5')

ax.legend()
ax.set_title("Moving Average Trend")

st.pyplot(fig)





# Prophet 
st. subheader("Bitcoin Price Forecast (Prophet)")

# Section Ttile
from prophet import Prophet 

# Prepare the data 
df_prophet = df[['Date','Close']]
df_prophet.columns =['ds','y']

# Train the Model
model = Prophet()
model.fit(df_prophet)

# Create future data 
future = model.make_future_dataframe(periods=30)

# Predict
forecast = model.predict(future)

fig1= model.plot(forecast)
st.pyplot(fig1) 

