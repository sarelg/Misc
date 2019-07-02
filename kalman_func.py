def const_vel_model(loc, vel, uncert_loc, uncert_vel, delta):

    loc_new = loc + delta*vel
    vel_new = vel

    uncert_loc_new = uncert_loc + delta*uncert_vel
    uncert_vel_new = uncert_vel

    return loc_new, vel_new, uncert_loc_new, uncert_vel_new


def const_vel_gain(uncert_loc_new, uncert_vel_new, uncert_mes, delta):

    k_loc = uncert_loc_new / (uncert_loc_new + uncert_mes)

    k_vel = uncert_vel_new / (uncert_vel_new + (uncert_mes / (delta ** 2)))

    return k_loc, k_vel


def const_vel_state_update(loc_new, vel_new, uncert_loc_new, uncert_vel_new, k_loc, k_vel, y, delta):

    loc = loc_new + k_loc*(y - loc_new)
    vel = vel_new + k_vel*((y - loc_new)/delta)

    uncert_loc = (1 - k_loc)*uncert_loc_new
    uncert_vel = (1 - k_vel)*uncert_vel_new

    return loc, vel, uncert_loc, uncert_vel


def stat_model(loc, uncert):

    loc_new = loc
    uncert_new = uncert

    return loc_new, uncert_new


def stat_gain(uncert_new, uncert_mes):

    k = uncert_new/(uncert_new + uncert_mes)

    return k


def state_update(loc_new, uncert_new, k, y):

    loc = loc_new + k*(y - loc_new)
    uncert = (1 - k)*uncert_new

    return loc, uncert
