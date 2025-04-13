import pandas as pd

# Dataset original del repositorio de sklearn (pero lo escribimos manualmente aquí)
columnas = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
            'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']

# Puedes descargarlo automáticamente desde un repositorio confiable si tienes conexión
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"

df = pd.read_csv(url, header=None, names=columnas)

# Guardarlo en tu carpeta actual
df.to_csv("diabetes.csv", index=False)

print("✅ Dataset 'diabetes.csv' guardado correctamente.")
