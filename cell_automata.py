import matplotlib.pyplot as plt
import numpy as np

time = 600
size = 600
base = 5
save_every_step = False

# creating empty world x-axis = space size, y-axis time
cells = np.zeros((size, time), dtype=np.int32)


# random starting configuration
def random_start():
    return np.random.randint(0, base, size)
cells[:, 0] = random_start()


# Convert rule to number in Wolfram notation
def rule_from_number(n, base, length):
    rule = np.zeros(length)
    i = -1
    while n > (base - 1):
        res = n % base
        n = n // base
        rule[i] = res
        i -= 1
    rule[i] = n
    return rule


# create all possibpe position variations for given base
configurations = []
for k in range(base ** 3):
    configurations.append(rule_from_number(k, base, 3))

configurations = np.array(configurations[::-1])
# print(configurations)
print('number of possible rules: {}'.format(base ** (base ** 3)))

def img_save(t, number, cells):
    plt.figure(figsize=(5, 5), dpi=300)
    plt.set_cmap('jet')
    ax = plt.axes([0, 0, 1, 1])
    plt.axis('off')
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    plt.imshow(cells[:, :])
    plt.savefig("step_{}_n{}.png".format(t, number), bbox_inches='tight', pad_inches=0)
    plt.close()


def automata_generate(rules, number):
    print('starting rule'.format(rules))
    # save starting configuration
    if save_every_step:
        img_save(0, number, cells)
    # generate every step
    for t in range(1, time):
        left = np.roll(cells[:, t - 1], 1)
        right = np.roll(cells[:, t - 1], -1)
        center = cells[:, t - 1]
        for n in range(size):
            # print(left[n], center[n], right[n])
            test = np.array([left[n], center[n], right[n]])
            for k, rule in enumerate(configurations):
                if all(rule == test):
                    cells[n, t] = rules[k]
                    break
        if save_every_step:
            img_save(t, number, cells)
    if not save_every_step:
        img_save(time, number, cells)
    print('finished')


# how many different rules to try?
rule_numbers = [32984747330028382193832345567771234334459484371]  #np.arange(1, 200)

for number in rule_numbers:
    rules = rule_from_number(number, base, base **3)
    automata_generate(rules, number)
print('all finished')
