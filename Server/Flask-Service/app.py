from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World! Docker Template Backend Flask Service is running!'


@app.route('/data')
def get_data():
    """
    return a json object
    """
    return {"backend_data": "some example data from backend"}


if __name__ == '__main__':
    # In the frontend side we have created a proxy to this port 5000
    app.run("0.0.0.0", 5000)
