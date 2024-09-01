from datetime import datetime, timedelta
import yfinance as yf
from prophet import Prophet
import pandas as pd

model = Prophet(daily_seasonality = True)

def train_model(ticker):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=1825)
    df = yf.download(ticker, start=start_date, end=end_date)
    print(df)
    df_prophet = df.reset_index()[["Date", "Close"]]
    df_prophet.columns = ["ds", "y"]
    print(df_prophet)
    model.fit(df_prophet)

def predict(days):
    print(f"Predicting for {days} days")
    future = model.make_future_dataframe(periods=days + 4)  # Add extra days to account for weekends
    print(f"Future dataframe shape: {future.shape}")
    forecast = model.predict(future)
    print(f"Forecast shape: {forecast.shape}")
    current_date = pd.Timestamp(datetime.now().date())
    future_forecast = forecast[forecast['ds'] > current_date]
    print(f"Future forecast shape: {future_forecast.shape}")
    results_df = future_forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].head(days).reset_index(drop=True)
    print(f"Results dataframe shape: {results_df.shape}")
    results_df['ds'] = results_df['ds'].dt.strftime('%Y-%m-%d')
    return results_df

train_model('META')