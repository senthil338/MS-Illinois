from flask import Flask, request
app = Flask(__name__)

val="0"
@app.route('/',methods=["GET"])
def get_value():
    return str(val)

@app.route('/', methods=["POST"])
def post_value():
    global val
    req = request.get_json()
    val = req["num"]
    return str(val)

'''
@app.route('/', methods=["POST"])
def json_example():
    return "wecome"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
'''