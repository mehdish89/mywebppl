import matplotlib.pyplot as plt
import matplotlib.cm as cm
# f = open('./data.txt')
# ls = f.read().split('\n')[1:-2]
# data = map(float, ls)
# print data
# plt.scatter(range(len(data)), data)

def is_number(n):
	try:
		float(n)
	except ValueError:
		return False
	return True

import csv
import numpy as np

plt.switch_backend('wxAgg')
mng = plt.get_current_fig_manager()
mng.frame.Maximize(True)

plt.subplots_adjust(left=0.04, bottom=0.04, right=0.97, top=0.97, wspace=0, hspace=0)

ax = plt.gca()

for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(18) 
for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(18) 
        tick.label.set_rotation(65)

ax.autoscale(enable=True, axis='both', tight=True)
	

with open('./data.csv') as f:
	reader = csv.reader(f, delimiter='\t')
	# data = [(int(t), float(sumW)) for t, sumW in reader]
	brk_point = float(reader.next()[0])
	data = np.array([line for line in reader if is_number(line[0])], dtype='float32')

	t = data[:, 0]
	sumW = data[:, 1]
	factorId = data[:, 2]
	print t
	print sumW
	print factorId

cmap = plt.get_cmap('Set1')
# cmap = plt.get_cmap('Spectral')
# cmap = plt.get_cmap('gray')
colors = cmap(np.linspace(0, 1, max(factorId)+1))
print colors

for fid in factorId:
	t_i = data[factorId==fid][:, 0]
	sumW_i = data[factorId==fid][:, 1]

	print colors[fid]

	plt.scatter(t_i, sumW_i, color=colors[fid], alpha=0.5)
	# plt.plot(t_i, sumW_i)
	# print t
	# print sumW


minW = min(filter(lambda x: x != -float('inf'), sumW))
maxW = max(sumW)

plt.plot([brk_point-0.5, brk_point-0.5], 
	 [minW, maxW],
	 color='r',
	 linewidth=5,
	 alpha=0.3)

plt.text(brk_point - 1, minW, 'breaking point \n = ' + str(brk_point) + ' ',
	 horizontalalignment='right',
	 color='r',
	 fontsize=28)

# plt.scatter(t, sumW)


plt.show()


