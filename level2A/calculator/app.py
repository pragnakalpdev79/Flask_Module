from flask import Flask,request,jsonify
from services.calculation_service import CalculationService

app = Flask(__name__)

@app.route("/calculate",methods=["POST"])
def calculate():
    data = request.get_json()

    if not data:
        return jsonify({
            "Error" :  "Request Body Required"
        }),400
    
    operation = data.get("operation")
    x = data.get("x")
    y = data.get("y")

    if not all([operation x is not None,y is not None]):
        return jsonify({
            "Error" : "Missing Operation, x or y "
        }),400
    
    try:
        result = CalculationService.calculate(operation,x,y)
        return jsonify({
            "Result" : result
        }),200
    except ValueError as e:
        return jsonify({
            "Error" : str(e)
        }),400
    
