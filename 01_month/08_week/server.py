# Importa la clase Flask del paquete flask
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "¡Hola, mundo!"

@app.route("/saludar", methods=["GET"])
def saludar():
    nombre = request.args.get("nombre")
    if not nombre:
        return (
            jsonify({"error": "Se requiere un nombre en los parámetros de la URL."}),
            400,
        )
    return jsonify({"mensaje": f"¡Hola, {nombre}!"})

@app.route("/sumar", methods=["GET"])
def sumar():
    num1 = int(request.args.get("num1"))
    num2 = int(request.args.get("num2"))
    if not num1 or not num2:
        return (
            jsonify({"error": "Se requiere un nombre en los parámetros de la URL."}),
            400,
        )
    return jsonify({"mensaje": num1 + num2})

def es_palindroma(cadena):
    if cadena == cadena[::-1]:
        return "espalindromo"
    else:
        return "no es espalindromo"


@app.route("/palindromo", methods=["GET"])
def palindromo():
    cadena = request.args.get("cadena")
    if not cadena:
        return (
            jsonify({"error": "Se requiere un cadena en los parametros de la URL."}),
            400,
        )
    return jsonify({"mensaje": es_palindroma(cadena)})

def contar_vocal(cadena, vocal):
    num = 0
    for i in range(len(cadena)):
        if cadena[i] == vocal:
            num += 1
    return num

@app.route("/contar", methods=["GET"])
def contar():
    cadena = request.args.get("cadena")
    vocal = request.args.get("vocal")
    if not cadena:
        return (
            jsonify({"error": "Se requiere un cadena en los parametros de la URL."}),
            400,
        )
    return jsonify({"mensaje": contar_vocal(cadena, vocal)})


if __name__ == "__main__":
    app.run()