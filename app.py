import re
from datetime import datetime
from flask import Flask, render_template,request
import regrecionlineal
import RegresionLogistica

app = Flask(__name__)


#Ejemplo clase
@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    match_object = re.match("[a-zA-Z]+", name)
    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friends"

    return render_template("index.html", name=clean_name, formatted_now=formatted_now)

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/", methods=["GET", "POST"])
def menu_formulario():
    seccion = None
    if request.method == "POST":
        seccion = request.form.get("seccion")
    return render_template("menu.html", seccion=seccion)

#Pagina casos de uso
@app.route("/exampleHTML/")
def exampleHTML():
    return render_template("casosdeuso.html")

#Mapa conceptual
@app.route("/mapa/")
def mapaHTML():
    return render_template("mapaconceptual.html")

#Rgresion Lineal
@app.route("/regrecionlineal", methods=["GET","POST"])

def regrecionlineal_endpoint():
    calcularResultado = None
    grafico_url = None
    if request.method=="POST":
       horas=float(request.form["Tiempo_actividad"])
       print(f"Valor recibido: {horas}")
       calcularResultado = regrecionlineal.calculateBienestar(horas)
       grafico_url = regrecionlineal.grafica_regresion(nuevo_tiempo=horas)
    return render_template("regrecionlineal.html", resultado=calcularResultado, grafico_url=grafico_url)

#if __name__ == "__main__":
 #   app.run(debug=True)#ejecutamo la aplicacion sin importar los errores del .py

#Regresión Logística

import joblib
from sklearn.preprocessing import StandardScaler


# Cargar modelo
model = joblib.load('modelo_fraude.pkl')

@app.route('/Sigmoid', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        # Obtener datos del formulario
        try:
            monto = float(request.form['monto'])
            tiempo = float(request.form['tiempo'])
            historial = float(request.form['historial'])
            
            # Crear DataFrame con los datos de entrada
            input_data = pd.DataFrame([[monto, tiempo, historial]], 
                                    columns=['Monto', 'Tiempo_Activacion', 'Historial'])
            
            # Hacer predicción
            prediction = model.predict(input_data)[0]
            prediction = "Fraude" if prediction == 1 else "No Fraude"
            
        except ValueError:
            prediction = "Error: Ingresa valores numéricos válidos"
    
    return render_template('RegresionLogistica.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True) 
