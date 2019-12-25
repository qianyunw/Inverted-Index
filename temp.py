# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 14:59:11 2016

@author: guolei
"""
import re
import requests
import urllib
from bs4 import BeautifulSoup
import jieba

class Node(object): #节点结构体
    def __init__(self, val,wh,p=0):
        self.data = val #val为string类型
        self.webhead = wh
        self.next = p

class LinkList(object):#链表
    def __init__(self):#初始化
        self.head = 0

    def __getitem__(self, key):#得到某一节点的内容，key相当于节点下标

        if self.is_empty():
            print ('linklist is empty.')
            return

        elif key <0  or key > self.getlength():
            print ('the given key is error')
            return

        else:
            return self.getitem(key)



    def __setitem__(self, key, value):#修改某节点内容

        if self.is_empty():
            print ('linklist is empty.')
            return

        elif key <0  or key > self.getlength():
            print ('the given key is error')
            return

        else:
            self.delete(key)
            return self.insert(key)

    def initlist(self,data,webhead):#初始化链表

        self.head = Node(data,webhead)

    def getlength(self):#返回链表长度

        p =  self.head
        length = 0
        while p!=0:
            length+=1
            p = p.next

        return length

    def is_empty(self):#判断链表是否为空

        if self.getlength() ==0:
            return True
        else:
            return False

    def clear(self):#清空链表

        self.head = 0


    def append(self,data,wh):#队尾插入

        q = Node(data,wh)
        if self.head ==0:
            self.head = q
        else:
            p = self.head
            while p.next!=0:
                p = p.next
            p.next = q


    def getdata(self,index):#得到任意节点内容

        if self.is_empty():
            print ('Linklist is empty.')
            return
        j = 0
        p = self.head

        while p.next!=0 and j <index:
            p = p.next
            j+=1

        if j ==index:
            return p.data

        else:

            print ('target is not exist!')
            
    def getwh(self,index):#得到任意节点内容

        if self.is_empty():
            print ('Linklist is empty.')
            return
        j = 0
        p = self.head

        while p.next!=0 and j <index:
            p = p.next
            j+=1

        if j ==index:
            return p.webhead

        else:

            print ('target is not exist!')
            
    def insert(self,index,data,wh):#在任意位置插入

        if self.is_empty() or index<0 or index >self.getlength():
            print ('Linklist is empty.')
            return

        if index ==0:
            q = Node(data,wh,self.head)

            self.head = q

        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1

        if index ==j:
            q = Node(data,wh,p)
            post.next = q
            q.next = p


    def delete(self,index):#删除任意节点

        if self.is_empty() or index<0 or index >self.getlength():
            print ('Linklist is empty.')
            return
            
        if index == 0:
            self.head = self.head.next
            
        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1

        if index == j:
            post.next = p.next

    def index(self,value):#查找链表中内容等于value的内容

        if self.is_empty():
            print ('Linklist is empty.')
            return

        p = self.head
        i = 0
        while p.next!=0 and not p.data == value:
            p = p.next
            i+=1

        if p.data == value:
            return i
        else:
            return -1



class Web(object): #节点结构体
    def __init__(self, val, p=0):
        self.data = val #val为string类型
        self.next = p

class WebList(object):#链表
    def __init__(self):#初始化
        self.head = 0

    def __getitem__(self, key):#得到某一节点的内容，key相当于节点下标

        if self.is_empty():
            print ('linklist is empty.')
            return

        elif key <0  or key > self.getlength():
            print ('the given key is error')
            return

        else:
            return self.getitem(key)



    def __setitem__(self, key, value):#修改某节点内容

        if self.is_empty():
            print ('linklist is empty.')
            return

        elif key <0  or key > self.getlength():
            print ('the given key is error')
            return

        else:
            self.delete(key)
            return self.insert(key)

    def initlist(self,data):#初始化链表

        self.head = Web(data)

    def getlength(self):#返回链表长度

        p =  self.head
        length = 0
        while p!=0:
            length+=1
            p = p.next

        return length

    def is_empty(self):#判断链表是否为空

        if self.getlength() ==0:
            return True
        else:
            return False

    def clear(self):#清空链表

        self.head = 0


    def append(self,data):#队尾插入

        q = Web(data)
        if self.head ==0:
            self.head = q
        else:
            p = self.head
            while p.next!=0:
                p = p.next
            p.next = q


    def getdata(self,index):#得到任意节点内容

        if self.is_empty():
            print ('Linklist is empty.')
            return
        j = 0
        p = self.head

        while p.next!=0 and j <index:
            p = p.next
            j+=1

        if j ==index:
            return p.data

        else:

            print ('target is not exist!')
            
    def insert(self,index,data):#在任意位置插入

        if self.is_empty() or index<0 or index >self.getlength():
            print ('Linklist is empty.')
            return

        if index ==0:
            q = Web(data, self.head)

            self.head = q

        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1

        if index ==j:
            q = Web(data, p)
            post.next = q
            q.next = p


    def delete(self,index):#删除任意节点

        if self.is_empty() or index<0 or index >self.getlength():
            print ('Linklist is empty.')
            return
            
        if index == 0:
            self.head = self.head.next
            
        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1

        if index == j:
            post.next = p.next

    def index(self,value):#查找链表中内容等于value的内容

        if self.is_empty():
            print ('Linklist is empty.')
            return

        p = self.head
        i = 0
        while p.next!=0 and not p.data == value:
            p = p.next
            i+=1

        if p.data == value:
            return i
        else:
            return -1

class Result(object): #节点结构体
    def __init__(self, val, p=0):
        self.data = val #val为string类型
        self.next = p

class ResultList(object):#链表
    def __init__(self):#初始化
        self.head = 0

    def __getitem__(self, key):#得到某一节点的内容，key相当于节点下标

        if self.is_empty():
            print ('linklist is empty.')
            return

        elif key <0  or key > self.getlength():
            print ('the given key is error')
            return

        else:
            return self.getitem(key)



    def __setitem__(self, key, value):#修改某节点内容

        if self.is_empty():
            print ('linklist is empty.')
            return

        elif key <0  or key > self.getlength():
            print ('the given key is error')
            return

        else:
            self.delete(key)
            return self.insert(key)

    def initlist(self,data):#初始化链表

        self.head = Result(data)

    def getlength(self):#返回链表长度

        p =  self.head
        length = 0
        while p!=0:
            length+=1
            p = p.next

        return length

    def is_empty(self):#判断链表是否为空

        if self.getlength() ==0:
            return True
        else:
            return False

    def clear(self):#清空链表

        self.head = 0


    def append(self,data):#队尾插入

        q = Result(data)
        if self.head ==0:
            self.head = q
        else:
            p = self.head
            while p.next!=0:
                p = p.next
            p.next = q


    def getdata(self,index):#得到任意节点内容

        if self.is_empty():
            print ('Linklist is empty.')
            return
        j = 0
        p = self.head

        while p.next!=0 and j <index:
            p = p.next
            j+=1

        if j ==index:
            return p.data

        else:

            print ('target is not exist!')
            
    def insert(self,index,data):#在任意位置插入

        if self.is_empty() or index<0 or index >self.getlength():
            print ('Linklist is empty.')
            return

        if index ==0:
            q = Result(data, self.head)

            self.head = q

        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1

        if index ==j:
            q = Result(data, p)
            post.next = q
            q.next = p


    def delete(self,index):#删除任意节点

        if self.is_empty() or index<0 or index >self.getlength():
            print ('Linklist is empty.')
            return
            
        if index == 0:
            self.head = self.head.next
            
        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1

        if index == j:
            post.next = p.next

    def index(self,value):#查找链表中内容等于value的内容

        if self.is_empty():
            print ('Linklist is empty.')
            return

        p = self.head
        i = 0
        while p.next!=0 and not p.data == value:
            p = p.next
            i+=1

        if p.data == value:
            return i
        else:
            return -1


Url = ['http://www.sds.bnu.edu.cn/']
Str =['']

#i = -1
#len2=0

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
try:
    solve()
except Exception as e:  
    print (e)    

#结巴分词，输出一个词就建一个词表节点
#print (Str[3])

ll = LinkList()

#for o in range(0,len(Url)):

for o in range(0,5):
    
    web = Url[o]
    seg_list = jieba.cut(Str[o])  
    for word in seg_list:
        #建立链表
        #print(word)
        if ll.getlength() == 0:
            wl = WebList()
            wl.initlist(web)
            ll.initlist(word,wl)

        if ll.getlength() > 0:
            i = ll.index(word)
            if i == -1:
                wl = WebList()
                wl.initlist(web)
                ll.append(word,wl)
                #print(word)
            if i != -1:
                j = ll.getwh(i).index(web)
                if j == -1:
                    ll.getwh(i).append(web)
                    #print(web)

#由于jieba分词的局限只能爬7个网页
#输入
search = input("Please putin your keyword: ")
         
rl = ResultList()
rl.initlist('hahahahahah')
#seach进行结巴分词
seg_list = jieba.cut(search)
for sword in seg_list:
#搜索去重
    k = ll.index(sword)
    if k != -1:
        p = ll.getwh(k).getlength()
        for m in range(0,p):
            b = ll.getwh(k).getdata(m)
            if rl.index(b) == -1:        
                rl.append(b)
                print(b)
