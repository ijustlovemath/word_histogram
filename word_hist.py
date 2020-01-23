import sys
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

word_list = [line.rstrip('\r\n') for line in sys.stdin.readlines()]

# Shamelessly taken from: https://stackoverflow.com/a/35603850

counts = Counter(word_list)

labels, values = zip(*counts.items())

# sort your values in descending order
indSort = np.argsort(values)[::-1]

# rearrange your data
labels = np.array(labels)[indSort]
values = np.array(values)[indSort]

indexes = np.arange(len(labels))

bar_width = 0.

plt.bar(indexes, values, width=0.8)

# add labels
plt.xticks(indexes + bar_width, labels, rotation=45)
plt.show()



