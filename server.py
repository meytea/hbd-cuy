from http.server import HTTPServer, SimpleHTTPRequestHandler

class MyHTTPRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="html", **kwargs)

def run_server():
    server_address = ('', 4000)
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
    print('Server Online!! 4000...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
