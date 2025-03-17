import numpy as np

def calcular_rendimientos(data):
    if data is not None:
        data['Log Returns'] = np.log(data['Close'] / data['Close'].shift(1))
        data.dropna(inplace=True)  # Eliminar valores NaN generados por el cálculo
        print("✅ Rendimientos logarítmicos calculados correctamente.")
    else:
        print("⚠️ No se pueden calcular rendimientos: el DataFrame está vacío.")
    return data
