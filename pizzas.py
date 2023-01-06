"""
API de Pizzas
"""

from flask import Flask, request, redirect, Response

import persistencia

app = Flask(__name__)


@app.route("/pizza", methods=["POST"])
def solicitar_pizza():
    """
    Guarda los datos de un pedido
    """
    nombre = request.form.get("nombre")
    apellidos = request.form.get("apellidos")

    print(nombre + " " + apellidos)

    persistencia.guardar_pedido(nombre, apellidos)

    return redirect("http://localhost/solicita_pedido.html", code=302)

@app.route("/checksize", methods=["POST"])
def checksize():
    """
    Comprueba disponibilidad de un tamaño de pizza.
    """
    size = request.form.get("size")

    mensaje = "No disponible" if size == "S" else "Disponible"

    return Response(mensaje, 200, {"Access-Control-Allow-Origin": "*"})
