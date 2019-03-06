import demjson
import math
from math import sin, cos
import matplotlib.pyplot as plt

f = open('data/exp.json')
json = f.read()
# json = json[:-10]
obj = demjson.decode(json)



fig, ax = plt.subplots()


def viz_arrow(x, y, th, color = "k"):
	LEN = 0.25
	for (ix,iy,ith) in zip(x, y, th):
		ax.arrow(float(ix), float(iy), (LEN * cos(ith)), (LEN * sin(ith)), head_width=0.1, head_length=0.1, fc=color, ec=color)

def viz_path(x, y, th, color = 'k'):
	ax.scatter(x, y, color = color, s=3)
	# ax.plot(x, y)
	viz_arrow(x, y, th, color = color)

def viz_obs(path, obs, color = 'k'):


	for i in range(1, len(path["x"])):
		px = float(path["x"][i])
		py = float(path["y"][i])
		pth = float(path["th"][i])

		# print(i-1, obs[i-1])

		for ob in obs[i-1]:


			r = float(ob["range"])
			b = float(ob["bearing"])
			l = int(ob["id"])

			# print l

			x = px + r * cos(pth + b)
			y = py + r * sin(pth + b)

			ax.annotate(str(l), (x,y), color = color)



mx = map(lambda m: float(m["x"]), obj["map"]);
my = map(lambda m: float(m["y"]), obj["map"]);



gx = obj["state"]["x"]
gy = obj["state"]["y"]
gth = obj["state"]["th"]

ix = obj["infered"]["x"]
iy = obj["infered"]["y"]
ith = obj["infered"]["th"]



viz_path(gx, gy, gth, 'green')
viz_path(ix, iy, ith, 'orange')

viz_obs(obj["infered"], obj["observations"], 'orange')

ax.scatter(mx, my)
for i,_ in enumerate(mx):
    ax.annotate(str(i), (mx[i],my[i]))


plt.show()