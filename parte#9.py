#NO GUSTAR ESTAR PARTE

import pandas as pd
import numpy as np
from sklearn.manifold import TSNE
import plotly.express as px

try:
    archivo_csv = "datos_procesados.csv"
    dataframe = pd.read_csv(archivo_csv)

    X = dataframe.drop(columns=['DEATH_EVENT', 'categoria_edad']).values
    y = dataframe['DEATH_EVENT'].values

    X_embedded = TSNE(n_components=3, learning_rate='auto', init='random', perplexity=3).fit_transform(X)

    df_embedded = pd.DataFrame({'Dimension 1': X_embedded[:, 0], 'Dimension 2': X_embedded[:, 1], 'Dimension 3': X_embedded[:, 2], 'DEATH_EVENT': y})

    fig = px.scatter_3d(df_embedded, x='Dimension 1', y='Dimension 2', z='Dimension 3', color='DEATH_EVENT',
                         color_discrete_sequence=['blue', 'red'], title='Visualización 3D de Datos')

    fig.update_traces(marker=dict(size=5, opacity=0.7))
    fig.update_layout(scene=dict(
        xaxis_title='Dimensión 1',
        yaxis_title='Dimensión 2',
        zaxis_title='Dimensión 3',
        bgcolor='lightgray',
    ))
    fig.update_layout(legend=dict(title='DEATH_EVENT', bgcolor='white'))
    fig.update_layout(title_font=dict(size=24))

    fig.show()

except FileNotFoundError:
    print(f"El archivo CSV en la ubicación '{archivo_csv}' no se encontró.")
except Exception as e:
    print(f"Error inesperado: {e}")
