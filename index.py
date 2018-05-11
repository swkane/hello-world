from wsgiref.simple_server import make_server

port = 3000
hostname = "0.0.0.0"

def simple_app(environ, start_response):
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    start_response(status, headers)

    return "Hello World\n"

if __name__ == "__main__":
    server = make_server(hostname, port, simple_app)
    print("Server is running at http://{}:{}".format(hostname, port))
    server.serve_forever()