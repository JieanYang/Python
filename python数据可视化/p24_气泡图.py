import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")
mov = pd.read_csv("./ucdavis.csv")

x = mov.tv
y = mov.computer
z = mov.sleep

cm = plt.cm.get_cmap('RdYlBu')
fig, ax = plt.subplots(figsize=(10,5))

sc = ax.scatter(x, y, s=z*50, c=z, cmap=cm, linewidth=0.2, alpha=0.5)
ax.grid()
fig.colorbar(sc)

ax.set_xlabel('tv', fontsize=14)
ax.set_ylabel('computer', fontsize=14)

plt.show()