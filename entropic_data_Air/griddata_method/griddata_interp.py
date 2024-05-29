import numpy as np
import pandas as pd
from scipy.interpolate import griddata,Rbf
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import MaxAbsScaler


lut_file = 'entropic_data_Air_LUT.csv'
data = pd.read_csv(lut_file)

validation_file = 'entropic_data_Air_Validation.csv'
validation_data = pd.read_csv(validation_file)

density = data['Density'].values
energy = data['Energy'].values
entropy = data['s'].values

density1=density.reshape(-1,1)
energy1 = energy.reshape(-1,1)
entropy1 = entropy.reshape(-1,1)

scaler = MaxAbsScaler()
scaler.fit(density1)
standardized_density = scaler.transform(density1)
scaler.fit(energy1)
standardized_energy = scaler.transform(energy1)
scaler.fit(entropy1)
standardized_entropy = scaler.transform(entropy1)

points = np.array([density, energy]).T
scaler.fit(points)
standardized_data = scaler.transform(points)

validation_points1 = validation_data[['Density', 'Energy']].values
true_entropy_values1 = validation_data['s'].values.reshape(-1,1)

scaler.fit(validation_points1)
validation_points = scaler.transform(validation_points1)

scaler.fit(true_entropy_values1)
true_entropy_values = scaler.transform(true_entropy_values1)

methods = ['linear','cubic','nearest']

for i, method in enumerate(methods, 1):
    interpolated_entropy_values = griddata(standardized_data, standardized_entropy, validation_points, method='linear')
    reshaped_interpolated_entropy_values=interpolated_entropy_values.reshape(-1,1)
    scaler.fit(reshaped_interpolated_entropy_values)
    scaled_interpolated=scaler.transform(reshaped_interpolated_entropy_values)

    fig = plt.figure(figsize=(18, 12))
    ax = fig.add_subplot(2, 2, i, projection='3d')
    ax.scatter(validation_points[:, 0], validation_points[:, 1], scaled_interpolated, c='r', marker='o', label='Interpolated')
    ax.scatter(validation_points[:, 0], validation_points[:, 1], true_entropy_values, c='b', marker='^', label='True')
    ax.set_xlabel('Density (kg/m^3)')
    ax.set_ylabel('Energy (kJ)')
    ax.set_zlabel('Entropy')
    ax.set_title(f'{method} Interpolation')
    ax.legend()
    plt.tight_layout()
    plt.show()

#plt.savefig('interpolation_results.png')