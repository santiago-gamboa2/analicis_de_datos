"""
esta es la url que tienen que poner en bash
 & "C:/Program Files/Python311/python.exe" c:/Users/USUARIO/Desktop/analicis_datos/parte#7.py https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv 
"""
# me hicieron odiar los graficos con este trabajo gracias 
import argparse
import pandas as pd
import requests
import io
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description="Descargar datos CSV desde una URL y categorizarlos.")

# Agregar un argumento para la URL
parser.add_argument("url", help="URL del archivo CSV")


args = parser.parse_args()

try:
    url_datos = args.url
    response = requests.get(url_datos)

    response.raise_for_status()

    
    response.headers['Content-Type'] = 'text/csv; charset=utf-8'

    
    dataframe = pd.read_csv(io.StringIO(response.content.decode('utf-8')))

    #  edad
    bins = [0, 30, 60, float('inf')]
    labels = ['Joven', 'Adulto', 'Mayor']
    dataframe['Grupo de Edad'] = pd.cut(dataframe['age'], bins=bins, labels=labels)

    # sexo y categoría
    fig, ax = plt.subplots(figsize=(10, 6))

    #  cantidad de hombres y mujeres en cada categoría
    men_data = dataframe[dataframe['sex'] == 1]
    women_data = dataframe[dataframe['sex'] == 0]
    
    men_counts = [men_data[men_data['anaemia'] == 1]['anaemia'].count(),
                  men_data[men_data['diabetes'] == 1]['diabetes'].count(),
                  men_data[men_data['smoking'] == 1]['smoking'].count(),
                  men_data[men_data['DEATH_EVENT'] == 1]['DEATH_EVENT'].count()]
    
    women_counts = [women_data[women_data['anaemia'] == 1]['anaemia'].count(),
                    women_data[women_data['diabetes'] == 1]['diabetes'].count(),
                    women_data[women_data['smoking'] == 1]['smoking'].count(),
                    women_data[women_data['DEATH_EVENT'] == 1]['DEATH_EVENT'].count()]
    
    categories = ['Anémicos', 'Diabéticos', 'Fumadores', 'Muertos']
    
    
    bar_width = 0.35

    men_x = range(len(categories))
    women_x = [x + bar_width for x in men_x]

   
    men_bars = ax.bar(men_x, men_counts, bar_width, label='Hombres', color='blue')
    women_bars = ax.bar(women_x, women_counts, bar_width, label='Mujeres', color='red')

    #   título
    ax.set_xlabel('Categorías')
    ax.set_ylabel('Cantidad')
    ax.set_title('Histograma Agrupado por Sexo')
    ax.set_xticks([x + bar_width / 2 for x in men_x])
    ax.set_xticklabels(categories)
    ax.legend()

    plt.show()

except requests.exceptions.RequestException as e:
    print(f"Error al hacer la solicitud: {e}")
except Exception as e:
    print(f"Error inesperado: {e}")
