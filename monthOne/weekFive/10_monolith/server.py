from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs

db = {
    1: {
        "title": "Mi primer publication",
        "content": "¡Hello word! Esta es mi primer publication en el blog.",
    },
    2: {
        "title": "Otra publication",
        "content": "¡Bienvenidos a mi blog! Aqui hay otra publication.",
    },
}


class BlogHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.wfile.write(json.dumps(response).encode('utf-8'))
        self.end_headers()

        if self.path == "/posts":
            self.wfile.write(json.dumps(list(db.values())).encode())
        elif self.path.startswith("/post/"):
            post_id = int(self.path.split("/")[-1])
            post = db.get(post_id)
            if post:
                self.wfile.write(json.dumps(post).encode())
            else:
                self.send_error(404, "Publication no encontrada")
        else:
            self.send_error(404, "Ruta no valid")

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        post_params = parse_qs(post_data.decode())

        if self.path == "/posts":
            title = post_params.get("title", [""])[0]
            content = post_params.get("content", [""])[0]
            new_post_id = max(db.keys()) + 1
            db[new_post_id] = {"title": title, "content": content}
            self.send_response(201)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"id": new_post_id}).encode())
        else:
            self.send_error(404, "Ruta no valid")

    def do_PUT(self):
        if self.path.startswith("/post/"):
            post_id = int(self.path.split("/")[-1])
            if post_id in db:
                content_length = int(self.headers["Content-Length"])
                post_data = self.rfile.read(content_length)
                post_params = parse_qs(post_data.decode())
                db[post_id]["title"] = post_params.get("title", [db[post_id]["title"]])[
                    0
                ]
                db[post_id]["content"] = post_params.get(
                    "content", [db[post_id]["content"]]
                )[0]
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"id": post_id}).encode())
            else:
                self.send_error(404, "Publication no encontrada")
        else:
            self.send_error(404, "Ruta no valid")

    def do_DELETE(self):
        if self.path.startswith("/post/"):
            post_id = int(self.path.split("/")[-1])
            if post_id in db:
                del db[post_id]
                self.send_response(204)
                self.end_headers()
            else:
                self.send_error(404, "Publication no encontrada")
        else:
            self.send_error(404, "Ruta no valid")


def run_server(server_class=HTTPServer, handler_class=BlogHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()