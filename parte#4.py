import pandas as pd
import requests
from io import StringIO

# URL de los datos
url = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"

# Realizar una solicitud GET para descargar los datos
response = requests.get(url)

if response.status_code == 200:
    # Leer los datos en un DataFrame
    data = pd.read_csv(StringIO(response.text))
    
    # Realizar operaciones adicionales en el DataFrame si es necesario
    # Por ejemplo, puedes hacer un preprocesamiento de los datos aquí
    
    # Guardar el DataFrame en un archivo CSV si es necesario
    data.to_csv("datos_parte6.csv", index=False)
    print("Datos descargados y guardados como datos_procesados.csv")
else:
    print("No se pudo descargar los datos. Código de estado:", response.status_code)
