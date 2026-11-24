import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

PI = np.pi

def get_data(file):
    data = pd.read_csv(file)
    data.columns = data.columns.str.strip().str.lstrip('#').str.strip()

    # Make dataframe
    dataframe = pd.DataFrame(data)
    T_max = dataframe['t_days'].max()
    N = len(dataframe)
    v_centered = dataframe['v_ms'] - dataframe['v_ms'].mean()

    # Velocity and time data
    d = (v_centered).to_numpy()
    t = (dataframe['t_days']).to_numpy()

    # Set frequencies
    df = 1.0 / (4.0 * T_max)
    f_min = 1.0 / (2.0 * T_max)
    f_max = 1.0 / 4.0
    f = np.arange(f_min, f_max + df, df)

    return d, t, f


def construct_g(f, t):
    n, m = len(t), len(f)
    G = np.zeros((n, 2*m))

    for i in range(n):
        for j in range(m):
                print(i,j)
                G[i, 2*j] = np.cos(2 * PI * f[j]* t[i])
                G[i, 2*j +1] = np.sin(2 * PI * f[j] * t[i])

    return G


def main():
    # frequencies = np.zeros(4)
    # times = np.zeros(4)

    # G = construct_g(frequencies, times)
    # print(G)
    # open('mystery_system.csv', mode='r')

if __name__ == "__main__":
    main()