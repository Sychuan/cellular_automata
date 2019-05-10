import matplotlib.pyplot as plt
import numpy as np

time = 60
size = 30

cells = np.zeros((size, time), dtype=np.int32)
cells[1, 0] = 1

rules = np.array(
    [[1, 1, 1], [1, 1, 0], [1, 0, 1], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
)
results = [0, 1, 1, 0, 1, 1, 1, 0]


def img_save(t, cells):
    fig = plt.figure(figsize=(5, 5), dpi=300)
    plt.set_cmap('hot')
    ax = plt.axes([0, 0, 1, 1])
    plt.axis('off')
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    plt.imshow(cells[:, :])
    plt.savefig("step_{}.png".format(t), bbox_inches='tight', pad_inches=0)
    # plt.show()
    plt.close()


img_save(0, cells)
for t in range(1, time):
    left = np.roll(cells[:, t - 1], 1)
    center = cells[:, t - 1]
    right = np.roll(cells[:, t - 1], -1)
    center = cells[:, t - 1]
    for n in range(size):
        # print(left[n], center[n], right[n])
        test = np.array([left[n], center[n], right[n]])
        for k, rule in enumerate(rules):
            if all(rule == test):
                cells[n, t] = results[k]
                break
    img_save(t, cells)
