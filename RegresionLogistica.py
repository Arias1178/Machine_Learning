#Provisto para Regresión Logística

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns #importar modelos estadisticos
import joblib

# Configuración para reproducibilidad
np.random.seed(42)

# Crear dataset sintético de 300 registros
n_samples = 300

data = {
    'Monto': np.round(np.random.gamma(5, scale=1000, size=n_samples), 2),
    'Tiempo_Activacion': np.random.randint(1, 730, size=n_samples),  # 1 día a 2 años
    'Historial': np.random.poisson(0.7, size=n_samples),  # Número de reclamos previos
}

df = pd.DataFrame(data)

# Generar variable objetivo (Fraude) de manera realista
def generar_fraude(row):
    prob = 0.05  # Probabilidad base
    
    # Factores que aumentan probabilidad de fraude
    if row['Monto'] > 8000:
        prob += 0.15
    if row['Tiempo_Activacion'] < 30:
        prob += 0.20
    if row['Historial'] > 2:
        prob += 0.10
    
    return 1 if np.random.random() < prob else 0

df['Fraude'] = df.apply(generar_fraude, axis=1)

# Guardar dataset
df.to_csv('fraude_dataset.csv', index=False)

print("Dataset creado con éxito. Distribución de fraudes:")
print(df['Fraude'].value_counts(normalize=True))

# Cargar dataset
df = pd.read_csv('fraude_dataset.csv')

# 1. Descripción del dataset
print("\nDescripción del dataset:")
print(df.describe())

# 2. División en train y test
X = df[['Monto', 'Tiempo_Activacion', 'Historial']]
y = df['Fraude']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# 3. Justificación de Regresión Logística:
# - Problema de clasificación binaria (fraude sí/no)
# - Queremos probabilidades de fraude
# - Relación lineal entre predictores y log-odds
# - Interpretabilidad de coeficientes

# 4. Ajuste del modelo
model = LogisticRegression(class_weight='balanced', max_iter=1000)
model.fit(X_train, y_train)

# 5. Predicciones
y_pred = model.predict(X_test)

# 6. Evaluación
print("\nMétricas de evaluación:")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print(f"Precision: {precision_score(y_test, y_pred):.2f}")
print(f"Recall: {recall_score(y_test, y_pred):.2f}")

# Matriz de confusión
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['No Fraude', 'Fraude'],
            yticklabels=['No Fraude', 'Fraude'])
plt.title('Matriz de Confusión')
plt.xlabel('Predicho')
plt.ylabel('Real')
plt.savefig('static/confusion_matrix.png')
plt.close()

# Guardar modelo
joblib.dump(model, 'modelo_fraude.pkl')
