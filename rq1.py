from planner import *
from othertools import *
import matplotlib.pyplot as plt


def main():
    score_2t = readfile('rq1_TimeLIME.csv')
    score_2f = readfile('rq1_LIME.csv')
    scores2_x = readfile('rq1_XTREE.csv')
    scores2_alve = readfile('rq1_Alves.csv')
    scores2_shat = readfile('rq1_Shat.csv')
    scores2_oliv = readfile('rq1_Oliv.csv')
    score2_rw = readfile('rq1_Random.csv')

    plt.subplots(figsize=(7, 7))
    plt.rcParams.update({'font.size': 16})
    # ind=np.arange(10)
    N = len(scores2_x)
    width = 0.25
    dummy1, dummy2, dummy3, dummy4, dummy5, dummy6, dummy7 = [], [], [], [], [], [], []
    for i in range(0, len(scores2_x)):
        dummy1.append(np.round(1 - np.mean(score_2t[i]), 3) * 20)
        dummy2.append(np.round(1 - np.mean(score_2f[i]), 3) * 20)
        dummy3.append(np.round(1 - np.mean(scores2_x[i]), 3) * 20)
        dummy4.append(np.round(1 - np.mean(scores2_alve[i]), 3) * 20)
        dummy5.append(np.round(1 - np.mean(scores2_shat[i]), 3) * 20)
        dummy6.append(np.round(1 - np.mean(scores2_oliv[i]), 3) * 20)
        dummy7.append(np.round(1 - np.mean(score2_rw[i]), 3) * 20)
    plt.scatter(np.arange(N), dummy2, label='Classical LIME', s=100, marker='o')
    plt.scatter(np.arange(N), dummy3, label='XTREE', s=100, marker='o')
    plt.scatter(np.arange(N), dummy4, label='Alves', s=100, marker='o')
    plt.scatter(np.arange(N), dummy5, label='Shatnawi', s=100, marker='o')
    plt.scatter(np.arange(N), dummy6, label='Oliveira', s=100, marker='o')
    plt.scatter(np.arange(N), dummy7, label='RandomWalk', s=100, marker='v')
    plt.plot(np.arange(N), dummy1, label='TimeLIME', marker='^', markersize=10, color='#22406D')

    # plt.ylim(-11,130)
    plt.xticks(np.arange(N), ['jedit', 'camel1', 'camel2', 'log4j', 'xalan', 'ant', 'velocity', 'poi', 'synapse'])
    plt.yticks([0, 2, 4, 6, 8, 10, 12])
    plt.subplots_adjust(bottom=0.2, left=0, right=1.1)
    plt.grid(axis='y')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True, ncol=3)
    plt.savefig("rq1", dpi=200, bbox_inches='tight')
    plt.show()

    return


if __name__ == "__main__":
    main()
