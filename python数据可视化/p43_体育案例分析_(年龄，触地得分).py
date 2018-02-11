from p37_csv_DictReader使用_num和getcolors函数 import num
from p37_csv_DictReader使用_num和getcolors函数 import getcolors

import csv
import matplotlib.pyplot as plt

def maxAge():
	maxage = 30

	with open('./qb_data.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			if(num(row['Age'])>maxage):
				maxage = num(row['Age'])
	print(maxage) # output -> 44

# if __name__ == "__main__":
# 	maxAge()
def getQbNames():
	qbnames = ['peyton Manning']
	# name = ''
	i = 0
	with open('./qb_data.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			if(qbnames[i] != row['Name']):
				qbnames.append(row['Name'])
				i = i+ 1
	return qbnames

def readQbdata():
	resultdata = []
	with open('./qb_data.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		resultdata = [row for row in reader]
		return resultdata
qbnames = getQbNames()
fdata = readQbdata()

i = 0
# rank = 0
prevysum = 0
lastyr = 0
highrank = 300
colorsdata = getcolors()

fig = plt.figure(figsize=(15,13))
ax = fig.add_subplot(111,axisbg='white')

# limits for TD
plt.ylim(10,744)
# changes xlimit to have age ranges
plt.xlim(20,50)

colindex=0
lastage=20

for qbn in qbnames:
	x = []
	y = []
	prevysum = 0
	for row in fdata:
		if(row['Name'] == qbn and row['Year'] != 'Career'):
			yrval = num(row['Year'])
			lastage = num(row['Age'])
			prevysum += num(row['TD'])
			lastyr = yrval
			x += [lastage]
			y += [prevysum]

	if(prevysum > highrank):
		if(lastage == 44):
			plt.plot(x, y, color='red', label=qbn, linewidth=3.5)
		else:
			plt.plot(x, y, color=colorsdata[colindex],label=qbn, linewidth=2.5)
			plt.legend(loc=0, prop={'size':10})
		colindex = (colindex+1)%22
		if qbn == 'Tom Brady':
			plt.text(lastage, prevysum-6, qbn+"("+str(prevysum)+"):"\
				+str(lastage),fontsize=9)
		else:
			plt.text(lastage-1, prevysum+2, qbn+"("+str(prevysum)+"):"\
				+str(lastage),fontsize=9)
	else:
		if(lastage == 44):
			plt.plot(x, y, color='red', label=qbn, linewidth=3.5)
			plt.text(lastage-1, prevysum+2, qbn+"("+str(prevysum)+"):"\
				+str(lastage), fontsize=9)
		else:
			plt.plot(x, y, color=colorsdata[22], linewidth=1.5)


plt.xlabel('Age', fontsize=18)
plt.ylabel('Number of Touch Downs', fontsize=18)
plt.title("Touch Downs by Quarter Backs by Age", fontsize=20)
plt.show()

# Question: 
# 哪位四分卫球员职业生涯最长
# Warrren Moon and Vinny Testaverde are 44 years
# 现在还有能超越Peyton Manning锄地得分记录的四分卫球员吗?
# 35 year old Drew Brees has scores 396 points