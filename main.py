import pygetwindow
import pyautogui
from PIL import Image
import cv2
from pytesseract import pytesseract
import asyncio
import discord
import time
import schedule
from pytz import timezone
from datetime import datetime

path = 'C:\\Users\\dongwankim\\Desktop\\test.png'
path_to_tesseract = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
pytesseract.tesseract_cmd = path_to_tesseract
custom_config = ('-l kor --oem 3 --psm 3')


def get_window_titles():
    titles = pygetwindow.getAllTitles()
    return titles

def get_window():
    window = pygetwindow.getWindowsWithTitle('LDPlayer-1')[0]
    return window

def save_screenshot():
    window = get_window()
    left, top = window.topleft
    right, bottom = window.bottomright

    pyautogui.screenshot(path)
    im = Image.open(path)
    im = im.crop((left+100, top+300, right-1000, bottom-115))
    im.save(path)


def convert_to_gray():    
    img_gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    return img_gray


def extract_text():
  save_screenshot()
  convert_to_gray()
  results = pytesseract.image_to_string(convert_to_gray(), lang='kor', config=custom_config)
  results = results.replace('\n', ' ')
  results = results.replace(' ', '').replace('다', '다.').split('.')
  return results



intents = discord.Intents.default()

intents.members = True  

client = discord.Client(intents=intents)
TOKEN = 'MTA3NjQyNDU4NDc4MzQ2NjQ5Ng.G2dCtm.bvVrzZGO6YhZv_hUbvYWRoOPkT4nczKb06ehjY' # 디코 봇 고유 토큰
CHANNEL_ID = 1076508219314274404 # 채팅방 id

async def send_message(msg):
    channel = client.get_channel(CHANNEL_ID)
    if channel is None:
        print(f"채널을 찾지 못했습니다. 채널 ID를 확인해주세요. ({CHANNEL_ID})")
        return
    await channel.send(f"@everyone {msg}", tts=True)



async def check_status():
    while True:
      for x in extract_text():
          if '출현' in x:
            await send_message(x + ":::: 출현 시각 ::::" + datetime.now(timezone('Asia/Seoul')).strftime('%H:%M:%S'))

      await asyncio.sleep(10)              
             

@client.event
async def on_ready():
    print(f'{client.user}로 로그인하였습니다!')
    await check_status()

client.run(TOKEN)







