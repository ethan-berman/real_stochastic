import numpy as np

print("test")

M = 1
N = 1

states = []

# rx_const = np.zeros(M)
# mol_pop = np.zeros(N)
#C1...Cm = propensities
#X1...Xn = populations
mol_pop = np.asarray([1000, 0])
rx_const = np.asarray([0.6])

rxn_counter = 0
time = 0.0
end_time = 6.0
dt = 0.1

#if c is high, expect high drop off
c_val = []


while time < end_time:
    M = mol_pop * rx_const
    a = np.sum(M)
    print(a)
    r1 = np.random.uniform(0,1)
    r2 = np.random.uniform(0,1)
    tau = (1/a) * np.log(1/r1)
    mu = r2 * a
    print(mu)
    time += tau

#state * rate constant
def pick_reaction():
    pass
    #r1 = random number one
    #a0 
    #tau = 1/a0 ln(1/r1