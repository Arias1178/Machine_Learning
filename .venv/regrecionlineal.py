import numpy as np
import pandas as pd 
import matplotlib
matplotlib.use("Agg") #usa un backend sin interfaz grafica
import matplotlib.pyplot as plit
import io
import base64
from sklearn.linear_model import LinearRegression


data = {
    "Horas Estudiadas": [10, 15, 12, 8, 14, 5, 16, 7, 11, 13, 9, 4, 18, 3, 17, 6, 14, 2, 20, 1],
    "Grado Final": [3.8, 4.2, 3.6, 3, 4.5, 2.5, 4.8, 2.8, 3.7, 4, 3.2, 2.2, 5, 1.8, 4.9, 2.7, 4.4, 1.5, 5, 1]
}

df = pd.DataFrame(data)
x = df[["Horas Estudiadas"]]
y = df[["Grado Final"]]

#aqui se entrena al modelo
model_regresion = LinearRegression()
model_regresion .fit(x,y)

print("Columnas usadas en el entrenamiento:", model_regresion.feature_names_in_)

def calculateGrade(horas):
    horas = float(horas)  # Convertimos a float
    horas_df = pd.DataFrame({"Horas Estudiadas": [horas]})  # Aseguramos que coincida

    print("Datos enviados a la predicción:\n", horas_df)  # 🔍 Depuración

    resultado = model_regresion.predict(horas_df)[0][0]  # Extraemos el valor de la predicción
    return resultado

def grafica_regresion(nueva_hora=None):
    #plitfigure crea el tamaño de la grafica
    plit.figure(figsize=(8,6))
    #puntos datos reales
    #crear el grafico de dispersion plit.scatter
    plit.scatter(df["Horas Estudiadas"],df["Grado Final"],color="blue", label="Datos reales")
    # Si se ha introducido una nueva hora, la agregamos como un punto verde
    if nueva_hora is not None:
        nuevo_grado = calculateGrade(nueva_hora)
        plit.scatter([nueva_hora], [nuevo_grado], color="green", s=100, label="Nueva predicción", marker= "x")
    #lienas de regresion
    #creamo los valores que van a aparecer en x con un maximo de 100 valores desde 0 y el reshape cambia la forma de los datos para que se lean correctamente y el np.linspace genera mas puntos intermedios para que la linea se vea mas fluida
    x_linea = np.linspace(min(df["Horas Estudiadas"]),max(df["Horas Estudiadas"]),100).reshape(-1,1)
    y_linea = model_regresion.predict(x_linea)
    #dibuja una linea de regresion en el grafico, la linea que aparece va a ser roja y laber agrega una etiqueta
    plit.plot (x_linea, y_linea, color="red", label="regresion lineal")
    #etiquetas y titulos
    plit.xlabel("Horas Estudiadas")#label para nombrar los ejes
    plit.ylabel("Grado Final")
    plit.title("Regresion Lineal: Horas Estudiadas vs Grado Final")#nombre para la grafica
    plit.legend()#muestra las leyendas de los graficos que fue la de plitplot y scartter
    
    #Guardamos la imagen en base64 para usarla en html
    img = io.BytesIO()
    plit.savefig(img, format='png')#guarda la figura creada como imagen.png
    img.seek(0)#reubica el puntero
    grafico_url = base64.b64encode(img.getvalue()).decode()#se guarda como base64 para importarla a html
    plit.close()

    return grafico_url # devuelve la grafica




