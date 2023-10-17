import pandas as pd

def procesar_datos(dataframe):
    if dataframe.isnull().values.any():
        print("Existen valores faltantes en el DataFrame.")
    
    if dataframe.duplicated().any():
        print("Existen filas duplicadas en el DataFrame.")
    
    def categorizar_edades(edad):
        if edad <= 12:
            return "Niño"
        elif 13 <= edad <= 19:
            return "Adolescente"
        elif 20 <= edad <= 39:
            return "Jóvenes adulto"
        elif 40 <= edad <= 59:
            return "Adulto"
        else:
            return "Adulto mayor"
    
    dataframe['categoria_edad'] = dataframe['age'].apply(categorizar_edades)
    
    conteo_categorias = dataframe['categoria_edad'].value_counts()
    categorias = ["Niño", "Adolescente", "Jóvenes adulto", "Adulto", "Adulto mayor"]
    for categoria in categorias:
        cantidad = conteo_categorias.get(categoria, 0)
        print(f"{cantidad} datos en la categoría '{categoria}'")
    
    datos_duplicados = dataframe[dataframe.duplicated()]
    if not datos_duplicados.empty:
        print(f"{len(datos_duplicados)} datos duplicados encontrados.")
    else:
        print("No se encontraron datos duplicados.")
    
    dataframe.to_csv('datos_procesados.csv', index=False)
    print("Los datos procesados se han guardado en datos_procesados.csv")

nombre_archivo = "datos_descargados.csv"
dataframe = pd.read_csv(nombre_archivo)
procesar_datos(dataframe)
