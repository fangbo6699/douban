import requests
from lxml import etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
#     'Referer':'https://movie.douban.com/explore'
}
url = 'https://movie.douban.com/top250'
moreurl=[]
# https://movie.douban.com/top250?start=25&filter=
# https://movie.douban.com/top250?start=50&filter=
for i in range(1,11):
#     moreurl[i+1]=url+"?start=i*25&filter="
#     list(moreurl)
    a=i*25
    b="?start="+str(a)+"&filter="
    moreurl.append(url+b)
#     print(moreurl[i-1])

    
for url in moreurl:
#     print(i)
    resp = requests.get(url,headers=headers)
        # resp.content：经过编码后的字符串
        # resp.text：没有经过编码，也就是unicode字符串
        # text：相当于是网页中的源代码了
    text = resp.content.decode('utf-8')
    # print(text)
        # tree：经过lxml解析后的一个对象，以后使用这个对象的xpath方法，就可以
        # 提取一些想要的数据了
    tree = etree.HTML(text)
        # xpath/beautifulsou4
    all_a = tree.xpath("//ol[@class='grid_view']//li")
    for a in all_a:
        mainpage = a.xpath(".//div[@class='pic']/a/@href")[0]
        print(mainpage)

        title = a.xpath(".//div[@class='hd']/a/span[1]/text()")[0]
        print(title)
        people = a.xpath(".//div[@class='bd']/div[@class='star']/span[last()]/text()")[0]
        print(people)
        score = a.xpath(".//div[@class='bd']/div[@class='star']/span[@class='rating_num']/text()")[0]
        print(score)
        print("--------------------")
