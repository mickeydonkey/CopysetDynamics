from cluster_simu.cluster import Cluster
import matplotlib.pyplot as plt
import random
import numpy as np

N = 30
R = 3
S = 4

steps = [1]

x = [[] for _ in range(len(steps))]
scatter_widths = [[] for _ in range(len(steps))]
copysets_number = [[] for _ in range(len(steps))]

x_base = []
scatter_widths_base = []
copysets_number_base = []

for i, s in enumerate(steps):
    iterations = int(np.ceil(20/s))
    c = Cluster(N, R, S, init = 'greedy')

    for ii in range(iterations):
        print("{}: {}".format(s, N - s * ii))
        mean_sw = c.mean_sw()
        curr_x = N - s * ii

        x[i-1].append(curr_x)
        scatter_widths[i-1].append(mean_sw)
        copysets_number[i-1].append(len(c.greedy_copysets))

        nodes = c.get_node_indices()
        indices = random.sample(nodes, k=s)

        c.remove_nodes(indices)

        if i == len(steps) - 1:
            c_base = Cluster(curr_x, R, S, init = 'greedy')
            x_base.append(curr_x)
            scatter_widths_base.append(c_base.mean_sw())
            copysets_number_base.append(len(c_base.greedy_copysets))

plt.style.use("ggplot")
plt.figure()
for i,s in enumerate(steps):
    label = "step" + str(s)
    plt.plot(x[i-1], scatter_widths[i-1], label=label)
plt.plot(x_base, scatter_widths_base, label="base")
plt.xlabel("#nodes")
plt.ylabel("mean scatter width")
plt.legend(loc="upper left")
plt.savefig('remove_simulation_sw.png')


plt.style.use("ggplot")
plt.figure()
for i,s in enumerate(steps):
    label = "step" + str(s)
    plt.plot(x[i-1], copysets_number[i-1], label=label)
plt.plot(x_base, copysets_number_base, label="base")
plt.xlabel("#nodes")
plt.ylabel("#copysets")
plt.legend(loc="upper left")
plt.savefig('remove_simulation_copysets.png')
