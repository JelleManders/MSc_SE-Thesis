# Number of models: 500 
# Number of branches: >15
# Learning Rate: 0.01

# explore random forest number of trees effect on performance
from numpy import mean
from numpy import std
from sklearn.datasets import make_regression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold
from sklearn.ensemble import RandomForestRegressor
# from matplotlib import pyplot

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
	return scores

# define dataset
X, y = ds.data_ref()

# construct a ensemble regression tree
ert = get_model()

# evaluate the model
scores = evaluate_model(ert, X, y)

# summarize the performance
print('>%s %.3f (%.3f)' % ("test", mean(scores), std(scores)))
