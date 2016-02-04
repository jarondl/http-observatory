from flask import Flask

from website import add_response_headers
from website.backend import api

app = Flask('http-observatory')


@app.route('/')
@add_response_headers()
def main() -> str:
    return 'Welcome to the HTTP Observatory backend service!'

if __name__ == '__main__':
    app.register_blueprint(api)
    app.run(debug=True)
