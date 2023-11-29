import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
import matplotlib.pyplot as plt

try:
    archivo_csv = "datos_procesados.csv"
    dataframe = pd.read_csv(archivo_csv)

    # Eliminar la columna 'categoria_edad'
    dataframe = dataframe.drop(columns=['categoria_edad'])

    # Definir las variables independientes (X) y la variable dependiente (y)
    X = dataframe.drop(columns=['DEATH_EVENT'])
    y = dataframe['DEATH_EVENT']

    # Realizar la partición estratificada del dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

    # Ajustar un Random Forest
    rf_classifier = RandomForestClassifier(n_estimators=20, random_state=42)
    rf_classifier.fit(X_train, y_train)
    y_pred = rf_classifier.predict(X_test)

    # Calcular la matriz de confusión
    confusion = confusion_matrix(y_test, y_pred)

    # Calcular el accuracy y el F1-Score
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print(f"Matriz de Confusión:\n{confusion}")
    print(f"Accuracy: {accuracy:.2f}")
    print(f"F1-Score: {f1:.2f}")

    # Graficar la matriz de confusión
    plt.figure()
    plt.imshow(confusion, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title("Matriz de Confusión")
    plt.colorbar()
    plt.xticks([0, 1], ["No Muerte", "Muerte"])
    plt.yticks([0, 1], ["No Muerte", "Muerte"])
    #plt.xlabel("Predicho")
    #plt.ylabel("Verdadero")
    plt.show()

except FileNotFoundError:
    print(f"El archivo CSV en la ubicación '{archivo_csv}' no se encontró.")
except Exception as e:
    print(f"Error inesperado: {e}")
