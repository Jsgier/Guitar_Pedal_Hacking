import numpy as np
from matplotlib import pyplot as plt


#organize parameters as a dictionary
#these are default values to be replaced with calculation
line_amp_params = {
        'rin': 10E6, #input impedance of guitar pickup
        'c_dcb': 10E-9, #DC blocking capacitor, 
        'r1b': 10E3, #r1 in divider bias network
        'r2b': 10E3 #r2 in divider bias network
        }

#--Calculations for determining component values--

#- Constants
fc_hpf = 100 #dc blocking capacitor filter cutoff frequency [Hz]

#- Functions


#- Calculations


line_amp_params['c_dcb'] = 


#open file and write parameters:
with open('line_amp.txt', 'w') as f:
    for parameter in line_amp_params:
        f.write(f'.param {parameter} {line_amp_params[parameter]}\n')