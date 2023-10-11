import requests

def descargar_csv_desde_url(url, nombre_archivo):
    try:
        respuesta = requests.get(url)
        
        if respuesta.status_code == 200:
            with open(nombre_archivo, 'wb') as archivo:
                archivo.write(respuesta.content)
            print(f"Los datos se han descargado y guardado en {nombre_archivo} correctamente.")
        else:
            print(f"La solicitud GET no fue exitosa. Código de estado: {respuesta.status_code}")
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")

url = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"
nombre_archivo = "datos_descargados.csv"
descargar_csv_desde_url(url, nombre_archivo)
