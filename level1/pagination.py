from flask import Flask,jsonify,request

app =Flask(__name__)

@app.route('/items',methods=["GET"])
def list_items():
   page = request.args.get("page",1,type=int)
   page_size = request.args.get("page_size",20,type=int)

   items = [
       {"id":1,"name" : "Item 1"},
       {"id": 2,"name": "Item 2"},
   ]
   return jsonify({
       "items" : items,
       "page" : page,
       "total" : len(items),
   })




if __name__ == "__main__":
    app.run(debug=True)
