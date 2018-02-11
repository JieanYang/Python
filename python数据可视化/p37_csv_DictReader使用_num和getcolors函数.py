import csv
import matplotlib.pyplot as plt

# csv has Name, Year, Age, Cmp, Att, Yds, TD, Teams
# example
# with open('./qb_data.csv') as csvfile:
# 	reader = csv.DictReader(csvfile)
# 	for row in reader:
# 		name = row['Name']
# 		tds = row['TD']

# ways to call DictReader

# if fieldname are Name, Year, Age, Cmp, Att, Yds, TD, Teams
if __name__ ==  '__main__':
	fieldnames = ['Name', 'Year', 'Age', 'Cmp', 'Att', 'Yds', 'TD', 'Teams']
	with open('./qb_data.csv') as csvfile:
		reader = csv.DictReader(csvfile, fieldnames=fieldnames)
		# if csv file has first row as Name, Year, Cmp, Att, Yds, TD, Teams
		# we don't need to define fieldnames, the reader automatically recognizes them.
		for row in reader:
			print(row['Name'])


# 转换和返回数值型数值的函数 
# prepare.py 中的 getcolors() 和 num()
def num(s):
	try:
		return int(s)
	except ValueError:
		return 0

def getcolors():
	colors=[(31,119,180), (255,0,0), (0,255,0), (148,103,189),(140,86,75), \
	(218,73,174), (127,127,127), (140,140,26), (23,190,207), (65,200,100), \
	(200,65,100), (125,255,32), (32,32,198), (255,191,201), (172,191,201), \
	(0,128,0), (244,130,150), (255,127,14), (128,128,0),(10,10,10), (44,160,44), \
	(214,39,40), (206,206,216)]
	for i in range(len(colors)):
		r, g, b = colors[i]
		colors[i] = (r/255., g/255., b/255.)
	return colors

	