"""Small HTTP application for DevOps deployment practice."""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


def health_payload():
    return {"status": "healthy", "service": "devops-practice"}


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            body = json.dumps(health_payload()).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        body = b"Hello from your DevOps practice application!\n"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format_string, *args):
        print("%s - %s" % (self.address_string(), format_string % args))


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), RequestHandler)
    print("Server listening on port 8080")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server")
    finally:
        server.server_close()
