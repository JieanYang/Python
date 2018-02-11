from p37_csv_DictReader使用_num和getcolors函数 import num
from p37_csv_DictReader使用_num和getcolors函数 import getcolors

import csv
import matplotlib.pyplot as plt




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

# fdata = []
# prevysum = 0


qbnames = getQbNames()
fdata = readQbdata()

i = 0
# rank = 0
prevysum = 0
lastyr = 0
highrank = 392
colorsdata = getcolors()

fig = plt.figure(figsize=(15,13))
ax = fig.add_subplot(111,axisbg='white')

# limits for TD
plt.ylim(10,744)
plt.xlim(1940,2021)

colindex = 0
lastage = 20


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
			x += [yrval]
			y += [prevysum]


	if(prevysum > highrank):
		plt.plot(x, y, color=colorsdata[colindex], label=qbn, linewidth=2.5)
		# plt.plot([1940,1950,1960],[100,200,125], linewidth=3)
		plt.legend(loc=0, prop={'size':10})
		colindex = (colindex+1)%22
		plt.text(lastyr-1, prevysum+2, qbn+"("+str(prevysum)+"):"+str(lastage), \
			fontsize=9)
	else:
		plt.plot(x, y, color=colorsdata[22], linewidth=1.5)
plt.xlabel('Year', fontsize=18)
plt.ylabel('Cumulative Touch Downs', fontsize=18)
plt.title("Cumulative Touch Downs by Quarter Backs", fontsize=20)
plt.show()
