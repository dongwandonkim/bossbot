
import asyncio

import discord

intents = discord.Intents.default()
intents.members = True  

client = discord.Client(intents=intents)
TOKEN = 'MTA3NjQyNDU4NDc4MzQ2NjQ5Ng.G2dCtm.bvVrzZGO6YhZv_hUbvYWRoOPkT4nczKb06ehjY' # 디코 봇 고유 토큰
CHANNEL_ID = 1076508219314274404 # 채팅방 id

previous_clipboard = None

async def send_message(msg):
    channel = client.get_channel(CHANNEL_ID)
    if channel is None:
        print(f"채널을 찾지 못했습니다. 채널 ID를 확인해주세요. ({CHANNEL_ID})")
        return
    await channel.send(f"@everyone {msg}")



@client.event
async def on_ready():
    global previous_clipboard
    print(f'{client.user}로 로그인하였습니다!')


client.run(TOKEN)