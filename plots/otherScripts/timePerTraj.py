import numpy as np
import matplotlib.pyplot as plt
import unicodedata

#Overview table for time: The Columns are the BB sizes and the rows are the distances
#       |||   0.500|   0.250|   0.125|   0.062|   0.031|
#-------|||--------|--------|--------|--------|--------|
#     25|||   0.817|   0.628|   0.270|   0.093|   0.041|
#    100|||   5.630|   4.381|   1.866|   0.609|   0.201|
#    400|||   6.177|   4.959|   2.124|   0.685|   0.222|
# 100000|||   6.889|   4.773|   1.882|   0.608|   0.211|


#Overview table for nofPaths: The Columns are the BB sizes and the rows are the distances
#       |||            0|            0|            0|            0|            0|
#-------|||-------------|-------------|-------------|-------------|-------------|
#     25|||       168570|       134451|        57107|        18468|         6595|
#    100|||      2288640|      1948294|       903384|       314285|       122174|
#    400|||      2824558|      2511392|      1359735|       568822|       256962|
# 100000|||      4781852|      4174645|      2577375|      1334826|       745257|


nofBBSizes = 5
arrayTime = [
	[0.817,   0.628,   0.270,   0.093,   0.041],
	[5.630,   4.381,   1.866,   0.609,   0.201],
	[6.177,   4.959,   2.124,   0.685,   0.222],
	[6.889,   4.773,   1.882,   0.608,   0.211]
]

arrayNofPaths = [
	[168570,       134451,        57107,        18468,         6595],
	[2288640,      1948294,       903384,       314285,       122174],
	[2824558,      2511392,      1359735,       568822,       256962],
	[4781852,      4174645,      2577375,      1334826,       745257]
]

arrayX = np.arange(1, nofBBSizes + 1)
nofDist = 4
arrayDist = [25, 100, 400, 100000]

# Plot
for i in range (nofDist):
	arrayY = []
	for j in range (nofBBSizes):
		timePerPath = arrayTime[i][j] / arrayNofPaths[i][j]
		timeInMicroseconds = timePerPath * 10 ** 6
		arrayY.append( timeInMicroseconds)
	plt.plot(arrayX, arrayY, label=str(arrayDist[i]) + ' km')

plt.title('Time per Trajectory')
plt.xlabel('Query rectangle size parameter r')
plt.ylabel(unichr(181) + 's')
plt.legend()
plt.xticks(arrayX)
plt.ylim(ymin=0)
plt.show()