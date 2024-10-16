#!/usr/bin/env python

import asyncio
import time

from websockets.asyncio.client import connect

async def hello():
    uri = "ws://192.168.4.1:80/ws"

    nb = 0

    start_time = time.time()
    async with connect(uri) as websocket:
        while(True):
            msg_trunk = "PINGTEST"
            print("{:.3f} WS send:".format(time.time()-start_time), msg_trunk);
            await websocket.send(msg_trunk)

            ret = await websocket.recv()
            print("{:.3f} WS received".format(time.time() - start_time), ret)
            nb += 1
            print("nb:", nb)
            time.sleep(0.5)


if __name__ == "__main__":
    asyncio.run(hello())
