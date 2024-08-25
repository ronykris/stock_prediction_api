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

train_model('META')

def predict(days):
    future = model.make_future_dataframe(periods=days)
    forecast = model.predict(future)
    current_date = pd.Timestamp(datetime.now().date())
    future_forecast = forecast[forecast['ds'] > current_date]
    results_df = future_forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].reset_index(drop=True)
    results_df['ds'] = pd.to_datetime(results_df['ds'])
    return results_df