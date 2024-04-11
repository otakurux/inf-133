from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

def greet(name):
    return "¡Hello, {}!".format(name)

def SumaDosNumeros(num1, num2):
    return num1 + num2
    
def CadenaPalindromo(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]

dispatcher = SoapDispatcher(
    "example-soap-server",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns=True,
)

dispatcher.register_function(
    "greet",
    greet,
    returns={"greeting": str},
    args={"name": str},
)

dispatcher.register_function(
    "SumaDosNumeros",
    SumaDosNumeros,
    returns={"SumaDosNumeros": int},
    args={"num1": int,
          "num2": int
          },
)

dispatcher.register_function(
    "CadenaPalindromo",
    CadenaPalindromo,
    returns={"CadenaPalindromo": bool},
    args={"word": str},
)

server = HTTPServer(("0.0.0.0", 8000), SOAPHandler)
server.dispatcher = dispatcher
print("Server SOAP initiate en http://localhost:8000/")
server.serve_forever()


# PySimpleSOAP