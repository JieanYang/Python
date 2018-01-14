# 我们就来说两个重要的, get, post, 95% 的时间, 你都是在使用这两个来请求一个网页.



# # get
# # 正常打开网页
# # 不往服务器传数据
import requests
import webbrowser
param = {"wd": "莫烦Python"}  # 搜索的信息
r = requests.get('http://www.baidu.com/s', params=param)
print(r.url)
webbrowser.open(r.url)


# post
# 账号登录
# 搜索内容
# 上传图片
# 上传文件
# 往服务器传数据 等
import requests
data = {'firstname': '莫烦', 'lastname': '周'}
r = requests.post('http://pythonscraping.com/files/processing.php', data=data)
print(r.text)

# 上传图片
import requests
file = {'uploadFile': open('./image.png', 'rb')}
r = requests.post('http://pythonscraping.com/files/processing2.php', files=file)
print(r.text)


# 登录
import requests
payload = {'username': 'Morvan', 'password': 'password'}
r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
print(r.cookies.get_dict())
# {'username': 'Morvan', 'loggedin': '1'}

r = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies=r.cookies)
print(r.text)


# Session 无需每次都输入cookie
import requests
session = requests.Session()
payload = {'username': 'Morvan', 'password': 'password'}
r = session.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
print(r.cookies.get_dict())

r = session.get("http://pythonscraping.com/pages/cookies/profile.php")
print(r.text)