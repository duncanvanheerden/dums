import asyncio
import websockets

async def send_and_receive():
    async with websockets.connect("ws://127.0.0.1:8000") as websocket:
        while True:
            message = input("Enter a message to send to the server (type 'exit' to quit): ")
            if message.lower() == 'exit':
                break
            
            await websocket.send(message)
            response = await websocket.recv()
            print("Server Response:", response)

asyncio.get_event_loop().run_until_complete(send_and_receive())
