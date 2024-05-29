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

density = data['Density'].values[0:10000]
energy = data['Energy'].values[0:10000]
entropy = data['s'].values[0:10000]

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

validation_points1 = validation_data[['Density', 'Energy']].values[0:1000]
true_entropy_values1 = validation_data['s'].values[0:1000].reshape(-1,1)

scaler.fit(validation_points1)
validation_points = scaler.transform(validation_points1)

scaler.fit(true_entropy_values1)
true_entropy_values = scaler.transform(true_entropy_values1)
# Create the Rbf interpolator
rbf_interpolator = Rbf(standardized_density, standardized_energy, standardized_entropy, function='multiquadric')
# Perform the interpolation
interpolated_entropy_values_rbf = rbf_interpolator(validation_points[:, 0], validation_points[:, 1])
#print(interpolated_entropy_values_rbf)
# Calculate accuracy metrics
mae_rbf = mean_absolute_error(true_entropy_values, interpolated_entropy_values_rbf)
mse_rbf = mean_squared_error(true_entropy_values, interpolated_entropy_values_rbf)
rmse_rbf = np.sqrt(mse_rbf)

print("Validation Results for Rbf Interpolation:")
print(f"Mean Absolute Error (MAE): {mae_rbf}")
print(f"Mean Squared Error (MSE): {mse_rbf}")
print(f"Root Mean Squared Error (RMSE): {rmse_rbf}")

fig = plt.figure(figsize=(18, 12))
ax = fig.add_subplot(111)
ax.scatter(validation_points[:, 0], validation_points[:, 1], c=interpolated_entropy_values_rbf,  marker='o', label='Interpolated')
ax.scatter(validation_points[:, 0], validation_points[:, 1], c=true_entropy_values,  marker='^', label='True')
ax.set_xlabel('Density(kg/m^3)')
ax.set_ylabel('Energy(kJ)')
#ax.set_zlabel('Entropy')
ax.set_title('RBF Interpolation')
plt.errorbar(validation_points[:, 0], validation_points[:, 1], yerr=interpolated_entropy_values_rbf, fmt="o")

plt.legend(loc='upper left')
plt.tight_layout()
plt.show()