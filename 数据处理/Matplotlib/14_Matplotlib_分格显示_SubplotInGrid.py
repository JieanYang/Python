import matplotlib.pyplot as plt


# method 1:subplot2grid
######################################
plt.figure()
# span 跨度
ax1 = plt.subplot2grid((3,3),(0,0),colspan=3,rowspan=1)
ax1.plot([1,2],[1,2])
ax1.set_title('ax1_title')
# ax1.set_xlabel()
# ax1.set_xlim()

ax2 = plt.subplot2grid((3,3),(1,0),colspan=2)
ax3 = plt.subplot2grid((3,3),(1,2),rowspan=2)
ax4 = plt.subplot2grid((3,3),(2,0))
ax5 = plt.subplot2grid((3,3),(2,1))

# method 2:gridspec
######################################
import matplotlib.gridspec as gridspec
plt.figure()
gs = gridspec.GridSpec(3,3)
ax6 = plt.subplot(gs[0,:])
ax7 = plt.subplot(gs[1,:2])
ax8 = plt.subplot(gs[1:,2])
ax9 = plt.subplot(gs[2,:1])
ax10 = plt.subplot(gs[2,1:2])


# method 3:easy to define structure
######################################
# f: figure
f, ((ax11,ax12),(ax21,ax22)) = plt.subplots(2,2,sharex=True,sharey=True)
ax11.scatter([1,2],[1,2])


# plt.tight_layout()
# plt.show()