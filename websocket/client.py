import asyncio
import websockets

async def receive_stock_updates():
    async with websockets.connect("ws://localhost:8765") as websocket:
        while True:
            data = await websocket.recv()
            print(f"Received Stock Prices: {data}")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(receive_stock_updates())
