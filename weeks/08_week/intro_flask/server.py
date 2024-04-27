from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "¡Hola, mundo!"

def generar_respuesta(mensaje, status_code):
    return jsonify({"mensaje": mensaje}), status_code, {"Content-Type": "application/json; charset=unicode-escape"}

@app.route("/saludar", methods=["GET"])
def saludar():
    nombre = request.args.get("nombre")
    if not nombre:
        return generar_respuesta("Se requiere un nombre en los parametros de la URL.", 400)
    return generar_respuesta(f"¡Hola, {nombre}!", 200)

@app.route("/sumar", methods=["GET"])
def sumar():
    try:
        num1 = int(request.args.get("num1"))
        num2 = int(request.args.get("num2"))
        mensaje = f"la suma de {num1} + {num2} = {num1 + num2}"
        return generar_respuesta(mensaje, 200)
    except ValueError:
        return generar_respuesta("Los parametros num1 y num2 deben ser numeros enteros.", 400)

def es_palindromo(cadena):
    return cadena == cadena[::-1]

@app.route("/palindromo", methods=["GET"])
def palindromo():
    cadena = request.args.get("cadena")
    if not cadena:
        return generar_respuesta("Se requiere una cadena en los parametros de la URL.", 400)
    mensaje = f"La cadena {cadena} es un palindromo." if es_palindromo(cadena) else f"La cadena {cadena} no es un palindromo."
    return generar_respuesta(mensaje, 200)

def contar_vocal(cadena, vocal):
    return cadena.lower().count(vocal.lower())

@app.route("/contar", methods=["GET"])
def contar():
    cadena = request.args.get("cadena")
    vocal = request.args.get("vocal")
    if not cadena or not vocal:
        return generar_respuesta("Se requiere una cadena y una vocal en los parametros de la URL.", 400)
    mensaje = f"La vocal '{vocal}' aparece {contar_vocal(cadena, vocal)} veces en la cadena {cadena}."
    return generar_respuesta(mensaje, 200)

if __name__ == "__main__":
    app.run()
