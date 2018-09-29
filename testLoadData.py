
import csv
import matplotlib.pyplot as plt

#must_have == dictionary of items each line must contain
#cant_have == dictionary of items each line must not contain
def load_death_data(file_name, must_have, cant_have):
    raw_data = []
    with open(file_name) as fp:
        reader = csv.reader(fp)
        raw_data = list(reader)

    final_data = [] #only lines that contain needed element
    for line in raw_data:
        if (all([line[v] == k for k, v in must_have.items()]) and 
            all([line[v] != k for k, v in cant_have.items()])):
            final_data.append(line)
    return final_data


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
