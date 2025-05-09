import re #para trabajar con expresiones regulares
from datetime import datetime
from flask import Flask, render_template, request, send_file
import joblib
import pandas as pd
import regrecionlineal
#import pyodbc
import os

EXCEL_PATH = 'resultados_diabetes.xlsx'
app = Flask(__name__)


# Configuración de conexión
#server = 'ModelosClasificacion.mssql.somee.com'
#database = 'ModelosClasificacion'
#username = 'isaVargas_SQLLogin_1'
#password = 'djz3g2kkhk'
#driver = '{ODBC Driver 17 for SQL Server}'
#connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'



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
historial = [] #guardar el historial de predicciones

@app.route('/Sigmoid', methods=['GET', 'POST'])
def sigmoidvista():
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



#XGBoost 8
# Carga del modelo entrenado
@app.route("/xgboost")
def xgmodelo():
   return render_template("XGBoost.html")

@app.route("/predecir", methods=["POST"])
def predecir():
    
    glucosa = float(request.form["glucosa"])
    edad = int(request.form["edad"])
    imc = float(request.form["imc"])
    modelo = joblib.load("modelo_diabetes.pkl")

    datos_nuevos = pd.DataFrame([{
        "Glucose": glucosa,
        "Age": edad,
        "BMI": imc
    }])

    prediccion = modelo.predict(datos_nuevos)[0]
    resultado = "Diabetes" if prediccion == 1 else "No Diabetes"
    
    
    registro = {
        'Glucosa': glucosa,
        'Edad': edad,
        'IMC': imc,
        'Resultado': resultado,
        'Fecha': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    historial.append(registro)

    return render_template("diabetes.html", resultado=resultado, historial=historial, datos=datos_nuevos.to_dict(orient="records")[0])

@app.route('/resultados')
def resultados():
    if not os.path.exists(EXCEL_PATH):
        return "No hay resultados aún."
    df = pd.read_excel(EXCEL_PATH)
    return render_template('resultados.html', tabla=df.to_dict(orient='records'))

@app.route('/exportar')
def exportar():
    if not historial:
        return "No hay datos para exportar."

    df = pd.DataFrame(historial)
    ruta_archivo = 'resultados_diabetes.xlsx'
    df.to_excel(ruta_archivo, index=False)

    return send_file(ruta_archivo, as_attachment=True)

if __name__ == '__main__':
  app.run(debug=True) 
