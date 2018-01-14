from urllib.request import urlopen


# 登录网页
# if has Chinese, apply decode()
html = urlopen(
    "https://morvanzhou.github.io/static/scraping/basic-structure.html"
).read().decode('utf-8')
print(html)


# 匹配内容
import re
res = re.findall(r"<title>(.+?)</title>", html)
print("\nPage title is: ", res[0])

# 找到所有链接
res = re.findall(r'href="(.*?)"', html)
print("\nAll links: ", res)