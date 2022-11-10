from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
@cross_origin()
def hello_world():
    return 'Hello, World! Docker Template Backend Flask Service is running!'


@app.route('/data')
@cross_origin()
def get_data():
    """
    return a json object
    """
    return {"backend_data": "some example data from backend"}


if __name__ == '__main__':
    # In the frontend side we have created a proxy to this port 5000
    app.run(host='0.0.0.0', debug=True)
