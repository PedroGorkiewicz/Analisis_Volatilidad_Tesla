import matplotlib.pyplot as plt

def graficar_volatilidad(data, result_garch, ticker):
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, result_garch.conditional_volatility, color='red', label="Volatilidad Condicional Estimada")
    plt.title(f"Evolución de la Volatilidad Estimada ({ticker})")
    plt.xlabel("Fecha")
    plt.ylabel("Volatilidad Condicional")
    plt.legend()
    plt.grid(False)
    plt.show()