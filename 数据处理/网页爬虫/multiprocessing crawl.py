# https://blog.scrapinghub.com/2015/08/05/distributed-frontera-web-crawling-at-large-scale/
# http://bittiger.blogspot.fr/2016/02/blog-post_3.html


import multiprocessing as mp
import time
from urllib.request import urlopen, urljoin
from bs4 import BeautifulSoup
import re



def crawl(url): # 爬取
	print('crawl:', url)
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
# DON'T OVER CRAWL THE WEBSITE OR YOU MAY NEVER VISIT AGAIN
if base_url != "http://127.0.0.1:4000/":
    restricted_crawl = True
else:
    restricted_crawl = False

def main():
    # freeze_support()
    unseen = set([base_url,])
    seen = set()

    count, t1 = 1, time.time()

    pool = mp.Pool(4)
    while len(unseen) != 0:
        if restricted_crawl and len(seen) >= 10:
            break
        # htmls = [crawl(url) for url in unseen]
        # --->
        print('\nDistributed Crawling...')
        crawl_jobs = [pool.apply_async(crawl, args=(url,)) for url in unseen]
        htmls = [j.get() for j in crawl_jobs]

        # results = [parse(html) for html in htmls]
        # --->
        print('\nDistributed Parsing...')
        parse_jobs = [pool.apply_async(parse, args=(html,)) for html in htmls]
        results = [j.get() for j in parse_jobs]

        print('\nAnalysing...')
        seen.update(unseen)         # seen the crawled
        unseen.clear()              # nothing unseen

        for title, page_urls, url in results:
            print(count, title, url)
            count += 1
            unseen.update(page_urls - seen)     # get new url to crawl
    print('Total time: %.1f s' % (time.time()-t1, ))    # 16 s !!!

if __name__ == '__main__':
    main()