

# 选着要爬的网址 (url)
# 使用 python 登录上这个网址 (urlopen等)
# 读取网页信息 (read() 出来)
# 将读取的信息放入 BeautifulSoup
# 使用 BeautifulSoup 选取 tag 信息等 (代替正则表达式)

from bs4 import BeautifulSoup
from urllib.request import urlopen

# if has Chinese, apply decode()
html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')
print(html)


# 读取这个网页信息, 我们将要加载进 BeautifulSoup, 以 lxml 的这种形式加载. 
# 除了 lxml, 其实还有很多形式的解析器, 不过大家都推荐使用 lxml 的形式. 
# 然后 soup 里面就有着这个 HTML 的所有信息. 
# 如果你要输出 <h1> 标题, 可以就直接 soup.h1.
# https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id9
soup = BeautifulSoup(html, features='lxml')
print('\n',soup.h1)
print('\n', soup.p)



all_href = soup.find_all('a')
all_href = [l['href'] for l in all_href]
print('\n', all_href)