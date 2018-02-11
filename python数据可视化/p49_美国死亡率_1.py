import csv
import matplotlib.pyplot as plt

def num(s):
	try:
		return float(s)
	except ValueError:
		return 0

fig = plt.figure(figsize=(15,13))
# ax = fig.add_subplot(111,axisbg='white')
plt.ylim(740,1128)
plt.xlim(1965,2011)

with open('./mortality1.csv') as csvfile:
	mortdata = [row for row in csv.DictReader(csvfile)]

x = []
males_y = []
females_y = []
every_y = []
yrval = 1968

for row in mortdata:
	x += [yrval]
	males_y += [num(row['Males'])]
	females_y += [num(row['Females'])]
	every_y += [num(row['Everyone'])]
	yrval = yrval +1


plt.plot(x,males_y, color='#1a61c3', label='Males', linewidth=1.8)
plt.plot(x, females_y, color='#bc108d', label='Females', linewidth=1.8)
plt.plot(x, every_y, color='#747e8a', label='Everyone', linewidth=1.8)
plt.legend(loc=0, prop={'size':10})

plt.xlabel('years', fontsize=18)
plt.ylabel('Death',fontsize=18)
plt.title('Mortality of America(1968~2010) based on 100 000 people')
plt.show()