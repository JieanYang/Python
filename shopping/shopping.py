from selenium import webdriver
import time
from bs4 import BeautifulSoup



def main():
	search = input("search:")
	# search = "dior"
	driver = webdriver.Chrome()
	htmls = [scrawl_sephora(search, driver), scrawl_nocibe(search, driver)]
	driver.close()
	html = initial_html_file(htmls)
	with open('./results.html', 'wb') as f:
		f.write(html.encode("utf-8"))


def initial_html_file(htmls):
	form_html_head = """
	<html>

	<head>
	    <meta charset="utf-8" />
	    <link href="./bootstrap.min.css" rel="stylesheet" />
	    <link href="./results.css" rel="stylesheet" />
	    <title>shopping</title>
	</head>

	<body class="container">
	    """
	form_html_foot = """
	</body>

	</html>
	"""
	
	contents=""
	for html in htmls:
		contents += html

	return form_html_head+contents+form_html_foot

def scrawl_nocibe(search, driver):
	driver.get("https://www.nocibe.fr/")
	driver.find_element_by_id("Rechercher").send_keys(search)
	js = "$('#searchBtn').css('display', 'block');"
	driver.execute_script(js);
	driver.find_element_by_id("searchBtn").click()

	searchs = driver.find_elements_by_class_name("pl_produit")
	html = ""
	for search in searchs:
		html += search.get_attribute("outerHTML")
	html = "<div class=\"row\"><div class=\"col-sm-12\"><p>https://www.nocibe.fr</p></div>"+html+"</div>"
	
	soup = BeautifulSoup(html, features="lxml")
	prev_href = "https://www.nocibe.fr"
	all_href = soup.find_all('a')
	for produt in all_href:
		produt['href'] = prev_href + produt['href']
	all_searchClassique = soup.find_all('article', class_="pl_produit")
	for produt in all_searchClassique:
		produt["class"] = "pl_produit col-sm-3"

	return str(soup.body.div)

def scrawl_sephora(search,driver):
	# driver = webdriver.Chrome()     # 打开 Chrome 浏览器
	driver.get("http://www.sephora.fr/")
	driver.find_element_by_id("champRecherche").send_keys(search)
	driver.find_element_by_id("rechercher").click()

	searchs = driver.find_elements_by_class_name("searchClassique")
	html = ""
	for search in searchs:
		html += search.get_attribute("outerHTML")
	html = "<div class=\"row\"><div class=\"col-sm-12\"><p>http://www.sephora.fr</p></div>"+html+"</div>"
	
	soup = BeautifulSoup(html, features="lxml")
	prev_href = 'http://www.sephora.fr'
	all_href = soup.find_all('a')
	for produt in all_href:
		produt['href'] = prev_href + produt['href']
	all_src = soup.find_all('img')
	for produt in all_src:
		produt['src'] = prev_href + produt['src']
	all_searchClassique = soup.find_all('div', class_="searchClassique")
	for produt in all_searchClassique:
		produt["class"] = "searchClassique col-sm-3"
	# driver.close()
	return str(soup.body.div)


if __name__ == '__main__':
    main()