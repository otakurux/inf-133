from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class Chocolate:
    def __init__(self, chocolate_type, peso, taste, filling=None):
        self.chocolate_type = chocolate_type
        self.peso = peso
        self.taste = taste
        self.filling = filling

class DeliveryFactory:
    @staticmethod
    def create_chocolate(chocolate_type, peso, taste, filling=None):
        return Chocolate(chocolate_type, peso, taste, filling)

class ChocolateStore:
    def __init__(self):
        self.chocolates = {}
        self.chocolate_id_counter = 1
        self.factory = DeliveryFactory()

    def add_chocolate(self, data):
        chocolate_type = data.get("chocolate_type")
        peso = data.get("peso")
        taste = data.get("taste")
        filling = data.get("filling")

        delivery_chocolate = self.factory.create_chocolate(
            chocolate_type, peso, taste, filling
        )
        chocolate_id = self.chocolate_id_counter
        self.chocolates[chocolate_id] = delivery_chocolate
        self.chocolate_id_counter += 1
        return {"chocolate_id": chocolate_id}

    def list_chocolates(self):
        return {chocolate_id: chocolate.__dict__ for chocolate_id, chocolate in self.chocolates.items()}

    def update_chocolate(self, chocolate_id, data):
        if chocolate_id in self.chocolates:
            chocolate = self.chocolates[chocolate_id]
            peso = data.get("peso")
            taste = data.get("taste")
            filling = data.get("filling")

            if peso:
                chocolate.peso = peso
            if taste:
                chocolate.taste = taste
            if filling is not None:
                chocolate.filling = filling

            return {"message": "Chocolate actualizado"}
        else:
            return None

    def delete_chocolate(self, chocolate_id):
        if chocolate_id in self.chocolates:
            del self.chocolates[chocolate_id]
            return {"message": "Chocolate eliminado"}
        else:
            return None

class ChocolateRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, chocolate_store: ChocolateStore, **kwargs):
        self.chocolate_store = chocolate_store
        super().__init__(*args, **kwargs)

    def do_POST(self):
        if self.path == "/chocolates":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode("utf-8"))
            response_data = self.chocolate_store.add_chocolate(data)
            self._send_json_response(201, response_data)
        else:
            self._send_error_response(404, "Ruta no encontrada")

    def do_GET(self):
        if self.path == "/chocolates":
            response_data = self.chocolate_store.list_chocolates()
            self._send_json_response(200, response_data)
        else:
            self._send_error_response(404, "Ruta no encontrada")

    def do_PUT(self):
        if self.path.startswith("/chocolates/"):
            chocolate_id = int(self.path.split("/")[-1])
            content_length = int(self.headers["Content-Length"])
            put_data = self.rfile.read(content_length)
            data = json.loads(put_data.decode("utf-8"))
            response_data = self.chocolate_store.update_chocolate(chocolate_id, data)
            if response_data:
                self._send_json_response(200, response_data)
            else:
                self._send_error_response(404, "Chocolate no encontrado")
        else:
            self._send_error_response(404, "Ruta no encontrada")

    def do_DELETE(self):
        if self.path.startswith("/chocolates/"):
            chocolate_id = int(self.path.split("/")[-1])
            response_data = self.chocolate_store.delete_chocolate(chocolate_id)
            if response_data:
                self._send_json_response(200, response_data)
            else:
                self._send_error_response(404, "Chocolate no encontrado")
        else:
            self._send_error_response(404, "Ruta no encontrada")

    def _send_json_response(self, status_code, data):
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def _send_error_response(self, status_code, message):
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"error": message}).encode("utf-8"))

def main():
    try:
        server_address = ("", 8000)
        chocolate_store = ChocolateStore()
        httpd = HTTPServer(server_address, lambda *args, **kwargs: ChocolateRequestHandler(*args, chocolate_store=chocolate_store, **kwargs))
        print("Iniciando servidor HTTP en puerto 8000...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        httpd.socket.close()

if __name__ == "__main__":
    main()
