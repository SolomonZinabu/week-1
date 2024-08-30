import pandas as pd
import talib

def load_stock_data(file_path):
    return pd.read_csv(file_path)

# def calculate_technical_indicators(df):
#     df['SMA'] = talib.SMA(df['Close'], timeperiod=20)
#     df['RSI'] = talib.RSI(df['Close'], timeperiod=14)
#     return df


def calculate_indicators(data):
    data['SMA_20'] = talib.SMA(data['Close'], timeperiod=20)
    data['RSI'] = talib.RSI(data['Close'], timeperiod=14)
    data['MACD'], data['MACD_signal'], data['MACD_hist'] = talib.MACD(data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    return data