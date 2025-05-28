from telethon import TelegramClient, events

# Get these from my.telegram.org
api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'

# Create the client
client = TelegramClient('session_name', api_id, api_hash)

# Set of replied message IDs to avoid repeated replies
replied_ids = set()

@client.on(events.NewMessage)
async def handler(event):
    if event.is_private and event.id not in replied_ids:
        await event.reply("Hello! This is an automated response.")
        replied_ids.add(event.id)

client.start()
print("Userbot is running...")
client.run_until_disconnected()
