# Number of models: 500 
# Number of branches: >15
# Learning Rate: 0.01

# explore random forest number of trees effect on performance
from numpy import mean, std, corrcoef
from sklearn.datasets import make_regression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold
from sklearn.model_selection import cross_val_predict
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

import DataSets as ds

N_MODELS = 500

# get the dataset
def get_dataset():
	X, y = make_regression(n_samples=1000, n_features=20, n_informative=15, noise=0.1, random_state=2)
	return X, y

# get a list of models to evaluate
def get_model():
	return RandomForestRegressor(n_estimators = N_MODELS)
 
# evaluate a given model using cross-validation
def evaluate_model(model, X, y):
	# define the evaluation procedure
	cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)
	# evaluate the model and collect the results
	scores = cross_val_score(model, X, y, scoring='neg_mean_squared_error', cv=cv, n_jobs=-1, error_score='raise')
	predictions = cross_val_predict(model, X, y)
	return scores, predictions

# define dataset
Metric_data, VMAF_labels = ds.data_10s()

# construct a ensemble regression tree
ert = get_model()

# evaluate the model
scores, predictions = evaluate_model(ert, Metric_data, VMAF_labels)

# summarize the performance
print('>%s %.3f (%.3f)' % ("test", mean(scores), std(scores)))

# Calculate the Pearson Coefficient of the predictions vs the VMAF labels
print("PCC: " + str(corrcoef(VMAF_labels, predictions)[0,1]))

# Plot the predictions against the VMAF labels
fig, ax = plt.subplots()
ax.scatter(VMAF_labels, predictions)
ax.set_xlabel("VMAF")
ax.set_ylabel("ERT-LSB")
plt.show()