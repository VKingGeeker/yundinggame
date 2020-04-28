# coding=utf-8
import urllib
from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request

#抓取百度搜索页右侧top话题
class MyHtmlParser(HTMLParser):
    def __init__(self):
        super(MyHtmlParser,self).__init__()
        self.mark = ''
        self.href = ''
        self.hot = ''
    def handle_starttag(self, tag, attrs):
        # print(attrs)
        if tag == 'span' and ('c-index  c-index-hot' in str(attrs) or 'c-index  c-gap-icon-right-small' in str(attrs)):
            self.mark = '1'
        elif tag == 'a' and ('target','_blank') in attrs and len(attrs)==3 and 'title' in attrs[1]:
            self.mark = '2'
            self.href = 'https://www.baidu.com'+attrs[2][1]
        elif tag == 'td' and ('class','opr-toplist1-right') in attrs:
            self.mark = '3'

    def handle_startendtag(self, tag, attrs):
        pass
    def handle_endtag(self, tag):
        self.mark = ''

    def handle_charref(self, name):
        pass

    def handle_entityref(self, name):
        pass

    def handle_data(self, data):
        if self.mark == '1':
            print('排名:' + data)
        elif self.mark == '2':
            print('标题:'+data)
            print('链接:' + self.href)
        elif self.mark == '3':
            print('热度:'+data)
            print('--------------------')

    def handle_comment(self, data):
        pass
parser = MyHtmlParser()
headers = {
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
}
req=request.Request('https://www.baidu.com/s?wd=%E8%AE%B8%E9%AD%8F%E6%B4%B2%E6%9D%8E%E7%8E%89%E6%89%93%E5%81%87&rsv_idx=2&tn=baiduhome_pg&usm=1&ie=utf-8&rsv_cq=python%E7%88%AC%E5%8F%96%E7%99%BE%E5%BA%A6&rsv_dl=0_right_fyb_pchot_20811_01&rsf=4df2dd5cfddedc573d5f9818b6a291e9_1_15_1&rqid=ba6ca8900001c36c')
req.add_header('User-Agent',
               'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36')

with urllib.request.urlopen(req) as f:
    data = f.read()
parser.feed(data.decode('utf-8'))

