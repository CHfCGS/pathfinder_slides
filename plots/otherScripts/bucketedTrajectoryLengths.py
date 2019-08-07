import numpy as np
import matplotlib.pyplot as plt
import math

# run compress.sh first to generate the file

max_exponent = 5
#init buckets with zero
nofPathsInBucket = [0]*max_exponent
numberOfCHEdgesInBucket = [0]*max_exponent

# Read in data
with open("../data/paths.ges.json_pathSizes", "r") as ins:
    arrayX = []
    arrayY = []
    for line in ins:
	tokens = line.split()

	nofOriginalEdges = int(tokens[0])
	nofCHEdges = int(tokens[1])

	if nofOriginalEdges != 0:
		exponent = math.log10( nofOriginalEdges)
		bucket_index = int(exponent)

		nofPathsInBucket[bucket_index] += 1
		numberOfCHEdgesInBucket[bucket_index] += nofCHEdges


latex_nof_paths_row = ""
latex_average_row = ""
for exp in range(max_exponent):
	latex_nof_paths_row += " & " + str(nofPathsInBucket[exp])

	average = numberOfCHEdgesInBucket[exp] / float(nofPathsInBucket[exp])
	latex_average_row += " & " + "%.2f" % average

print latex_nof_paths_row
print latex_average_row