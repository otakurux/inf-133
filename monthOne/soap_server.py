from http.server import HTTPSever
from pysimplesoap.server import SoapDispatcher, SOAPHandler

def saluter(name):
    return "hello, f{name}"
dispatcher = SoapDispatcher(
    "ejemplo.soap-server",
    location = "http://localhost:8000",
    action = "http://localhost:8000",
    namespace = "http://localhost:8000",
    trace = true,
    ns = true,
)

dispatcher.register.register_function(
    "saluter",
    saluter,
    returns = {"saludo":str},
    args =  {"name": str}
)

server = HTTPSever(("0.0.0.0", 8000), SOAPHandler)
server.dispatcher = dispatcher
print("Servidor SOAP iniciando en http://localhost:8000/")
server.serve_forever()