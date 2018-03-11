# coding=utf-8       
import requests as tt
import urllib
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import time
import pdfkit
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
{content}
</body>
</html>
"""


def geturls(url):  #获取所有url
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    wb=tt.get(url,headers=headers)
    wb.encoding='utf-8'#显示指定网页编码
    time.sleep(5)
    soup=BeautifulSoup(wb.text,'lxml')
    a=soup.find_all('a',attrs={'target':'_top'})
    lista=[]     #收集所有url
    for each in a:
        '''
        if each.get('href')[:4]=='wiki': #筛选符合条件的url
        '''
        url2="http://www.runoob.com"+each.get('href')
        lista.append(url2)
    print(lista)
    return lista



def read2(url):               #获取各个页的文字
    headers={
    'User-Agent':'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11'
    }
    x=1
    i=1
    url[8]='http://www.runoob.com/mongodb/mongodb-create-database.html'
    url[9]='http://www.runoob.com/mongodb/mongodb-dropdatabase.html'
    print(len(url))
    for each in url:
        wb=tt.get(each,headers=headers)
        wb.encoding='utf-8'
        soup=BeautifulSoup(wb.text,'lxml')
        a=soup.find_all('div',class_="article-intro")
        a=str(a)
        html=html_template.format(content=a)#将tag形式的a转化为字符形式才能用format方法
          #将str形式的html转化为字节形式的bytes才能以wb方法写入文件
        with open('E:/mongodb.html','a+',encoding='utf-8') as f:
            print('正在处理第%s个-----------------------------------------' %x)
            f.write(html)
        x=x+1
        i=i+2
        time.sleep(i)


def save_pdf(htmls):
    #把所有html文件转成pdf
    options={
        'page-size':'letter',
        'encoding':'utf-8',
        'custom-header':[('Accept-Encoding','gzip')]
    }
    pdfkit.from_file(htmls,'mongodb.pdf',options=options)    
 


if __name__=="__main__":
    url='http://www.runoob.com/mongodb/mongodb-tutorial.html'
    a=geturls(url)
    print(len(a))
    read2(a)
    save_pdf('mongodb.html')