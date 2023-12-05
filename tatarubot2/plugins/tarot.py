"""
塔罗牌
"""

import os
import random
import json
import time

from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.kaiheila import Message, MessageSegment

from tatarubot2.plugins.utils import NoArg, str2img


this_command = "抽卡"
tarot = on_command(this_command, priority=5)


# 当前目录
this_dir = os.path.split(os.path.realpath(__file__))[0]
img_dir = os.path.join(this_dir, "../data/TarotImages")
json_path = os.path.join(img_dir, "ff14_tarot.json")
with open(json_path, "r", encoding="utf-8") as f_r:
    tarot_dict = json.load(f_r)


async def get_tarot(bot: Bot):
    id_now = random.randint(0, 43)
    info_now = tarot_dict["_塔罗牌堆"][id_now]
    text_now = info_now.split("[", 1)[0]
    file_name = info_now.rsplit("/", 1)[-1][:-1]
    file_name = file_name.replace(" ", "_")
    file_path = os.path.join(img_dir, file_name)
    print(file_path)

    with open(file_path, "rb") as f_r:
        img_bytes = f_r.read()

    # txt_bytes = str2img(text_now, width_now=20)

    # msg = Message([MessageSegment.image(txt_bytes),
    #                MessageSegment.image(img_bytes)])
    img_name = str(int(time.time() * 10))
    img_url = await bot.upload_file(img_bytes, img_name)

    # msg = Message([MessageSegment(type="text", data={"content": text_now}),
    #                MessageSegment(type="image", data={"file_key": img_url})])

    # msg = MessageSegment(type="image", data={"file_key": img_url})

    res = [{"type": "section","text": {"type": "kmarkdown", "content": text_now}, },
           {"type": "container","elements": [{"type": "image","src": img_url}]}
          ]
    cards = [{"type": "card", "theme": "info", "size": "lg", "modules": res}]
    msg = MessageSegment.Card(cards)

    await tarot.finish(msg)



@tarot.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State, _=NoArg()):
    await get_tarot(bot)