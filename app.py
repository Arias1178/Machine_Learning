import re
from datetime import datetime
from flask import Flask, render_template,request
import regrecionlineal

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Bebes"

@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    match_object = re.match("[a-zA-Z]+", name)
    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    return render_template("index.html", name=clean_name, formatted_now=formatted_now)

if __name__ == "__main__":
    app.run(debug=True)


@app.route("/exampleHTML/")
def exampleHTML():
    return render_template("example.html")


<<<<<<< Updated upstream
=======

#Menu
@app.route("/menuformulario", methods=["GET", "POST"])
def menu_formulario():
    seccion = None
    if request.method == "POST":
        seccion = request.form.get("seccion")
    return render_template("menu.html", seccion=seccion)

if __name__ == "__main__":
    app.run(debug=True)

#Rgresion Lineal
>>>>>>> Stashed changes
@app.route("/regrecionlineal", methods=["GET","POST"])
def regrecionlineal_endpoint():
    calcularResultado = None
    grafico_url = None
    if request.method=="POST":
       horas=float(request.form["horas"])
       print(f"Valor recibido: {horas}")
       calcularResultado = regrecionlineal.calculateGrade (horas)
       grafico_url = regrecionlineal.grafica_regresion(nueva_hora=horas)
    return render_template("regrecionlineal.html", resultado=calcularResultado, grafico_url=grafico_url)

if __name__ == "__main__":
    app.run(debug=True)#ejecutamo la aplicacion sin importar los errores del .py

#Regresion Logistica
@app.route("/RegresionLogistica/")
def regresion_logistica():
    return render_template("menu_regresion_logistica.html")
