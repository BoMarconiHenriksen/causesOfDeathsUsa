''' 
This class is plotting the increase in alzheimers in a periode from 1999 to 2016.
'''

import matplotlib.pyplot as plt

def plot_increse(dead, year, state):
    plot_file = 'alzheimers.png'
    xs = year
    ys = dead
    xlabels = year
    plt.title("Increases in deaths of Alzheimers in " + state, fontsize=16) #+str(state)
    plt.xlabel("Years", fontsize=12)
    plt.ylabel("Changes in number of deaths", fontsize=12)
    plt.xticks(xs, xlabels, rotation='vertical')
    plt.tight_layout(pad=2.0)
    plt.bar(xs, ys)
    plt.savefig(plot_file)