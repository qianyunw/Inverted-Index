# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 14:08:41 2016

@author: wangrongyu
"""

import re
import requests
import urllib
from bs4 import BeautifulSoup

Url = ['http://www.sds.bnu.edu.cn/']
Str = ['']


def solve():
    i = 0
    while i < len(Url):
        
        
        try:
            # 用try就可以避免发生异常程序就中断了
            r = requests.get(Url[i])
            data = r.text
            # TODO: 这里用BeautifulSoup什么东东处理data，我这里没装这个库就略了

            url_list = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", data)
            for u in url_list:
                if u[:4] != 'http':
                    u = Url[0] + u
                    if u not in Url and 'image' not in u and '@' not in u and requests.get(u).status_code == 200:
                        Url.append(u)
                elif 'sds.bnu.edu.cn' in u:
                    if u not in Url and 'image' not in u and '@' not in u and requests.get(u).status_code == 200 :
                        Url.append(u)
            req = urllib.request.urlopen(Url[i])
            the_page = req.read()
        
            req.close()
            soup = BeautifulSoup(the_page)
            if i==0:
                Str[i]=soup.get_text(strip=True)
            else:
                Str.append(soup.get_text(strip=True))
           
            i += 1
        except Exception as e:
            print(e)

if __name__ == '__main__':
    solve()
