import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "➻ ⏤͟͞ 𝙆𝙄𝙍𝙈𝘼𝘿𝘼⏤͟͞ ┈➤ ⌯ ❰ #𝙇𝙊𝙍𝘿 ❱"])

async def join(client):
    try:
        await client.join_chat("NLTRIDE")
    except BaseException:
        pass
