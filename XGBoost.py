# Proyecto: Clasificación de diabetes usando XGBoost y Flask

import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 1. Cargar datos originales
df = pd.read_csv("diabetes.csv")  # Dataset original de diabetes

# 2. Selección de columnas relevantes
# - Se seleccionan solo las variables más representativas según análisis previo:
#   Glucose (glucosa), Age (edad), BMI (índice de masa corporal)
X = df[['Glucose', 'Age', 'BMI']]
y = df['Outcome']  # Variable objetivo: 1 (diabetes) o 0 (no diabetes)

print("Columnas usadas en el entrenamiento:", list(X.columns))

# 3. División del dataset en conjunto de entrenamiento y prueba
# - test_size=0.2 indica que el 20% se reserva para pruebas
# - stratify=y garantiza que la proporción de clases se mantiene
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 4. Inicialización y entrenamiento del modelo XGBoost
# - n_estimators: número de árboles
# - learning_rate: velocidad de aprendizaje
# - use_label_encoder=False: desactiva advertencias
# - eval_metric: métrica utilizada internamente (logloss para clasificación)
modelo = XGBClassifier(
    n_estimators=100,
    learning_rate=0.1,
    use_label_encoder=False,
    eval_metric='logloss'
)
modelo.fit(X_train, y_train)

# 5. Predicción sobre el conjunto de prueba
y_pred = modelo.predict(X_test)

# 6. Evaluación del modelo
print("\nEvaluación del modelo:")
print("Accuracy:", accuracy_score(y_test, y_pred))  # Precisión total
print("\nReporte de clasificación:")
print(classification_report(y_test, y_pred))  # Métricas por clase

# 7. Matriz de confusión (puedes graficarla si lo deseas)
cm = confusion_matrix(y_test, y_pred)
print("\nMatriz de confusión:")
print(cm)

# 8. Guardar el modelo entrenado
joblib.dump(modelo, 'modelo_diabetes.pkl')

print("\nModelo guardado exitosamente como modelo_diabetes.pkl")