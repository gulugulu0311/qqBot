import httpx
import random
from lxml import etree
import re

base_url = 'https://www.vilipix.com/ranking'


def get_html(page_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/94.0.4606.71 Safari/537.36',
        'Host': 'www.vilipix.com'
    }
    params = {
        'mode': 'daily'
    }
    res = httpx.get(page_url, params=params, headers=headers)
    res.encoding = 'utf-8'
    return etree.HTML(res.text)


async def illust_src_list(random_num):
    origin_html = get_html(base_url)
    try:
        # ranking_page = origin_html.xpath('//ul[@class="illust-content"]/li/div[@class="illust"]/a/@href')[
        #     random.randint(1, 30)]
        ranking_page = origin_html.xpath('//ul[@class="illust-content"]/li/div[@class="illust"]/a/@href')[random_num]
        build_illust_url = 'https://www.vilipix.com' + ranking_page
        illusts = get_html(build_illust_url).xpath('//ul[@class="illust-pages"]/li/a/img/@src')
        # baz = re.sub('\\?x-oss-process=image/resize,m_fill,w_1000', '', illusts[0])
        return illusts
    except Exception as e:
        print(e, '...')


async def illust_get_id(random_num):
    origin_html = get_html(base_url)
    try:
        ranking_page = origin_html.xpath('//ul[@class="illust-content"]/li/div[@class="illust"]/a/@href')[random_num]
        build_illust_url = 'https://www.vilipix.com' + ranking_page
        name = get_html(build_illust_url).xpath('//div[@class="info"]/h2/a/text()')[0]
        id = get_html(build_illust_url).xpath('//div[@class="info"]/p/text()')[0]
        return name + ' ' + id
    except Exception as e:
        print(e)


if __name__ == '__main__':
    random_num = random.randint(0, 29)
    print(illust_src_list(random_num))
