import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

try:
    archivo_csv = "datos_procesados.csv"
    dataframe = pd.read_csv(archivo_csv)

    # eliminar xd
    X = dataframe.drop(columns=['DEATH_EVENT', 'age', 'categoria_edad'])

    # vector y 
    y = dataframe['age']

    # lo del modelo lineal 
    model = LinearRegression()
    model.fit(X, y)

    # aprocimacion edades       AUN SIGO SIN ENTENDER BIEN PARA QUE ES ESTO 
    y_pred = model.predict(X)

    # masomenos el error
    mse = mean_squared_error(y, y_pred)

    print(f" El error cuadrático medio es: {mse}")

except FileNotFoundError:
    print(f"El archivo CSV en la ubicación '{archivo_csv}' no se encontró.")
except Exception as e:
    print(f"Error inesperado: {e}")
