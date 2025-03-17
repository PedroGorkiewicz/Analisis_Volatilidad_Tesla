import matplotlib.pyplot as plt

def graficar_rendimientos_vs_volatilidad(data, result_garch, ticker):

    fig, ax = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    ax[0].plot(data.index, data['Log Returns'], label="Rendimientos Logarítmicos", color='blue')
    ax[0].set_title(f"Rendimientos Logarítmicos de {ticker}")
    ax[0].set_ylabel("Rendimiento")
    ax[0].legend()
    ax[0].grid(False)

    ax[1].plot(data.index, result_garch.conditional_volatility, label="Volatilidad Estimada", color='red')
    ax[1].set_title(f"Evolución de la Volatilidad Estimada ({ticker})")
    ax[1].set_xlabel("Fecha")
    ax[1].set_ylabel("Volatilidad Condicional")
    ax[1].legend()
    ax[1].grid(False)

    plt.show()