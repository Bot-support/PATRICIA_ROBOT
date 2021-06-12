from ShasaBot.events import register

from ShasaBot import OWNER_ID

from ShasaBot import telethn as tbot

import os 

from PIL import Image, ImageDraw, ImageFont

import random

@register(pattern="^/logo ?(.*)")

async def lego(event):

 quew = event.pattern_match.group(1)

 if event.sender_id == OWNER_ID:

     pass

 else:

     

    if not quew:

       await event.reply('Provide Some Text To Draw!')

       return

    else:

       pass

 await event.reply('Creating your logo...wait!')

 try:

    text = event.pattern_match.group(1)

    img = Image.open('./ShasaBot/resources/blackbg.jpg')

    draw = ImageDraw.Draw(img)

    image_widthz, image_heightz = img.size

    pointsize = 500

    fillcolor = "gold"

    shadowcolor = "blue"

    font = ImageFont.truetype("./ShasaBot/resources/Chopsic.otf", 330)

    w, h = draw.textsize(text, font=font)

    h += int(h*0.21)

    image_width, image_height = img.size

    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))

    x = (image_widthz-w)/2

    y= ((image_heightz-h)/2+6)

    draw.text((x, y), text, font=font, fill="black", stroke_width=25, stroke_fill="yellow")

    fname2 = "LogoByPatricia.png"

    img.save(fname2, "png")

    await tbot.send_file(event.chat_id, fname2, caption="Made By Savage")

    if os.path.exists(fname2):

            os.remove(fname2)

 except Exception as e:

   await event.reply(f'Error Report @Savage_management_bot, {e}')

   

@register(pattern="^/wlogo ?(.*)")

async def lego(event):

 quew = event.pattern_match.group(1)

 if event.sender_id == OWNER_ID:

     pass

 else:

     

    if not quew:

       await event.reply('Provide Some Text To Draw!')

       return

    else:

       pass

 await event.reply('Creating your logo...wait!')

 try:

    text = event.pattern_match.group(1)

    img = Image.open('./ShasaBot/resources/blackbg.jpg')

    draw = ImageDraw.Draw(img)

    image_widthz, image_heightz = img.size

    pointsize = 500

    fillcolor = "white"

    shadowcolor = "blue"

    font = ImageFont.truetype("./ShasaBot/resources/Maghrib.ttf", 1000)

    w, h = draw.textsize(text, font=font)

    h += int(h*0.21)

    image_width, image_height = img.size

    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))

    x = (image_widthz-w)/2

    y= ((image_heightz-h)/2+6)

    draw.text((x, y), text, font=font, fill="white", stroke_width=0, stroke_fill="white")

    fname2 = "LogoByPatricia.png"

    img.save(fname2, "png")

    await tbot.send_file(event.chat_id, fname2, caption="Made By ShasaBot")

    if os.path.exists(fname2):

            os.remove(fname2)

 except Exception as e:

   await event.reply(f'Error Report @Savage_userbot, {e}')







   

file_help = os.path.basename(__file__)

file_help = file_help.replace(".py", "")

file_helpo = file_help.replace("_", " ")

__mod_name__ = "Logo"

