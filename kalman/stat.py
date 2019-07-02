import numpy as np
import matplotlib.pyplot as plt
from kalman_func import state_update, stat_model, stat_gain

mu = 50
sigma = 5
n = 1000

y = np.random.normal(mu, sigma, n)

# give rough initial guesses

loc = 60
uncert = 15 ** 2

est = np.array([])

for i in range(len(y)):

    loc_new, uncert_new = stat_model(loc, uncert)

    k = stat_gain(uncert_new, (sigma ** 2))

    loc, uncert = state_update(loc_new, uncert_new, k, y[i])

    est = np.append(est, loc)


true_val = np.full(n, 50)
y_ax = np.arange(1, n + 1)

plt.plot(y_ax, true_val, 'r', y_ax, y, 'b', y_ax, est, 'g')
plt.xlim(0, n + 1)
plt.ylim(mu - 10, mu + 10)
plt.show()
