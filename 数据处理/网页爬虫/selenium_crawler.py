from selenium import webdriver
import time
driver = webdriver.Chrome()     # 打开 Chrome 浏览器

# 将刚刚复制的帖在这
driver.get("https://morvanzhou.github.io/")
driver.find_element_by_xpath(u"//img[@alt='强化学习 (Reinforcement Learning)']").click()
driver.find_element_by_link_text("About").click()
driver.find_element_by_link_text(u"赞助").click()
driver.find_element_by_link_text(u"教程 ▾").click()
driver.find_element_by_link_text(u"数据处理 ▾").click()
driver.find_element_by_link_text(u"网页爬虫").click()

time.sleep(2)
# 得到网页 html, 还能截图
html = driver.page_source       # get html
driver.get_screenshot_as_file("./img/sreenshot1.png")
driver.close()

# 最后, Selenium 的优点我们都看出来了, 可以很方便的帮你模拟你的操作, 
# 添加其它操作也是非常容易的, 但是也是有缺点的, 不是任何时候 selenium 都很好. 
# 因为要打开浏览器, 加载更多东西, 它的执行速度肯定没有其它模块快. 所以如果你需要速度, 
# 能不用 Selenium, 就不用吧.

