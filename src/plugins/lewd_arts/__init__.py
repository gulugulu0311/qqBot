from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
from nonebot.permission import *
from aiocqhttp.exceptions import Error as CQHttpError
import random
from .data_source import illust_src_list, illust_get_id
import re

foo = on_keyword({'art'})
base_url = 'https://www.vilipix.com/ranking'


@foo.handle()
async def download(bot: Bot, event: Event, state: T_State):
    random_num = random.randint(0, 29)
    illusts = await illust_src_list(random_num)
    info = await illust_get_id(random_num)
    try:
        for item in illusts:
            item = re.sub('\\?x-oss-process=image/resize,m_fill,w_1000', '', item)
            await foo.send(message=Message(f'[CQ:image,file={item}]'))
        await foo.send(message=Message(info))
    except CQHttpError:
        pass
