from simpletransformers.seq2seq import Seq2SeqModel
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import cgi

model = None

class Server(BaseHTTPRequestHandler):
    def _set_headers(self, type_response):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', "*")
        self.send_header('Access-Control-Allow-Methods', "POST, GET, OPTIONS, PUT, DELETE")
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Allow-Headers", "Origin")
        self.send_header('Content-type', type_response)
        self.end_headers

    def do_HEAD(self):
        self._set_headers(type_response='application/json')

    
    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin', "*")
        self.send_header('Access-Control-Allow-Methods', "POST, GET, OPTIONS, PUT, DELETE")
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Allow-Headers", "Origin")
        self.end_headers()

    def do_POST(self):
        global model

        ctype, pdict = cgi.parse_header(self.headers.get('content-type'))

        if ctype!='application/json':
            self.send_response(400)
            self.end_headers()
            return

        length=int(self.headers.get('content-length'))
        message = json.loads(self.rfile.read(length))

        summarized = model.predict([message['base_text']])[0]

        response = {}
        response['summary'] = summarized

        self._set_headers(type_response = 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())


def init_model():
    global model
    model = Seq2SeqModel(
        encoder_decoder_type='bart',
        encoder_decoder_name='downFolder/content/outputs/best_model'
    )


def run(server_class=HTTPServer, handler_class=Server, port=8000):
    server_address=('',port)
    httpd=server_class(server_address, handler_class)

    print(f'Starting server on port {port}')
    httpd.serve_forever()

if __name__=='__main__':
    init_model()
    run()
