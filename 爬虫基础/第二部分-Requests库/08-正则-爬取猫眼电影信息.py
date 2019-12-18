import json,requests,re,time
from requests.exceptions import RequestException

def get_one_page(url):
    try:
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
        resp = requests.get(url, headers=header)
        return resp.text
    except RequestException:
        return None
def parse_one_page(html):
    reg=re.compile('')
    result=re.findall(reg,html)
    for i in result:
        yield{'index':i[0],'image':i[1]}
