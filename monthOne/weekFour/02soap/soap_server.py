from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

def greet(name):
    return "¡Hello, {}!".format(name)

def sum(num1, num2):
    return num1 + num2
    
def is_palindrome(word):
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
    "sum",
    sum,
    returns={"sum": int},
    args={"num1": int,
          "num2": int
          },
)

dispatcher.register_function(
    "is_palindrome",
    is_palindrome,
    returns={"is_palindrome": bool},
    args={"word": str},
)

server = HTTPServer(("0.0.0.0", 8000), SOAPHandler)
server.dispatcher = dispatcher
print("Server SOAP initiate en http://localhost:8000/")
server.serve_forever()


# PySimpleSOAP