import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

def comparar_volatilidad(ticker, start_date, end_date, garch_forecast, data):
    new_data = yf.download(ticker, start=start_date, end=end_date)
    new_data['Log Returns'] = np.log(new_data['Close'] / new_data['Close'].shift(1))
    new_data.dropna(inplace=True)
    window_size = 5  # Período de 5 días
    new_data['Realized Volatility'] = np.sqrt((new_data['Log Returns']**2).rolling(window=window_size).mean())
    available_dates = new_data.index
    garch_forecast_filtered = garch_forecast[:len(available_dates)]

    plt.figure(figsize=(12, 6))
    plt.plot(available_dates, garch_forecast_filtered, marker='o', linestyle='dashed', color='red', label="Predicción GARCH")
    plt.plot(new_data.index, new_data['Realized Volatility'], marker='s', linestyle='solid', color='blue', label="Volatilidad Real")
    plt.title(f"Comparación: Predicción de Volatilidad vs. Volatilidad Real ({ticker})")
    plt.xlabel("Fecha")
    plt.ylabel("Volatilidad")
    plt.legend()
    plt.grid(True)
    plt.show()