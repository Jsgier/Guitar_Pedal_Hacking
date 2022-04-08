import numpy as np
from matplotlib import pyplot as plt


#organize parameters as a dictionary
#these are default values to be replaced with calculation
params = {
        'rin': 10E6,#input impedance of guitar pickup
        'c_dcb': 10E-9, #DC blocking capacitor 
        'r1b': 10E3, #r1 in divider bias network
        'r2b': 10E3, #r2 in divider bias network
        'rf' : 1E3, #rf in non inverting amplifier
        'rg' : 1E3, #rg in non inverting amplifier
        'raa' : 50, #antialiasing filter resistor
        'caa' : 1E-9 #antialiasing filter capacitor
        }

#--Calculations for determining component values--

#- Constants
fc_hpf = 100 #dc blocking capacitor filter cutoff frequency [Hz]
vin = 300E-3 #input voltage Vpk
vout = 1.2 #desired output voltage Vpk

#- Functions

def R_parallel(r1,r2): return r1*r2 / (r1 + r2)
def calc_r2(vs, vb, r1): return r1 / ((vs/vb)-1) #rs - source voltage, rb - divider output
def wc(r1,r2,cdcb): return 1 / (2*np.pi * R_parallel(r1,r2) * cdcb)
def calc_dcb(r1,r2,fc): return 1 / (2*np.pi * R_parallel(r1,r2) * fc)
def calc_gain(rf,rg): return 1 + rf / rg
def calc_rg(gain, rf): return rf / (gain - 1) 
def calc_c_lpf(fc, r): return 1 / (2*np.pi*fc*r)

#- Calculations
params['r2b'] = calc_r2(vs = 5, vb = 1.65, params['r1b']) #calculate r2 for bias network
params['c_dcb'] = calc_dcb(params['r1b'], params['r2b'], fc_hpf) #calculate dc blocking cap for fc
params['rg'] = calc_rg(gain = vout / vin, rf = params['rf']) #calculate gain resistor for amp
params['caa'] = calc_c_lpf(fc = 50E3, params['raa']) #calculate antialiasing filter capacitor value


#open file and write parameters
#print results to terminal
with open('line_amp.txt', 'w') as f:
    for parameter in params:
        f.write(f'.param {parameter} {params[parameter]:.2e}\n')
        print(f'.param {parameter} {params[parameter]:.2e}')
