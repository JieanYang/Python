# https://blog.scrapinghub.com/2015/08/05/distributed-frontera-web-crawling-at-large-scale/
# http://bittiger.blogspot.fr/2016/02/blog-post_3.html


import multiprocessing as mp
import time
from urllib.request import urlopen, urljoin
from bs4 import BeautifulSoup
import re



def crawl(url): # 爬取
	response = urlopen(url)
	# time.sleep(0.1) # 爬取延迟 slightly delay for downloading
	return response.read().decode()

def parse(html): # 解析
    soup = BeautifulSoup(html, 'lxml')
    urls = soup.find_all('a', {"href": re.compile('^/.+?/$')})
    title = soup.find('h1').get_text().strip()
    page_urls = set([urljoin(base_url, url['href']) for url in urls])   # 去重
    url = soup.find('meta', {'property': "og:url"})['content']
    return title, page_urls, url # tuple 格式

# base_url = "http://127.0.0.1:4000/"
base_url = 'https://morvanzhou.github.io/'

unseen = set([base_url,])
seen = set()

count, t1 = 1, time.time()

# DON'T OVER CRAWL THE WEBSITE OR YOU MAY NEVER VISIT AGAIN
if base_url != "http://127.0.0.1:4000/":
    restricted_crawl = True
else:
    restricted_crawl = False

while len(unseen) != 0:  # still get some url to visit
    if restricted_crawl and len(seen) >= 20:
        break
    
    print('\nDistributed Crawling...')
    htmls = [crawl(url) for url in unseen]
    
    print('\nDistributed Parsing...')
    results = [parse(html) for html in htmls]

    print('\nAnalysing...')
    seen.update(unseen)  # seen the crawled
    unseen.clear()  # nothing unseen

    for title, page_urls, url in results:
    	print(count, title, url)
    	count += 1
    	# 在page_urls 里筛选出已经 seen 的链接，加到 unseen 里
    	unseen.update(page_urls - seen)  # get new url to crawl
print('Total time: %.1f s' % (time.time()-t1, )) 