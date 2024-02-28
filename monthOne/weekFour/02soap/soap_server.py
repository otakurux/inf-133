from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

def greet(name):
    return "¡Hello, {}!".format(name)

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

server = HTTPServer(("0.0.0.0", 8000), SOAPHandler)
server.dispatcher = dispatcher
print("Server SOAP initiate en http://localhost:8000/")
server.serve_forever()
