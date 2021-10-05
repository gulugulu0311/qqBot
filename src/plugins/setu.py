from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests
from nonebot.permission import *
from aiocqhttp.exceptions import Error as CQHttpError
import re

anime = on_keyword({'涩图'})


@anime.handle()
async def downloads(bot: Bot, event: Event, state: T_State):
    msg = await downloads_page()  # url
    try:
        await anime.send(message=Message(msg))
    except CQHttpError:
        pass


async def downloads_page():
    url = "https://api.lolicon.app/setu/"
    da = requests.get(url).text
    ur = re.findall(r'url":"(.+?)"}]}', da)
    # setu=requests.get(ur).text
    st = ur[0]
    # st = requests.get(str).text
    tu = f'[CQ:image,file={st}]'
    print(tu)
    return tu
