import pandas as pd
import matplotlib.pyplot as plt

try:
    
    archivo_csv = "datos_procesados.csv"
    dataframe = pd.read_csv(archivo_csv)

    
    anemic_count = dataframe['anaemia'].sum()
    diabetic_count = dataframe['diabetes'].sum()
    smoking_count = dataframe['smoking'].sum()
    death_count = dataframe['DEATH_EVENT'].sum()

    # Crear un gráfico con subplots de torta
    plt.figure(figsize=(12, 6))

    # Subplot 1: Cantidad de anémicos
    plt.subplot(2, 2, 1)
    labels = ['No Anémicos', 'Anémicos']
    sizes = [len(dataframe) - anemic_count, anemic_count]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title('Distribución de Anémicos')

    # Subplot 2: Cantidad de diabéticos
    plt.subplot(2, 2, 2)
    labels = ['No Diabéticos', 'Diabéticos']
    sizes = [len(dataframe) - diabetic_count, diabetic_count]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title('Distribución de Diabéticos')

    # Subplot 3: Cantidad de fumadores
    plt.subplot(2, 2, 3)
    labels = ['No Fumadores', 'Fumadores']
    sizes = [len(dataframe) - smoking_count, smoking_count]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title('Distribución de Fumadores')

    # Subplot 4: Cantidad de muertos
    plt.subplot(2, 2, 4)
    labels = ['Vivos', 'Muertos']
    sizes = [len(dataframe) - death_count, death_count]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title('Distribución de Muertos')

    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print(f"El archivo CSV en la ubicación '{archivo_csv}' no se encontró.")
except Exception as e:
    print(f"Error inesperado: {e}")
