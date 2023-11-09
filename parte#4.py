import pandas as pd
import numpy as np
from sklearn.manifold import TSNE
import plotly.express as px

# Cargar el archivo CSV desde la URL
url = 'https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv'
df = pd.read_csv(url)

# Eliminar datos duplicados y ordenar el DataFrame por una columna (puedes reemplazar 'columna_de_orden' con la columna que desees)
df = df.drop_duplicates()
df = df.sort_values(by='columna_de_orden', ascending=True)  # Reemplaza 'columna_de_orden' por la columna adecuada

# Exportar una matriz con solo los valores de los atributos en formato de numpy array
X = df.drop(columns=['DEATH_EVENT', 'categoria_edad']).values

# Exportar un array unidimensional de solo la columna objetivo 'DEATH_EVENT'
y = df['DEATH_EVENT'].values

# Ejecutar el t-SNE con las opciones especificadas
X_embedded = TSNE(
    n_components=3,
    learning_rate='auto',
    init='random',
    perplexity=3
).fit_transform(X)

# Crear un DataFrame con los resultados de t-SNE y la columna objetivo 'DEATH_EVENT'
df_embedded = pd.DataFrame(X_embedded, columns=['X_embedded_1', 'X_embedded_2', 'X_embedded_3'])
df_embedded['DEATH_EVENT'] = y

# Crear el gráfico de dispersión 3D con Plotly
fig = px.scatter_3d(
    df_embedded,
    x='X_embedded_1',
    y='X_embedded_2',
    z='X_embedded_3',
    color='DEATH_EVENT',
    color_continuous_scale='Viridis',  # Puedes ajustar la paleta de colores
    labels={'DEATH_EVENT': 'Death Event'}
)

# Mostrar el gráfico
fig.show()
