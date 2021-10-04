# RADIOACTIVITY UNITS
rad_units = {'dps':1, 'dpm':1, 'Bq':1, 'kBq':1000, 'MBq':1000000, 'GBq':1000000000, 'uCi':4000, 'mCi':4000000, 'Ci':4000000000}

# IONIZING RADIATION UNITS

# The absorbed radiation dose
a_dose_units = {'Gy':1, 'rad':0.01, 'J/kg':1, 'mGy':0.001, 'uGy':0.000001, 'cGy':0.01}

# Exposure dose of radiation
e_dose_units = {'R':1, 'mR':0.001, 'uR':0.000001}

# Equivalent dose of radiation
eq_dose_units = {'Sv':1, 'Baer':0.01, 'mSv':0.001, 'uSv':0.000001}

def units_converter(units, n, in_unit, out_unit):
    base  = n*units[in_unit]
    print( base/units[out_unit], out_unit)

possible_values = {'radioactivity', 'absorbed radiation dose', 'exposure dose', 'equivalent dose'}

value = input('Choose the physical quantity: radioactivity / absorbed radiation dose / exposure dose / equivalent dose ')
while value not in possible_values:    
    print('I can not convert this, try again and choose one of the following options:')
    value = input('Choose the value: radioactivity / absorbed radiation dose / exposure dose / equivalent dose ')

if value == 'radioactivity':    
    units = rad_units
elif value == 'absorbed radiation dose':    
    units = a_dose_units
elif value == 'exposure dose':    
    units = e_dose_units
elif value == 'equivalent dose':    
    units = eq_dose_units

unit_list = '/'.join(i for i in units)

in_unit = input(f"What unit would you like to convert? Please, choose {unit_list} ")
while in_unit not in units:    
    in_unit = input(f'This is not the {value} unit. Please, try again. Choose from {unit_list} ')

n = int(input("Input the value: "))

out_unit = input(f"What unit would you like to get? Choose from {unit_list}  ")
while out_unit not in units:
    out_unit = input(f'This is not the {value} unit. Please, try again. Choose from {unit_list}  ')

units_converter(units, n, in_unit, out_unit)

