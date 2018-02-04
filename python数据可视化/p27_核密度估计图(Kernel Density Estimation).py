from numpy.random import random
import matplotlib as mpl
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_palette("hls")
mpl.rc("figure", figsize=(10,6))
data = random(250)
plt.title("KDE Demonstration using seaborn and Matplotlib", fontsize=20)
sns.distplot(data, color='#ff8000')

plt.show()