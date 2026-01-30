from flask import Flask,jsonify,request

app =Flask(__name__)

@app.route('/calculate',methods=["POST"])
def calculate():
    data = request.get_json()
    #{"operation": "add", "x": 10, "y": 5}
    if not data or 'operation' not in data:
        return jsonify({
            "error" : "Missing Operation"
        }),400
    
    operation = data['operation']
    x = data.get('x',0)
    y = data.get('x',0)

    if operation == 'add':
        result = x + y
    elif operation == 'substract':
        result = x - y
    elif operation == 'multiply':
        result = x * y
    elif operation == 'divide':
        if y == 0 :
            return jsonify({
                "error" : "Cannot divide by zero"
            }),400
        result = x/y
    else:
        return jsonify({
            "error" : "Invalid Operation"
        }),400
    
    return jsonify({
        "result":result
    }),200

@app.route("/search",methods=['GET'])
def search():
    query = request.args.get("q")
    print(query)
    if not query:
        return jsonify({
            "error" : "no query paramter to show"
        })
    return jsonify({
            "query" : query
        }),200


if __name__ == "__main__":
    app.run(debug=True)
