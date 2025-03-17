import matplotlib.pyplot as plt

def graficar_precio_cierre(data, ticker, grid=False):
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Close'], label=f"Precio de Cierre de {ticker}", color='blue')
    plt.title(f"Evolución del Precio de Cierre de {ticker}")
    plt.xlabel("Fecha")
    plt.ylabel("Precio (USD)")
    plt.legend()
    plt.grid(grid)  # Permite activar/desactivar la grilla
    plt.show()
    