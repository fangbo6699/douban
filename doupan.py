import requests
from lxml import etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
#     'Referer':'https://movie.douban.com/explore'
}
data=[]
url = 'https://movie.douban.com/top250'
urls=[]
urls.append(url)

    
########################################
# 找规律
# https://movie.douban.com/top250
# https://movie.douban.com/top250?start=50&filter=
########################################
for i in range(1,11):
    a=i*25
    b="?start="+str(a)+"&filter="
    urls.append(url+b)
########################################     
def parse_page(url):
    resp = requests.get(url,headers=headers)
    # resp.content：经过编码后的字符串
    # resp.text：没有经过编码，也就是unicode字符串
    # text：相当于是网页中的源代码了
    text = resp.content.decode('utf-8')
        # print(text)
        # tree：经过lxml解析后的一个对象，以后使用这个对象的xpath方法，就可以
        # 提取一些想要的数据了
    tree = etree.HTML(text)
    all_a = tree.xpath("//ol[@class='grid_view']//li")
    for a in all_a:
        mainpage = a.xpath(".//div[@class='pic']/a/@href")
        print(mainpage)
        data.append({"mainpage":mainpage})
        title = a.xpath(".//div[@class='hd']/a/span[1]/text()")[0]
        print(title)
        data.append({"title":title})
        peopleview = a.xpath(".//div[@class='bd']/div[@class='star']/span[last()]/text()")[0]
        print(peopleview)
        data.append({"peopleview":peopleview})
        score = a.xpath(".//div[@class='bd']/div[@class='star']/span[@class='rating_num']/text()")[0]
        print(score)
        data.append({"score":score})
        print("--------------------")
       
if __name__ == '__main__':
    
    print(urls)
    for url in urls:
        parse_page(url)
        print(data)
 
