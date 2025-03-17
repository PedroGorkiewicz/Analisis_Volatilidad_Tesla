from descargar_datos import descargar_datos
from calcular_rendimientos import calcular_rendimientos
from statsmodels.tsa.arima.model import ARIMA
from arch import arch_model
from grafica_precio_cierre import graficar_precio_cierre
from graficar_volatilidad import graficar_volatilidad
from graficar_rendimientos_vs_volatilidad import graficar_rendimientos_vs_volatilidad
from predecir_volatilidad import predecir_volatilidad
from comparar_volatilidad import comparar_volatilidad

TICKER = "TSLA"
START_DATE = "2020-01-01"
END_DATE = "2023-01-01"

data = descargar_datos(TICKER, START_DATE, END_DATE)



data = calcular_rendimientos(data)
if data is not None:
    print(data.head())

model_arima = ARIMA(data['Log Returns'], order=(1, 0, 1))
result_arima = model_arima.fit()

# Resumen del modelo ARIMA
print(result_arima.summary())

model_garch = arch_model(data['Log Returns'], vol='Garch', p=1, q=1)
result_garch = model_garch.fit()

# Resumen del modelo GARCH
print(result_garch.summary())

graficar_precio_cierre(data, "TSLA", grid=False)
graficar_volatilidad(data, result_garch, "TSLA")
graficar_rendimientos_vs_volatilidad(data,result_garch, "TSLA")
volatility_forecast = predecir_volatilidad(result_garch, data, "TSLA", horizon=30)
comparar_volatilidad("TSLA", "2023-01-01", "2023-02-01", volatility_forecast, data)
