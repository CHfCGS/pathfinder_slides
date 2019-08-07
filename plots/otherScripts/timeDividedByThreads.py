import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

nofBBSizes = 5
arrayTime = [
	[8.334, 4.987, 2.029, 0.864, 0.150],
	[4.811, 3.788, 1.537, 0.703, 0.122],
	[2.722, 1.999, 0.830, 0.348, 0.072],
	[1.351, 1.067, 0.447, 0.210, 0.056],
	[0.801, 0.624, 0.273, 0.130, 0.037],
	[0.632, 0.495, 0.196, 0.099, 0.032]
]

arrayNofThreads = [1, 2, 4, 8, 16, 24]

# Plot
for i in range (nofBBSizes):
	arrayY = []
	for j in range(len(arrayNofThreads)):
		normalizedTime = arrayTime[j][i] * arrayNofThreads[j]
		arrayY.append( normalizedTime)
	rectangleSize = 2**(-(i+1))
	plt.plot(arrayNofThreads, arrayY, label=str(Fraction(rectangleSize)))

plt.title('Time * # threads')
plt.xlabel('# threads')
plt.ylabel('seconds')
plt.legend()
plt.xticks(arrayNofThreads)
plt.ylim(ymin=0)
plt.show()