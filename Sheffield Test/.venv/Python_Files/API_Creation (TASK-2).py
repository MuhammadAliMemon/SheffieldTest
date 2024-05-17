from flask import Flask, jsonify, abort
import pandas as pd

app = Flask(__name__)

customers = pd.read_csv('../CSV_Files/customers.csv')
orders = pd.read_csv('../CSV_Files/orders.csv')


@app.route("/customers")
def customers_to_json1():
    return jsonify(customers.to_dict(orient='records'))


@app.route("/customers/<int:customer_id>")
def customers_to_json2(customer_id):
    customer = customers[customers["customer_id"] == customer_id].to_dict(orient='records')
    if not customer:
        abort(404)
    return jsonify(customer)


@app.route("/orders")
def get_orders():
    return jsonify(orders.to_dict(orient='records'))


if __name__ == '__main__':
    app.run(debug=True)
