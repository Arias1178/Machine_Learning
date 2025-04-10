import pandas as pd
import numpy as np
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# Entrenarlo 
np.random.seed(42)
data = {
    "glucosa": np.random.randint(70, 200, 300),
    "edad": np.random.randint(18, 80, 300),
    "IMC": np.round(np.random.uniform(18, 40, 300), 1)
}
#prueba
df = pd.DataFrame(data)
df["diabetes"] = ((df["glucosa"] > 125) | (df["IMC"] > 30)).astype(int)

X = df[["glucosa", "edad", "IMC"]]
y = df["diabetes"]

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.3, random_state=42)

model = XGBClassifier(use_label_encoder=False, eval_metric="logloss")
model.fit(X_train, y_train)

# Evaluación
print(classification_report(y_test, model.predict(X_test)))

# Guardar modelo
joblib.dump(model, "modelo_diabetes.pkl")
