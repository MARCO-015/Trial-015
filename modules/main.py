import os
import re
import sys
import json
import time
import asyncio
import requests
import subprocess

import core as helper
from utils import progress_bar
from vars import api_id, api_hash, bot_token
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


bot = Client(
    "bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token)


@bot.on_message(filters.command(["start"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text(
       f"𝓦𝓮𝓵𝓬𝓸𝓶𝓮 𝓣𝓸 ❤️\n\n❖ Λ𝗜ᎷᏋᏒ𝗦 ❤️ ❖\n\n❈ I Am A Bot For Download Links From Your **TXT** File.", reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("♛ 𝐉𝐨𝐢𝐧 𝐌𝐀𝐈𝐍 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ♛" ,url=f"https://t.me/+uxqAQJ3wnstkMmQ9") ],
                    [
                    InlineKeyboardButton("★ Λ𝗜ᎷᏋᏒ𝗦 ❤️ ★" ,url="https://t.me/AIMERS_AKATSUKI") ],
                    [
                    InlineKeyboardButton("🐯 𝐅𝐨𝐥𝐥𝐨𝐰 𝐌𝐞 🐯" ,url="https://bio.site/all_aimers") ],                           
                    [
                    InlineKeyboardButton("🐯 𝐅𝐨𝐥𝐥𝐨𝐰 𝐌𝐞 🐯" ,url="https://whatsapp.com/channel/0029Vac9SnM6BIElqk2pMm2q") ]                               
            ]))

@bot.on_message(filters.command("stop"))
async def restart_handler(_, m):
    await m.reply_text("🚦**RUK GYA MALIK**🚦", True)
    os.execl(sys.executable, sys.executable, *sys.argv)



@bot.on_message(filters.command(["aimers"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text('****Please Send TXT file for download**')
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    try:
       with open(x, "r") as f:
           content = f.read()
       content = content.split("\n")
       links = []
       for i in content:
           links.append(i.split("://", 1))
       os.remove(x)
            # print(len(links)
    except:
           await m.reply_text("**𝓜𝓪𝔃𝓪𝓴 𝓶𝓽 𝓚𝓻.**")
           os.remove(x)
           return
    
   
    await editable.edit(f"**Total links found are **{len(links)}**\n\n**Send From where you want 𝐓𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐈𝐧𝐢𝐭𝐚𝐥 𝐢𝐬 ** **1**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("****Send Me Your Batch Name.**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    

    await editable.edit("**𝔼ɴᴛᴇʀ ʀᴇ𝕤ᴏʟᴜᴛɪᴏɴ📸**\n`144` 🍃,`240` 🌱,`360` ☘️,`480` 🌿,`720` 🪴,`1080` 🌲 please choose quality.**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    try:
        if raw_text2 == "144":
            res = "256x144"
        elif raw_text2 == "240":
            res = "426x240"
        elif raw_text2 == "360":
            res = "640x360"
        elif raw_text2 == "480":
            res = "854x480"
        elif raw_text2 == "720":
            res = "1280x720"
        elif raw_text2 == "1080":
            res = "1920x1080" 
        else: 
            res = "UN"
    except Exception:
            res = "UN"
    
    

    await editable.edit("**Enter A Captio to add Otherwise send**   **`Λ𝗜ᎷᏋᏒ𝗦 ❤️`**")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    highlighter  = f"️Λ𝗜ᎷᏋᏒ𝗦 ❤️⁪⁬⁮⁮⁮"
    if raw_text3 == 'Λ𝗜ᎷᏋᏒ𝗦 ❤️':
        MR = highlighter 
    else:
        MR = raw_text3
   
    await editable.edit("Now Send Your **Thumb url**\nEg : https://i.imghippo.com/files/FJAd3614SXE.jpg\n\nOr Send **no**")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    if len(links) == 1:
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(count - 1, len(links)):

            V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","") # .replace("mpd","m3u8")
            url = "https://" + V

            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            if '/master.mpd' in url and not '/drm/' in url:
                id = url.split("/")[-2]
                pwtoken = os.getenv('pwtoken')
                url = f'https://madxapi-d0cbf6ac738c.herokuapp.com/{id}/master.m3u8?token={pwtoken}'
                print(url)

            elif 'classplusapp' in url:
                  headers = {
                      'Host': 'api.classplusapp.com',
                      'x-access-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjMyODI4IiwiZW1haWwiOiJuYXZlZG1vaGFtbWFkMDUzQGdtYWlsLmNvbSIsInRpbWVzdGFtcCI6MTczMjU5Njg5N30.3MJZbdJwKMx2X5DfeG8MD83LvOccQ6fUd5Y_gl4kqgk',
                      'user-agent': 'Mobile-Android',
                      'app-version': '1.4.37.1',
                      'api-version': '18',
                      'device-id': '5d0d17ac8b3c9f51',
                      'device-details':'2848b866799971ca_2848b8667a33216c_SDK-30',
                      'accept-encoding': 'gzip, deflate' }
                
                  params = (('url', f'{url}'), )
                  response = requests.get('https://api.classplusapp.com/cams/uploader/video/jw-signed-url', headers=headers, params=params)                
                  url = response.json()['url']

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}) {name1[:60]}'

            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"

            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:  
                
                cc =  f'[🎥]**Vid_id  »** {str(count).zfill(3)}**\n**Tɪᴛᴛʟᴇ  »** {name1} {res} Λ𝗜ᎷᏋᏒ𝗦 ❤️.mkv\nBᴀᴛᴄʜ Nᴀᴍᴇ » **{raw_text0}**\n\n**𝐄𝐱𝐭𝐫𝐚𝐜𝐭𝐞𝐝 𝐁𝐲 ➤ {MR}**\n\n'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                cc1 = f'[📕]**Pdf_id  »** {str(count).zfill(3)}** {name1} Λ𝗜ᎷᏋᏒ𝗦 ❤️.pdf \nBᴀᴛᴄʜ Nᴀᴍᴇ »**{raw_text0}**\n\n**𝐄𝐱𝐭𝐫𝐚𝐜𝐭𝐞𝐝 𝐁𝐲 ➤ {MR}**\n\n'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)
                        count+=1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                
                elif ".pdf" in url:
                    try:
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                        count += 1
                        os.remove(f'{name}.pdf')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    Show = f"**⥥ 📥 ＤＯＷＮＬＯＤＩＮＧ 📥 :-**\n\n**📝Name »** `{name}\n❄𝐐𝐮𝐚𝐥𝐢𝐭𝐲 » {raw_text2}`\n\n**Url :-** `Kya karega URL dekhke ☠️☠️`\n\n **Bot made by 👉 Λ𝗜ᎷᏋᏒ𝗦 ❤️"
                    prog = await m.reply_text(Show)
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(
                    f"**downloading failed 🔰『 Λ𝗜ᎷᏋᏒ𝗦 ❤️ 』🔰**\n{str(e)}\n**Name** - {name}\n**Link** - {url}"
                )
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("**DONE BRO 😁\n\nBY- Λ𝗜ᎷᏋᏒ𝗦 ❤️**")


bot.run()
