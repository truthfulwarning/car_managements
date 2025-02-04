from flask import Flask, request, jsonify
import json

app = Flask(__name__)

with open("data.json", "r") as file:
    data = json.load(file)

def save_data():
    with open('data.json', 'w') as file:
        json.dump(data.file,indent=4)

@app.route("/cars", methods=["GET"])
def seeing_cars():
    return jsonify(data["cars"])

@app.route("/cars/<int:car_id>", methods=["GET"])
def seeing_car(car_id):
    car = next((c for c in data["cars"] if c["id"] == car_id), None)
    return jsonify(car) if car else ("Car not found")

@app.route("/addcars", methods=["POST"])
def add_car():
    new_car = request.json
    new_car["id"] = len(data["cars"]) + 1
    data["cars"].append(new_car)
    return jsonify(new_car)

@app.route("/updatecars/<int:car_id>", methods=["PUT"])
def update_car(car_id):
    car = None  # Assume the car is not found

    for c in data["cars"]:  
        if c["id"] == car_id:  
            car = c  
            break
    if not car:
        return ("Car not found")
    car.update(request.json)
    return jsonify(car)

@app.route("/deletecars/<int:car_id>", methods=["DELETE"])
def delete_car(car_id):
    global data
    new_cars = []
        for car in data["cars"]:
            if car["id"] != car_id:
                new_cars.append(car)
    data["cars"] = new_cars
    return jsonify({"message": "Car deleted"})

@app.route("/manufacturers", methods=["GET"])
def get_manufacturers():
    return jsonify(data["manufacturers"])

@app.route("/addmanufacturer", methods=["POST"])
def add_manufacturer():
    new_manufacturer = request.json
    new_manufacturer["id"] = len(data["manufacturers"]) + 1
    data["manufacturers"].append(new_manufacturer)
    return jsonify(new_manufacturer), 201

@app.route("/deletemanufacturer/<int:manufacturer_id>", methods=["DELETE"])
def delete_manufacturer(manufacturer_id):
    global data
    data["manufacturers"] = [m for m in data["manufacturers"] if m["id"] != manufacturer_id]
    return jsonify({"message": "Manufacturer deleted"})

@app.route("/models/<int:manufacturer_id>", methods=["GET"])
def get_models(manufacturer_id):
    models = [m for m in data["models"] if m["manufacturer_id"] == manufacturer_id]
    return jsonify(models)

@app.route("/addmodel", methods=["POST"])
def add_model():
    new_model = request.json
    new_model["id"] = len(data["models"]) + 1
    data["models"].append(new_model)
    return jsonify(new_model), 201


@app.route("/customers", methods=["GET"])
def see_customers():
    return jsonify(data["customers"])

@app.route("/customers/<int:customer_id>", methods=["GET"])
def see_1_customer(customer_id):
    customer = None
    for c in data["customers"]:
        if c["id"] == customer_id:
            customer = c
            break
    
    if customer:
        return jsonify(customer)
    else:
        return jsonify({"error": "Customer not found"})


@app.route("/addcustomers", methods=["POST"])
def add_customer():
    new_customer = request.json
    new_customer["id"] = len(data["customers"]) + 1
    data["customers"].append(new_customer)
    return jsonify(new_customer)

@app.route("/updatecustomers/<int:customer_id>", methods=["PUT"])
def update_customer(customer_id):
    """Updates customer details."""
    for customer in data["customers"]:
        if customer["id"] == customer_id:
            customer.update(request.json)
            return jsonify(customer)

@app.route("/deletecustomers/<int:customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    """Deletes a customer from the database."""
    global data
    data["customers"] = [c for c in data["customers"] if c["id"] != customer_id]
    return jsonify({"message": "Customer deleted"})

@app.route("/placeorder", methods=["POST"])
def place_order():
    new_order = request.json
    new_order["id"] = len(data["orders"]) + 1
    data["orders"].append(new_order)
    return jsonify(new_order), 201

@app.route("/orders/<int:customer_id>", methods=["GET"])
def get_orders(customer_id):
    orders = [o for o in data["orders"] if o["customer_id"] == customer_id]
    return jsonify(orders)


@app.route("/sales", methods=["GET"])
def see_sales():
    """Returns a list of all sales transactions."""
    return jsonify(data["sales"])

@app.route("/sales/<int:sale_id>", methods=["GET"])
def see_sale(sale_id):
    """Returns details of a sale transaction by ID."""
    sale = None
    for s in data["sales"]:
        if s["id"] == sale_id:
            sale = s
            break
    
    if sale:
        return jsonify(sale)
    else:
        return jsonify({"error": "Sale not found"})       
 
@app.route("/addsales", methods=["POST"])
def add_sale():
    new_sale = request.json
    new_sale["id"] = len(data["sales"]) + 1
    data["sales"].append(new_sale)
    return jsonify(new_sale)

@app.route("/updatesales/<int:sale_id>", methods=["PUT"])
def update_sale(sale_id):
    for sale in data["sales"]:
        if sale["id"] == sale_id:
            sale.update(request.json)
            return jsonify(sale)

@app.route("/deletesales/<int:sale_id>", methods=["DELETE"])
def delete_sale(sale_id):
    global data
    data["sales"] = [s for s in data["sales"] if s["id"] != sale_id]
    return jsonify({"message": "Sale deleted"})


if __name__ == "__main__":
    app.run(debug=True)