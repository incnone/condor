from scipy.integrate import dblquad
import math
import numpy

def elo_prob(x):
    return 1/(1+10**(-x/400))

def binormal_dist(x1, x2, m1, m2, s1, s2, covar):
    corr = covar/(s1*s2)
    z = ((x1 - m1)**2)/(s1**2) - 2*corr*(x1-m1)*(x2-m2)/(s1*s2) + ((x2-m2)**2)/(s2**2)
    a = 1/(2*math.pi*s1*s2*math.sqrt(1-corr**2))
    return a*math.exp(-z/(2*(1 - corr**2)))

def integrand_30(x1, x2, m1, m2, s1, s2, covar):
    return (elo_prob(x1-x2))**3 * binormal_dist(x1, x2, m1, m2, s1, s2, covar)

def integrand_21(x1, x2, m1, m2, s1, s2, covar):
    prob = elo_prob(x1-x2)
    return 3*(prob**2)*(1-prob)*binormal_dist(x1, x2, m1, m2, s1, s2, covar)

def integrand_12(x1, x2, m1, m2, s1, s2, covar):
    prob = elo_prob(x1-x2)
    return 3*(prob)*((1-prob)**2)*binormal_dist(x1, x2, m1, m2, s1, s2, covar)

def integrand_03(x1, x2, m1, m2, s1, s2, covar):
    return (elo_prob(x2-x1))**3 * binormal_dist(x1, x2, m1, m2, s1, s2, covar)

def calc_probs(elo_p1, stdev_p1_squared, elo_p2, stdev_p2_squared, covar):
    stdev_p1 = math.sqrt(stdev_p1_squared)
    stdev_p2 = math.sqrt(stdev_p2_squared)
    lower_lim_1 = elo_p1 - 6*stdev_p1
    upper_lim_1 = elo_p1 + 6*stdev_p1
    lower_lim_2 = elo_p2 - 6*stdev_p2
    upper_lim_2 = elo_p2 + 6*stdev_p2
    r_val = []
    r_val.append(dblquad(lambda x1, x2: integrand_30(x1, x2, elo_p1, elo_p2, stdev_p1, stdev_p2, covar),
            lower_lim_2, upper_lim_2, lambda x: lower_lim_1, lambda x: upper_lim_1)[0])
    r_val.append(dblquad(lambda x1, x2: integrand_21(x1, x2, elo_p1, elo_p2, stdev_p1, stdev_p2, covar),
            lower_lim_2, upper_lim_2, lambda x: lower_lim_1, lambda x: upper_lim_1)[0])
    r_val.append(dblquad(lambda x1, x2: integrand_12(x1, x2, elo_p1, elo_p2, stdev_p1, stdev_p2, covar),
            lower_lim_2, upper_lim_2, lambda x: lower_lim_1, lambda x: upper_lim_1)[0])
    r_val.append(dblquad(lambda x1, x2: integrand_03(x1, x2, elo_p1, elo_p2, stdev_p1, stdev_p2, covar),
            lower_lim_2, upper_lim_2, lambda x: lower_lim_1, lambda x: upper_lim_1)[0])
    return r_val


if __name__ == "__main__":
    elo_data = open('elo2_data.txt', 'r')
    elo_output = open('elo2_results.txt', 'w')

    for line in elo_data:
        values = line.split('\t')
        elo_p1 = int(values[0])
        elo_p2 = int(values[1])
        stdev_p1_sq = int(values[2])
        stdev_p2_sq = int(values[3])
        covar = int(values[4])
        predicted_vals = calc_probs(elo_p1, stdev_p1_sq, elo_p2, stdev_p2_sq, covar)
        elo_output.write(str(predicted_vals[0]))
        elo_output.write('\t')
        elo_output.write(str(predicted_vals[1]))
        elo_output.write('\t')
        elo_output.write(str(predicted_vals[2]))
        elo_output.write('\t')
        elo_output.write(str(predicted_vals[3]))
        elo_output.write('\n')
