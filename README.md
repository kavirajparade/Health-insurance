
Health Insurance Charges Prediction

This project uses a Linear Regression model to predict health insurance charges based on several factors such as age, BMI, number of children, gender, and smoking status.

Dataset
The dataset includes the following columns:

age: Age of the individual.
sex: Gender of the individual (1 for female, 0 for male).
bmi: Body Mass Index.
children: Number of children covered under the insurance plan.
smoker: Smoking status (1 for smoker, 0 for non-smoker).
region: Geographical region (not used in the model).
charges: Medical charges billed by health insurance.

Data Preprocessing
The sex column was encoded to 1 for female and 0 for male.
The smoker column was encoded to 1 for smoker and 0 for non-smoker.
Features for model training: ['age', 'bmi', 'children', 'sex', 'smoker'].
Target variable: charges.
Model
The project employs Linear Regression from the sklearn library for predicting insurance charges.

Requirements
Python 3.7 or later
Libraries:
pandas
numpy
scikit-learn
