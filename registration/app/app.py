from flask import Flask, render_template,jsonify,request,session

app = Flask(__name__,template_folder='templates')



messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]

@app.route("/",methods=['POST'])
def index():
    json_data = request.form['first']
    print(json_data)

    return jsonify({
        "hello" : json_data
    })

if __name__ == "__main__":
    app.run(debug=True)
