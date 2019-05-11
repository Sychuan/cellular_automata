import matplotlib.pyplot as plt
import numpy as np

time = 500
size = 500
save_every_step = False

# creating empty world x-axis = space size, y-axis time
cells = np.zeros((size, time), dtype=np.int32)


# random starting configuration
def random_start():
    return np.random.randint(0, 3, size)


# starting configuration

cells[:, 0] = random_start()

configuration = np.array(
    [[1, 1, 1], [1, 1, 0], [1, 0, 1], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
)

configuration = np.array(
    [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [0, 2, 0], [0, 2, 1], [0, 2, 2],
     [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 2, 2]]
)[::-1]


# Convert rule to number in Wolfram notation
def rule_from_number(n):
    base = 3
    rule = np.zeros(19)
    i = -1
    while n > 1:
        res = n % base
        n = n // base
        rule[i] = res
        i -= 1
    rule[i] = n
    print(rule)
    return rule



def img_save(t, number, cells):
    plt.figure(figsize=(4, 4), dpi=300)
    plt.set_cmap('jet')
    ax = plt.axes([0, 0, 1, 1])
    plt.axis('off')
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    plt.imshow(cells[:, :])
    plt.savefig("step_{}_n{}.png".format(t, number), bbox_inches='tight', pad_inches=0)
    plt.close()


def automata_generate(rules, number):
    print('starting')
    # save starting configuration
    if save_every_step:
        img_save(0, number, cells)
    # generate every step
    for t in range(1, time):
        left = np.roll(cells[:, t - 1], 1)
        center = cells[:, t - 1]
        right = np.roll(cells[:, t - 1], -1)
        center = cells[:, t - 1]
        for n in range(size):
            # print(left[n], center[n], right[n])
            test = np.array([left[n], center[n], right[n]])
            for k, rule in enumerate(configuration):
                if all(rule == test):
                    cells[n, t] = rules[k]
                    break
        if save_every_step:
            img_save(t, number, cells)
    if not save_every_step:
        img_save(time, number, cells)

    print('finished')


rule_numbers = [1768]  # np.arange(1, 2*3**7+2*3**6+2*3**5+2*3**4+2*3**3+2*3**2+2*3**1+2)

for number in rule_numbers:
    rules = rule_from_number(number)
    automata_generate(rules, number)
print('all finished')
