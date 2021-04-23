import threading
from datetime import datetime
from wsgiref.simple_server import make_server

from flask import Flask

from observer import get_full_version

app = Flask(__name__)


@app.route('/about')
def about():
    return {'ok': 'ok'}


@app.route('/version')
def version():
    return {'version': get_full_version(), 'ts': int(datetime.now().timestamp())}


@app.route('/health')
def health():
    return {'status': 'OK'}


def init_httpd():
    httpd = make_server('0.0.0.0', 80, app)
    httpd_thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    httpd_thread.start()
