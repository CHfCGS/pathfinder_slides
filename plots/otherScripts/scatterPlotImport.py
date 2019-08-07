import numpy as np
import matplotlib.pyplot as plt
import subprocess

# run compress.sh first to generate the file

# Read in data
with open("../data/paths.ges.json_pathSizes", "r") as ins:
    arrayX = []
    arrayY = []
    for line in ins:
	tokens = line.split()

	arrayX.append(int(tokens[0]))
	arrayY.append(int(tokens[1]))

colors = (0,0,0)
area = 0.0001

# Plot
plt.scatter(arrayX, arrayY, s=area, c=colors, alpha=1)
plt.title('Trajectory lengths in # edges')
plt.xlabel('original')
plt.ylabel('compressed')
plt.xscale('log')
plt.yscale('log')
plt.xlim(xmin=1)
plt.xlim(xmax=(10**4))
plt.ylim(ymin=1)
plt.ylim(ymax=(10**3))

plt.savefig('trajectory_lengths.png', dpi=1000)

#makes the pdf really big
#plotFilename="../../TrajQueries/graphics/trajectory_lengths.svg"
#plt.savefig(plotFilename)

#convert to pdf_latex
#latex_pdfFilename="../../TrajQueries/graphics/trajectory_lengths.pdf"
#command="inkscape -D -z --file=" + plotFilename + " --export-pdf=" + latex_pdfFilename + " --export-latex"
#subprocess.call(command, shell=True)