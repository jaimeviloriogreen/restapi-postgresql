from flask import Flask, jsonify, request, render_template
from modules.data import getAllData, getOneData, deleteData, insertData

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

#! Show all products
@app.route("/products")
def getProducts():  
    datas = getAllData(["name", "price", "qty"], "products")
    result = [{"name":data[0], "price": float(data[1]), "qty": int(data[2])} for data in datas]

    return jsonify(result)

#! Show one product
@app.route("/product")
@app.route("/product/<string:name>")
def getProduct(name = None):
    if name:
        data = getOneData(["name", "price", "qty"], "products", name)
        result = [{"name":data[0], "price":float(data[1]), "qty":int(data[2])}] if data else {"Error: ":"Product not found!"}
        return jsonify(result)
    else:
        return jsonify({"Error: ": "No product name added!"})
    
#! Delete one product
@app.route("/product", methods=["DELETE"])
@app.route("/product/<string:name>", methods=["DELETE"])
def deleteProduct(name = None):
    if name:
        data = deleteData("products", name)
        return jsonify({"Result":f"{data} value(s) has been deleted!" if data >= 1 else "Nothing have been deleted!"})
    else:
        return jsonify({"Error: ": "No product name added!"})

# ! Insert Products
@app.route("/product", methods=["POST"])
def insertProduct():
    name = request.json['name']
    price = request.json['price']
    qty = request.json['qty']
    result = insertData("products", name, price, qty);
    return {"Message: ": f"{result} product added!!", "product": request.json};

# ! Handle Error 404
@app.errorhandler(404)
def page_not_found(error):
    return {"Error: ": "Page not found!"}

if __name__ == "__main__":
    app.run(debug=True)
        
