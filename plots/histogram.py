import matplotlib.pyplot as plt
import numpy as np

def plot_histogram(data, title, output_filename):
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')

    fig, axis = plt.subplots()
    X = data[:,0]
    Y = data[:,1]
    axis.set_xlabel(r'association count', fontsize=15)
    axis.set_ylabel(r'number of edges', fontsize=15)

    # add an extra bin for 0
    apx_num_bins = 100
    step = int(X.max()/apx_num_bins)
    bins = range(-step+1, int(X.max())+step+1, step)

    plt.hist(X, bins, weights=Y, log=True, histtype='bar', color='green', align='right')
    plt.savefig(output_filename, bbox_inches='tight')

titles = [ '100000', '100', '25', '400', 'osmGerHist' ]
datasets = [ '100000hist', '100hist', '25hist', '400hist', 'osmGerHist' ]

for i in range(0, len(datasets)):
    dataset = datasets[i]
    title = titles[i]
    data = np.loadtxt('../data/' + dataset)
    output_filename = dataset + '.pdf'
    plot_histogram(data, "\\textsc{" + title.capitalize() + "}", output_filename)
