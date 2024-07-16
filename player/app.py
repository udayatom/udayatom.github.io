import mimetypes

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__, static_folder="web/static", template_folder="web/templates")
CORS(app, origins=['http://0.0.0.0:5055/webhook', 'http://127.0.0.1:5055/webhook', 'http://localhost:5055/webhook',
                   'http://localhost:5005/webhooks/rest/webhook'])
"""
# Decorator to add CORS headers to the response
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

# Apply the decorator to all routes
@app.after_request
def after_request(response):
    return add_cors_headers(response)
"""


@app.route('/', methods=['GET', 'POST'])
def hello():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(ssl_context=("cert.pem", "key.pem"), debug=True, port=5002)
