from flask import Flask, request, redirect

app = Flask(__name__)


@app.route("/pizza", methods=["POST"])
def solicitar_pizza():
    nombre = request.form.get("nombre")
    apellidos = request.form.get("apellidos")

    print(nombre + " " + apellidos)

    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write(nombre + " " + apellidos + "\n")
        file.close

    return redirect("http://localhost/solicita_pedido.html", code=302)
