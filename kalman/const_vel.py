import numpy as np
import matplotlib.pyplot as plt
from kalman_func import const_vel_model, const_vel_state_update, const_vel_gain

loc = 30000
vel = 40
delta = 5
sigma_mes = 500
n = 100
uncert_mes = sigma_mes ** 2
uncert_loc = sigma_mes ** 2
uncert_vel = sigma_mes ** 2

y = np.array([])
y1 = np.array([])

est = np.array([])
kgain = np.array([])
pred = np.array([])

for i in range(n):

    y = np.append(y, np.random.normal(loc + delta*vel*i, sigma_mes))
    y1 = np.append(y1, loc + delta*vel*i)

for i in range(n):

    loc_new, vel_new, uncert_loc_new, uncert_vel_new = const_vel_model(loc, vel, uncert_loc, uncert_vel, delta)

    k_loc, k_vel = const_vel_gain(uncert_loc_new, uncert_vel_new, uncert_mes, delta)

    loc, vel, uncert_loc, uncert_vel = const_vel_state_update(loc_new, vel_new, uncert_loc_new, uncert_vel_new, k_loc,
                                                              k_vel, y[i], delta)

    est = np.append(est, loc)
    kgain = np.append(kgain, k_loc)
    pred = np.append(pred, loc_new)

# plt.plot(y, 'r')
plt.plot(y1, 'g')
plt.plot(est, 'b-')
plt.plot(y, 'r.-')

plt.figure()

plt.plot(kgain, '*-', c='black')

plt.show()
