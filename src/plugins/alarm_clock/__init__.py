from aiocqhttp.exceptions import Error as CQHttpError
import random

import httpx
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/94.0.4606.71 Safari/537.36',
    'Host': 'www.vilipix.com'
}
params = {
    'mode': 'daily'
}
res = httpx.get('https://www.vilipix.com/ranking', params=params, headers=headers)
res.encoding = 'utf-8'
origin_html = etree.HTML(res.text)
try:
    # ranking_page = origin_html.xpath('//ul[@class="illust-content"]/li/div[@class="illust"]/a/@href')[
    #     random.randint(1, 30)]
    ranking_page = origin_html.xpath('//ul[@class="illust-content"]/li/div[@class="illust"]/a/@href')[0]
    build_illust_url = 'https://www.vilipix.com' + ranking_page
    res2 = httpx.get(build_illust_url, params=params, headers=headers)
    origin_html2 = etree.HTML(res2.text)
    illust = origin_html2.xpath('//ul[@class="illust-pages"]/li/a/img/@src')[0]
    print(illust)
except Exception as e:
    print(e)
