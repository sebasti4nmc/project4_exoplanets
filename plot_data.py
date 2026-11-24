import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('mystery_system.csv')
data.columns = data.columns.str.strip().str.lstrip('#').str.strip()
print(data.head())
uncertainty = data['sigma_ms']

plt.figure(figsize=(8, 4.5))
#plt.plot(data['t_days'], data['v_ms'], marker='o', linestyle='-', markersize=4)
plt.errorbar(data['t_days'], data['v_ms'], yerr=uncertainty, fmt='o', markersize=4)
plt.xlabel('Time [days]')
plt.ylabel('Stellar radial velocity [m/s]')
plt.title('Radial velocity of target star')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
plt.close()