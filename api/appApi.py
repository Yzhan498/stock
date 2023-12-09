from flask import Flask, request, jsonify

app = Flask(__name__)

# Temporary data store for stocks (in-memory storage).
stocks = []

@app.route('/stocks', methods=['GET'])
def get_stocks():
    return jsonify(stocks)

@app.route('/stocks', methods=['POST'])
def add_stock():
    data = request.get_json()
    new_stock = {
        'name': data['name'],
        'ticker_symbol': data['ticker_symbol'],
        'current_price': data['current_price']
    }
    stocks.append(new_stock)
    return jsonify(new_stock), 201
if __name__ == '__main__':
    app.run(debug=True)