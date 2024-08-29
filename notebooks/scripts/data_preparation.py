import pandas as pd
import talib

def load_stock_data(file_path):
    return pd.read_csv(file_path)

def calculate_technical_indicators(df):
    df['SMA'] = talib.SMA(df['Close'], timeperiod=20)
    df['RSI'] = talib.RSI(df['Close'], timeperiod=14)
    return df
