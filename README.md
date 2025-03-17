# Análisis de Volatilidad de Tesla (TSLA) con Modelos ARIMA y GARCH

Este proyecto tiene como objetivo analizar y predecir la volatilidad de las acciones de Tesla (TSLA) utilizando modelos econométricos, específicamente ARIMA y GARCH. A través de este análisis, buscamos comprender mejor el comportamiento de los rendimientos de las acciones y su volatilidad a lo largo del tiempo.

## Contenido del Proyecto

### El proyecto se divide en las siguientes etapas:

1. Descarga de Datos Históricos: Obtención de los precios históricos de las acciones de Tesla desde Yahoo Finance.​
2. Cálculo de Rendimientos Logarítmicos: Transformación de los precios en rendimientos logarítmicos para facilitar el análisis.
3. Ajuste del Modelo ARIMA: Modelado de los rendimientos para identificar patrones predecibles.
4. Ajuste del Modelo GARCH: Modelado de la volatilidad de los rendimientos para capturar la heterocedasticidad condicional.
5. Visualización de Precios Históricos: Gráficos que muestran la evolución de los precios de cierre de Tesla.
6. Visualización de la Volatilidad Estimada: Gráficos que muestran la volatilidad condicional estimada por el modelo GARCH.
7. Comparación de Rendimientos vs. Volatilidad: Análisis comparativo entre los rendimientos y la volatilidad estimada.
8. Predicción de Volatilidad Futura: Estimación de la volatilidad futura para los próximos 30 días.
9. Backtesting: Comparación de las predicciones de volatilidad con la volatilidad real observada en datos futuros.
10. Conclusiones: Resumen de hallazgos y posibles mejoras futuras.

## Archivos Principales

main.py: Script principal que ejecuta las diferentes etapas del análisis.​
descargar_datos.py: Contiene la función descargar_datos() para descargar los datos históricos.​
calcular_rendimientos.py: Incluye la función calcular_rendimientos() para calcular los rendimientos logarítmicos.​
graficas.py: Contiene funciones para la visualización de datos, como graficar_precio_cierre(), graficar_volatilidad() y graficar_rendimientos_vs_volatilidad().​
predicciones.py: Incluye la función predecir_volatilidad() para realizar predicciones de volatilidad futura.​
backtesting.py: Contiene la función comparar_volatilidad() para realizar el backtesting de las predicciones.

## Requisitos

### Para ejecutar este proyecto, necesitarás las siguientes bibliotecas de Python:

- pandas
- numpy
- matplotlib
- yfinance
- statsmodels
- arch

Puedes instalar las bibliotecas necesarias utilizando pip:

pip install pandas numpy matplotlib yfinance statsmodels arch

## Cómo Ejecutar el Proyecto

1. Clona este repositorio en tu máquina local.​
2. Asegúrate de tener instaladas las bibliotecas requeridas.​
3. Ejecuta el script principal main.py:

   python main.py

## Resultados y Conclusiones

Modelo ARIMA: Los coeficientes AR(1) y MA(1) no fueron estadísticamente significativos, lo que sugiere que los rendimientos de Tesla siguen un comportamiento aleatorio y no son fácilmente predecibles mediante este modelo.​
Modelo GARCH: Se observó que la volatilidad tiene una alta persistencia en el tiempo, y los choques recientes en el mercado afectan significativamente la volatilidad futura.​
Predicciones: Las predicciones de volatilidad fueron bastante precisas, aunque se sugiere explorar modelos más avanzados, como EGARCH o GJR-GARCH, para capturar posibles asimetrías en la volatilidad.​

## Posibles Mejoras

Explorar modelos de volatilidad asimétrica, como EGARCH o GJR-GARCH.​
Utilizar distribuciones alternativas, como la t-Student, para modelar los residuos y capturar eventos extremos.​
Implementar un enfoque de pronóstico móvil (rolling forecast) para mejorar la precisión de las predicciones.


