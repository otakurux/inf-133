from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Database simulated pizzas
pizzas = {}
num = 0


# Product: Pizza
class Pizza:
    def __init__(self, size, mass, toppings):
        self.size = size
        self.mass = mass
        self.toppings = toppings

    def __str__(self):
        return f"Size: {self.size}, Mass: {self.mass}, Toppings: {', '.join(self.toppings)}"


# Factory: Pizza Factory
class PizzaFactory:
    def create_pizza(self, size, mass, toppings):
        return Pizza(size, mass, toppings)


# Service: Pizza Service
class PizzaService:
    def __init__(self, pizza_factory):
        self.pizza_factory = pizza_factory

    def create_pizza(self, size, mass, toppings):
        pizza = self.pizza_factory.create_pizza(size, mass, toppings)
        pizzas[num] = pizza
        num += 1
        return pizza

    def read_pizzas(self):
        return {index: pizza.__dict__ for index, pizza in pizzas.items()}

    def update_pizza(self, index, size=None, mass=None, toppings=None):
        if index in pizzas:
            pizza = pizzas[index]
            if size:
                pizza.size = size
            if mass:
                pizza.mass = mass
            if toppings:
                pizza.toppings = toppings
            return pizza
        else:
            return None

    def delete_pizza(self, index):
        return pizzas.pop(index, None)


class HTTPDataHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

    @staticmethod
    def handle_reader(handler):
        content_length = int(handler.headers["Content-Length"])
        post_data = handler.rfile.read(content_length)
        return json.loads(post_data.decode("utf-8"))


class PizzaHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.pizza_service = kwargs.pop('pizza_service')
        super().__init__(*args, **kwargs)

    def do_POST(self):
        if self.path == "/pizzas":
            data = HTTPDataHandler.handle_reader(self)
            size = data.get("size")
            mass = data.get("mass")
            toppings = data.get("toppings", [])
            response_data = self.pizza_service.create_pizza(size, mass, toppings)
            HTTPDataHandler.handle_response(self, 200, response_data.__dict__)
        else:
            HTTPDataHandler.handle_response(self, 404, {"Error": "Ruta no existente"})

    def do_GET(self):
        if self.path == "/pizzas":
            response_data = self.pizza_service.read_pizzas()
            HTTPDataHandler.handle_response(self, 200, response_data)
        else:
            HTTPDataHandler.handle_response(self, 404, {"Error": "Ruta no existente"})

    def do_PUT(self):
        if self.path.startswith("/pizzas/"):
            index = int(self.path.split("/")[2])
            data = HTTPDataHandler.handle_reader(self)
            size = data.get("size")
            mass = data.get("mass")
            toppings = data.get("toppings")
            response_data = self.pizza_service.update_pizza(index, size, mass, toppings)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data.__dict__)
            else:
                HTTPDataHandler.handle_response(self, 404, {"Error": "Indice de pizza no valid"})
        else:
            HTTPDataHandler.handle_response(self, 404, {"Error": "Ruta no existente"})

    def do_DELETE(self):
        if self.path.startswith("/pizzas/"):
            index = int(self.path.split("/")[2])
            deleted_pizza = self.pizza_service.delete_pizza(index)
            if deleted_pizza:
                HTTPDataHandler.handle_response(self, 200, {"message": "Pizza eliminada correctamente"})
            else:
                HTTPDataHandler.handle_response(self, 404, {"Error": "Indice de pizza no valid"})
        else:
            HTTPDataHandler.handle_response(self, 404, {"Error": "Ruta no existente"})


def run(server_class=HTTPServer, handler_class=PizzaHandler, port=8000):
    pizza_factory = PizzaFactory()
    pizza_service = PizzaService(pizza_factory)
    server_address = ("", port)
    httpd = server_class(server_address, lambda *args, **kwargs: handler_class(*args, **kwargs, pizza_service=pizza_service))
    print(f"Iniciando servidor HTTP en puerto {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
