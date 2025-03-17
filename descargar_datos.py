import yfinance as yf
import pandas as pd

def descargar_datos(ticker, start_date, end_date):
    try:
        data = yf.download(ticker, start=start_date, end=end_date)

        if data.empty:
            print(f"⚠️ No se encontraron datos para {ticker}. Revisa el símbolo y las fechas.")
            return None

        print(f"✅ Datos descargados correctamente para {ticker}.")
        return data

    except Exception as e:
        print(f"❌ Error al descargar los datos de {ticker}: {e}")
        return None