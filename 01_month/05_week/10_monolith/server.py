from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs

db = {
    1: {
        "title": "Mi primer publication",
        "content": "¡Hola mundo! Esta es mi primer publication en el blog.",
    },
    2: {
        "title": "Otra publication",
        "content": "¡Bienvenidos a mi blog! Aqui hay otra publication.",
    },
}


class BlogService:
    def get_all_posts(self):
        return list(db.values())

    def get_post_by_id(self, post_id):
        return db.get(post_id)

    def create_post(self, title, content):
        new_post_id = max(db.keys()) + 1
        db[new_post_id] = {"title": title, "content": content}
        return new_post_id

    def update_post(self, post_id, title, content):
        if post_id in db:
            db[post_id]["title"] = title
            db[post_id]["content"] = content
            return True
        else:
            return False

    def delete_post(self, post_id):
        if post_id in db:
            del db[post_id]
            return True
        else:
            return False


class BlogHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.blog_service = BlogService()
        super().__init__(*args, **kwargs)

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        if self.path == "/posts":
            self.wfile.write(json.dumps(self.blog_service.get_all_posts()).encode())
        elif self.path.startswith("/post/"):
            post_id = int(self.path.split("/")[-1])
            post = self.blog_service.get_post_by_id(post_id)
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

        title = post_params.get("title", [""])[0]
        content = post_params.get("content", [""])[0]

        new_post_id = self.blog_service.create_post(title, content)

        self.send_response(201)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"id": new_post_id}).encode())

    def do_PUT(self):
        if self.path.startswith("/post/"):
            post_id = int(self.path.split("/")[-1])
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            post_params = parse_qs(post_data.decode())

            title = post_params.get("title", [""])[0]
            content = post_params.get("content", [""])[0]

            if self.blog_service.update_post(post_id, title, content):
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
            if self.blog_service.delete_post(post_id):
                self.send_response(204)
                self.end_headers()
            else:
                self.send_error(404, "Publication no encontrada")
        else:
            self.send_error(404, "Ruta no valid")


def run_server(server_class=HTTPServer, handler_class=BlogHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Iniciando servidor HTTP en puerto {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
