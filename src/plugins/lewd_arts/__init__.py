from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
from nonebot.permission import *
from aiocqhttp.exceptions import Error as CQHttpError
import re
import httpx

anime = on_keyword({'lewd'})


@anime.handle()
async def downloads(bot: Bot, event: Event, state: T_State):
    msg = await downloads_page()
    try:
        await anime.send(message=Message(msg))

    except CQHttpError:
        pass


async def downloads_page():
    url = "https://api.lolicon.app/setu/"
    da = httpx.get(url).text
    ur = re.findall(r'url":"(.+?)"}]}', da)
    st = ur[0]
    tu = f'[CQ:image,file={st}]'
    return tu
