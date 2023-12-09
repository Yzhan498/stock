import asyncio
import websockets
import random
import json

# Mock stock data for demonstration
stocks = {
    'AAPL': 150.0,
    'AC': 20.0,
    'TSLA': 750.0
}

async def stock_price_updates(websocket, path):
    while True:
        # Simulate stock price changes (you should replace this with real data)
        for symbol in stocks:
            stocks[symbol] += random.uniform(-5.0, 5.0)
        
        # Send updated stock prices to connected clients
        await websocket.send(json.dumps(stocks))
        await asyncio.sleep(1)  # Update every second

start_server = websockets.serve(stock_price_updates, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
