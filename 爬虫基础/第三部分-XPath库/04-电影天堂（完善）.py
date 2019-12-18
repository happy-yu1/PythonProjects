from lxml import etree
import requests

Header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
Base_Domain = 'https://www.ygdy8.net'


def get_detail_urls(url):
#传入参数为多个电影列表url，该函数获得此电影列表下每个电影的详情页url
    resp = requests.get(url, headers=Header)
    text = resp.text
    html = etree.HTML(text)
    detail_urls = html.xpath('//table[@class="tbspan"]//a/@href')
    # for detail_url in detail_urls:
    #     detail_url = Base_Domain + detail_url  # 得到首页展示电影对应的详情url
    #     print(detail_url)
    detail_urls=map(lambda url:Base_Domain+url,detail_urls)
    return detail_urls


def parse_detail_page(url):
#分析某个电影的详细内容，传入参数为电影详情url，即上个函数得到的结果，作为传入的参数
    movie = {}
    resp = requests.get(url, headers=Header)
    text = resp.content.decode('gbk')
    html = etree.HTML(text)

    title = html.xpath('//div[@class="title_all"]//font[@color="#07519a"]/text()')[0]
    movie['title'] = title

    zoomE = html.xpath('//div[@id="Zoom"]')[0]

    imgs = zoomE.xpath('.//img/@src')
    cover = imgs[0]
    movie['cover'] = cover  # 提取海报图
    screenshot = imgs[1]
    movie['screenshot'] = screenshot  # 提取截图

    infos = zoomE.xpath('.//text()')

    def parse_rule(info, rule):
        return info.replace(rule, '').strip()

    for index, info in enumerate(infos):  # 解释在下面，主演信息那
        if info.startswith('◎年　　代'):
            info = parse_rule(info, '◎年　　代')
            movie['year'] = info  # 提取年份

        elif info.startswith('◎主　　演'):
            actors = []
            info = parse_rule(info, '◎主　　演')  # 提取 杰森·苏戴奇斯 Jason Sudeikis
            actors = [info]

            for x in range(index + 1, len(infos)):
                actor = infos[x].strip()
                if infos[x].startswith('◎'):
                    break
                actors.append(actor)  # 提取其他演员的姓名
            movie['actors'] = actors  # 提取所有演员的名字

        elif info.startswith('◎简　　介'):  # 原理同上
            details = []
            for x in range(index + 1, len(infos)):
                introduction = infos[x].strip()
                if infos[x].startswith(' '):
                    break
                details.append(introduction)
            movie['details'] = details  # 提取电影简介

    return movie

def spider(): #如只爬取两页信息
    base_url='https://www.ygdy8.net/html/gndy/dyzz/list_23_{}.html'
    movies=[]
    for x in range(1,3):  #range（1，n）则爬取n-1页
        url=base_url.format(x)
        detail_urls=get_detail_urls(url)  #获取一页电影列表中每个电影对应的详情url
        for detail_url in detail_urls:
            movie=parse_detail_page(detail_url) #获取某个电影对应的详细信息
            movies.append(movie)
            # print(movie)
    print(movies)
    # for i in movies:
    #     print(i,end='\n')
    # print(len(movies))
if __name__ == '__main__':
    spider()