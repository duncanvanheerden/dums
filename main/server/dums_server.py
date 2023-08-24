import asyncio
import websockets

async def handle_client(websocket, path):
    async for message in websocket:
        response_message = f"You sent: {message}"
        await websocket.send(response_message)

start_server = websockets.serve(handle_client, "127.0.0.1", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
