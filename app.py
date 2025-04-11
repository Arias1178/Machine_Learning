import re #para trabajar con expresiones regulares
from datetime import datetime
from flask import Flask, render_template, request, send_file
import joblib
import pandas as pd
import regrecionlineal
#import pyodbc
import os


app = Flask(__name__)


# Configuración de conexión
server = 'ModelosClasificacion.mssql.somee.com'
database = 'ModelosClasificacion'
username = 'isaVargas_SQLLogin_1'
password = 'djz3g2kkhk'
driver = '{ODBC Driver 17 for SQL Server}'
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'



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

#Menu
@app.route("/", methods=["GET", "POST"])
def menu_formulario():
    seccion = None
    if request.method == "POST":
        seccion = request.form.get("seccion")
    return render_template("menu.html", seccion=seccion)


#Pagina casos de uso 3
@app.route("/exampleHTML/")
def exampleHTML():
    return render_template("casosdeuso.html")

#Mapa conceptual 4
@app.route("/mapa/")
def mapaHTML():
    return render_template("mapaconceptual.html")

#Rgresion Lineal 5
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

#Info Regresion Logistica 7
'''@app.route('/infoRegresionLogistica/')
def infoRegresionLogistica():
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM modelo where idModelo = 1;")
        row = cursor.fetchone()
        if row:
            modelo = {
                'nombre': row.nombre,
                'descripcion': row.descripcion,
                'enlace': row.enlace,
                'imagen': row.imagen
            }
            return render_template('infoRegresionLogistica.html', modelo=modelo)
        else:
            return "No se encontró ningún modelo en la base de datos."
    except Exception as e:
        return f"Error: {e}"

#Info KNN 7
@app.route('/infoKNN/')
def infoKNN():
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM modelo where idModelo = 2;")
        row = cursor.fetchone()
        if row:
            modelo = {
                'nombre': row.nombre,
                'descripcion': row.descripcion,
                'enlace': row.enlace,
                'imagen': row.imagen
            }
            return render_template('infoKNN.html', modelo=modelo)
        else:
            return "No se encontró ningún modelo en la base de datos."
    except Exception as e:
        return f"Error: {e}"

#Info Arboles Decision
@app.route('/infoArbolesDecision/')
def infoArbolesDecision():
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM modelo where idModelo = 3;")
        row = cursor.fetchone()
        if row:
            modelo = {
                'nombre': row.nombre,
                'descripcion': row.descripcion,
                'enlace': row.enlace,
                'imagen': row.imagen
            }
            return render_template('infoArbolesDecision.html', modelo=modelo)
        else:
            return "No se encontró ningún modelo en la base de datos."
    except Exception as e:
        return f"Error: {e}"

#Info Random Forest
@app.route('/infoRandomForest/')
def infoRandomForest():
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM modelo where idModelo = 4;")
        row = cursor.fetchone()
        if row:
            modelo = {
                'nombre': row.nombre,
                'descripcion': row.descripcion,
                'enlace': row.enlace,
                'imagen': row.imagen
            }
            return render_template('infoRandomForest.html', modelo=modelo)
        else:
            return "No se encontró ningún modelo en la base de datos."
    except Exception as e:
        return f"Error: {e}"

#Info SVM
@app.route('/infoSVM/')
def infoSVM():
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM modelo where idModelo = 5;")
        row = cursor.fetchone()
        if row:
            modelo = {
                'nombre': row.nombre,
                'descripcion': row.descripcion,
                'enlace': row.enlace,
                'imagen': row.imagen
            }
            return render_template('infoSVM.html', modelo=modelo)
        else:
            return "No se encontró ningún modelo en la base de datos."
    except Exception as e:
        return f"Error: {e}"

#Info XGBoost
@app.route('/infoXGBoost/')
def infoXGBoost():
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM modelo where idModelo = 6;")
        row = cursor.fetchone()
        if row:
            modelo = {
                'nombre': row.nombre,
                'descripcion': row.descripcion,
                'enlace': row.enlace,
                'imagen': row.imagen
            }
            return render_template('infoXGBoost.html', modelo=modelo)
        else:
            return "No se encontró ningún modelo en la base de datos."
    except Exception as e:
        return f"Error: {e}"

#Info AdaBoost
@app.route('/infoAdaBoost/')
def infoAdaBoost ():
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM modelo where idModelo = 7;")
        row = cursor.fetchone()
        if row:
            modelo = {
                'nombre': row.nombre,
                'descripcion': row.descripcion,
                'enlace': row.enlace,
                'imagen': row.imagen
            }
            return render_template('infoAdaBoost.html', modelo=modelo)
        else:
            return "No se encontró ningún modelo en la base de datos."
    except Exception as e:
        return f"Error: {e}"

#Info Naive Bayes
@app.route('/infoNaiveBayes/')
def infoNaiveBayes ():
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM modelo where idModelo = 8;")
        row = cursor.fetchone()
        if row:
            modelo = {
                'nombre': row.nombre,
                'descripcion': row.descripcion,
                'enlace': row.enlace,
                'imagen': row.imagen
            }
            return render_template('infoNaiveBayes.html', modelo=modelo)
        else:
            return "No se encontró ningún modelo en la base de datos."
    except Exception as e:
        return f"Error: {e}"

#Info Regresion Logistica
@app.route('/infoRegresionLogistica/')
def infoRegresionLogistica():
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM modelo where idModelo = 1;")
        row = cursor.fetchone()
        if row:
            modelo = {
                'nombre': row.nombre,
                'descripcion': row.descripcion,
                'enlace': row.enlace,
                'imagen': row.imagen
            }
            return render_template('infoRegresionLogistica.html', modelo=modelo)
        else:
            return "No se encontró ningún modelo en la base de datos."
    except Exception as e:
        return f"Error: {e}"

#Info KNN
@app.route('/infoKNN/')
def infoKNN():
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM modelo where idModelo = 2;")
        row = cursor.fetchone()
        if row:
            modelo = {
                'nombre': row.nombre,
                'descripcion': row.descripcion,
                'enlace': row.enlace,
                'imagen': row.imagen
            }
            return render_template('infoKNN.html', modelo=modelo)
        else:
            return "No se encontró ningún modelo en la base de datos."
    except Exception as e:
        return f"Error: {e}"

#Info Arboles Decision
@app.route('/infoArbolesDecision/')
def infoArbolesDecision():
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM modelo where idModelo = 3;")
        row = cursor.fetchone()
        if row:
            modelo = {
                'nombre': row.nombre,
                'descripcion': row.descripcion,
                'enlace': row.enlace,
                'imagen': row.imagen
            }
            return render_template('infoArbolesDecision.html', modelo=modelo)
        else:
            return "No se encontró ningún modelo en la base de datos."
    except Exception as e:
        return f"Error: {e}"

#Info Random Forest
@app.route('/infoRandomForest/')
def infoRandomForest():
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM modelo where idModelo = 4;")
        row = cursor.fetchone()
        if row:
            modelo = {
                'nombre': row.nombre,
                'descripcion': row.descripcion,
                'enlace': row.enlace,
                'imagen': row.imagen
            }
            return render_template('infoRandomForest.html', modelo=modelo)
        else:
            return "No se encontró ningún modelo en la base de datos."
    except Exception as e:
        return f"Error: {e}"

#Info SVM
@app.route('/infoSVM/')
def infoSVM():
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM modelo where idModelo = 5;")
        row = cursor.fetchone()
        if row:
            modelo = {
                'nombre': row.nombre,
                'descripcion': row.descripcion,
                'enlace': row.enlace,
                'imagen': row.imagen
            }
            return render_template('infoSVM.html', modelo=modelo)
        else:
            return "No se encontró ningún modelo en la base de datos."
    except Exception as e:
        return f"Error: {e}"

#Info XGBoost
@app.route('/infoXGBoost/')
def infoXGBoost():
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM modelo where idModelo = 6;")
        row = cursor.fetchone()
        if row:
            modelo = {
                'nombre': row.nombre,
                'descripcion': row.descripcion,
                'enlace': row.enlace,
                'imagen': row.imagen
            }
            return render_template('infoXGBoost.html', modelo=modelo)
        else:
            return "No se encontró ningún modelo en la base de datos."
    except Exception as e:
        return f"Error: {e}"

#Info AdaBoost
@app.route('/infoAdaBoost/')
def infoAdaBoost ():
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM modelo where idModelo = 7;")
        row = cursor.fetchone()
        if row:
            modelo = {
                'nombre': row.nombre,
                'descripcion': row.descripcion,
                'enlace': row.enlace,
                'imagen': row.imagen
            }
            return render_template('infoAdaBoost.html', modelo=modelo)
        else:
            return "No se encontró ningún modelo en la base de datos."
    except Exception as e:
        return f"Error: {e}"

#Info Naive Bayes
@app.route('/infoNaiveBayes/')
def infoNaiveBayes ():
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM modelo where idModelo = 8;")
        row = cursor.fetchone()
        if row:
            modelo = {
                'nombre': row.nombre,
                'descripcion': row.descripcion,
                'enlace': row.enlace,
                'imagen': row.imagen
            }
            return render_template('infoNaiveBayes.html', modelo=modelo)
        else:
            return "No se encontró ningún modelo en la base de datos."
    except Exception as e:
        return f"Error: {e}" '''


#if __name__ == "__main__":
 #   app.run(debug=True)#ejecutamo la aplicacion sin importar los errores del .py

#Regresión Logística
# Cargar modelo 6
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


#if __name__ == '__main__':
 #   app.run(debug=True) 

#XGBoost 8
# Carga del modelo entrenado
modelo = joblib.load("modelo_diabetes.pkl")
@app.route("/XGBoost", methods=["GET", "POST"])
def resultado():
    tabla = None

    if request.method == "POST":
        if "archivo" in request.files:
            archivo = request.files["archivo"]
            df = pd.read_excel(archivo)

            columnas = ["glucosa", "edad", "IMC"]
            if not all(col in df.columns for col in columnas):
                return "El archivo debe contener las columnas: glucosa, edad, IMC"

            predicciones = modelo.predict(df[columnas])
            df["Resultado"] = ["Diabetes" if x == 1 else "No Diabetes" for x in predicciones]

            df.to_excel("datos/resultados.xlsx", index=False)
            df.to_csv("datos/resultados.csv", index=False)

            tabla = df.to_html(classes="table", index=False)

        elif "formato" in request.form:
            formato = request.form["formato"]
            if formato == "excel":
                return send_file("datos/resultados.xlsx", as_attachment=True)
            elif formato == "csv":
                return send_file("datos/resultados.csv", as_attachment=True)

    return render_template("XGBoost.html", tabla=tabla)

if __name__ == "__main__":
    app.run(debug=True)

 