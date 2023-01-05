from flask import Flask, request, redirect

import persistencia

app = Flask(__name__)


@app.route("/pizza", methods=["POST"])
def solicitar_pizza():
    nombre = request.form.get("nombre")
    apellidos = request.form.get("apellidos")

    print(nombre + " " + apellidos)

    persistencia.guardar_pedido(nombre, apellidos)

    return redirect("http://localhost/solicita_pedido.html", code=302)
