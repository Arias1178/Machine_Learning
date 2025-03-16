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


@app.route("/exampleHTML/")
def exampleHTML():
    return render_template("example.html")



@app.route("/regrecionlineal", methods=["GET","POST"])
def regrecionlineal_endpoint():
    calcularResultado = None
    grafico_url = None
    if request.method=="POST":
       tiempo=float(request.form["Tiempo_actividad"])
       print(f"Valor recibido: {tiempo}")
       calcularResultado = regrecionlineal.calculateBienestar (tiempo)
       grafico_url = regrecionlineal.grafica_regresion(nuevo_tiempo=tiempo)
    return render_template("regrecionlineal.html", resultado=calcularResultado, grafico_url=grafico_url)

if __name__ == "__main__":
    app.run(debug=True)