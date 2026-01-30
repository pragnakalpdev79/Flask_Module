from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route("/ping",methods=['GET'])
def pong():
    return jsonify({
        "pong" : True
    })


if __name__ == '__main__':
    app.run(debug=True)


