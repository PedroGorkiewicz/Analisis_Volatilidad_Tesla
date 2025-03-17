import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def predecir_volatilidad(result_garch, data, ticker, horizon=30):
    forecast = result_garch.forecast(horizon=horizon)
    garch_vol_forecast = forecast.variance.iloc[-1].values
    volatility_forecast = np.sqrt(garch_vol_forecast)
    future_dates = pd.date_range(start=data.index[-1], periods=horizon+1)[1:]

    plt.figure(figsize=(10, 5))
    plt.plot(future_dates, volatility_forecast, marker='o', linestyle='dashed', color='red', label="Predicción de Volatilidad")
    plt.title(f"Predicción de Volatilidad para los Próximos {horizon} Días ({ticker})")
    plt.xlabel("Fecha")
    plt.ylabel("Volatilidad Condicional")
    plt.legend()
    plt.grid(True)
    plt.show()

    return volatility_forecast