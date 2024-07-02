# KDTree Interpolation for Methane Flamelet Data

This repository contains a Python script that performs KDTree interpolation on a 3D scattered dataset of flamelet gas properties. The dataset consists of 3 query and 5 output variables, provided in two CSV files for training and validation. The process includes scaling the inputs using `MinMaxScaler` and `QuantileTransformer`, applying KDTree interpolation, and generating R2 plots to compare the interpolated and reference values.

## Dataset

- `MethaneFlameletData_LUT.csv`: Training dataset containing the input query and output variables.
- `MethaneFlameletData_Validation.csv`: Validation dataset containing the input query variables for validation and reference output variables.

## Requirements

- Python 3.x
- NumPy
- Pandas
- SciPy
- Scikit-learn
- Matplotlib

You can install the required packages using:

```bash
pip install numpy pandas scipy sci-kit-learn matplotlib

## **Steps**

### **1\. Load the CSV Files**

Load the training and validation data from the provided CSV files. The training data contains the input query variables and output variables, while the validation data contains the input query variables for validation and the reference output variables.

### **2\. Define Query and Output Variables**

Specify the query variables and output variables:

- Query variables: ProgressVariable, EnthalpyTot, MixtureFraction
- Output variables: Temperature, MolarWeightMix, DiffusionCoefficient, Conductivity, ViscosityDyn

### **3\. Extract Query and Output Variables**

Extracted the query and output variables from the training data and extracted the query variables from the validation data.

### **4\. Scale the Input Variables**

Using MinMaxScaler to scale the input data to the range \[0, 1\]. Then, QuantileTransformer will be applied to transform the features to follow a uniform distribution. This scaling ensures that the query variables have a similar range, improving the KDTree algorithm's performance.

### **5\. Create a KDTree**

Created a KDTree from the scaled training data. KDTree is a data structure that allows for efficient nearest-neighbor searches, which is useful for interpolation.

### **6\. Define KDTree Interpolation Function**

Define a function to interpolate using KDTree. The function queries the KDTree to find the k-nearest neighbors for each validation point, applies inverse distance weighting to the neighbors' output values, and returns the interpolated values.

### **7\. Apply KDTree Interpolation**

Apply the KDTree-based interpolator to the scaled validation data to obtain interpolated output values for the validation queries.

### **8\. Calculate R-squared Scores**

Calculate the R-squared value for each output variable to quantify the fit between the interpolated and reference values. R-squared is a statistical measure that indicates how well the interpolated values approximate the reference values.

### **9\. Generate R2 Plots**

Create scatter plots of the interpolated temperatures against the reference temperatures. Add a line representing the ideal fit where interpolated values equal reference values. The plots visually show the correlation between the interpolated and reference values. You can also print the R-squared scores for all output variables.
![plot](
### **Generated Plots**

- **R2 Plot for Temperature**:

Replace path_to_generated_plot.png with the actual path to your generated plot image.

## **Conclusion**

This repository provides a method for performing KDTree interpolation on scaled 3D scattered datasets, with a focus on flamelet gas properties. The R2 plots and R-squared scores offer a quantitative and visual assessment of the interpolation performance.

Feel free to clone the repository, modify the script, and experiment with different datasets or interpolation methods.
