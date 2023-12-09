from flask import Flask, request, jsonify
from ariadne import QueryType, ObjectType, make_executable_schema
from graphql import graphql_sync

app = Flask(__name__)

# Sample data storage (in-memory)
stocks = [
    {
        'name': 'Algonquin Company',
        'ticker': 'AC',
        'current price': 10.00,
        'historical_prices': [8.50, 10.20, 9.75],
        'highest_price': 10.20,
        'lowest_price': 8.50,
        'trading_volume': 50000,
    },
    # Add more sample stocks here
]

# Define GraphQL types and queries
query = QueryType()
stock_type = ObjectType("Stock")

@query.field("stocks")
def resolve_stocks(_, info):
    return stocks

@stock_type.field("historicalPrices")
def resolve_historical_prices(stock, _):
    return stock.get("historical_prices", [])

@stock_type.field("highestPrice")
def resolve_highest_price(stock, _):
    return stock.get("highest_price")

@stock_type.field("lowestPrice")
def resolve_lowest_price(stock, _):
    return stock.get("lowest_price")

@stock_type.field("tradingVolume")
def resolve_trading_volume(stock, _):
    return stock.get("trading_volume")
type_defs = """
    type Stock {
        name: String
        ticker: String
        price: Float
        historicalPrices: [Float]
        highestPrice: Float
        lowestPrice: Float
        tradingVolume: Int
    }

    type Query {
        stocks: [Stock]
    }

    schema {
        query: Query
    }
"""
# Create an executable GraphQL schema
schema = make_executable_schema(type_defs, query, stock_type)


# Define a route to serve the GraphQL Playground (for testing)
@app.route("/graphql", methods=["GET"])
def graphql_playground():
    # You can provide a link to the Playground URL or custom instructions here
    return "Visit http://localhost:5000/graphql in your browser to access the GraphQL Playground for testing.", 200

# Define a route to handle GraphQL queries
@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(schema, data, context_value=request)
    status_code = 200 if success else 400
    return jsonify(result), status_code

if __name__ == "__main__":
    app.run(debug=True)
