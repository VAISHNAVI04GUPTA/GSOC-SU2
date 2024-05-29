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

density = data['Density'].values[0:1000]
energy = data['Energy'].values[0:1000]
entropy = data['s'].values[0:1000]

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

x=standardized_density
y=standardized_energy
z=true_entropy_values
z1=interpolated_entropy_values_rbf
fig, ax = plt.subplots( figsize = (18,12))
jet=plt.get_cmap('coolwarm')
plt.scatter(x, y, s=100, c=z, cmap=jet, vmin=0, vmax=1)
plt.scatter(x,y, s=100, c=z1, cmap=jet, vmin=0, vmax=1)
ax.set_xlabel('density')
ax.set_ylabel('energy')
ax.set_title('Scatter chart, third variable as gradient', size = 14)
plt.show()