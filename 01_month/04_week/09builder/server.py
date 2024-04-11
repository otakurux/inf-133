from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Product: Pizza
class Pizza:
    def __init__(self):
        self.size = None
        self.mass = None
        self.toppings = []

    def __str__(self):
        return f"Size: {self.size}, Mass: {self.mass}, Toppings: {', '.join(self.toppings)}"

# Builder: Constructor de pizzas
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size

    def set_mass(self, mass):
        self.pizza.mass = mass

    def add_topping(self, topping):
        self.pizza.toppings.append(topping)

    def get_pizza(self):
        return self.pizza

# Director: Pizzeria
class Pizzeria:
    def __init__(self, builder):
        self.builder = builder

    def create_pizza(self, size, mass, toppings):
        self.builder.set_size(size)
        self.builder.set_mass(mass)
        for topping in toppings:
            self.builder.add_topping(topping)
        return self.builder.get_pizza()

class PizzaHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/pizza':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)

            data = json.loads(post_data.decode('utf-8'))

            size = data.get('size', None)
            mass = data.get('mass', None)
            toppings = data.get('toppings', [])

            builder = PizzaBuilder()
            pizzeria = Pizzeria(builder)

            pizza = pizzeria.create_pizza(size, mass, toppings)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            response = {
                'size': pizza.size,
                'mass': pizza.mass,
                'toppings': pizza.toppings
            }

            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=PizzaHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Iniciando servidor HTTP en puerto {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()