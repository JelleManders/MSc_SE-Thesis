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

def test(plot_title, Metric_data, VMAF_labels):
	# construct a ensemble regression tree
	ert = get_model()

	# evaluate the model
	scores, predictions = evaluate_model(ert, Metric_data, VMAF_labels)

	# summarize the performance
	print('>%s %.3f (%.3f)' % ("test", mean(scores), std(scores)))

	# Calculate the Pearson Coefficient of the predictions vs the VMAF labels
	pcc = str(corrcoef(VMAF_labels, predictions)[0,1])
	print("PCC: " + pcc)

	# Plot the predictions against the VMAF labels
	fig, ax = plt.subplots()
	ax.scatter(VMAF_labels, predictions)
	ax.set_xlabel("VMAF")
	ax.set_ylabel("ERT-LSB")
	plt.title(plot_title, loc='left')
	plt.title("PCC: " + pcc, loc='right')
	plt.show()

# def run_test_10s():
# 	data, labels = ds.data_10s()
# 	test("10s", data, labels)

# def run_test_5s():
# 	data, labels = ds.data_5s()
# 	test("5s", data, labels)
	
# def run_test_2s():
# 	data, labels = ds.data_2s()
# 	test("2s", data, labels)
	
# def run_test_1s():
# 	data, labels = ds.data_1s()
# 	test("1s", data, labels)
	
# run_test_10s()
# run_test_5s()
# run_test_2s()
# run_test_1s()

def run_test_10s_equalized():
	data, labels = ds.data_10s()
	eqdata, eqlabels = ds.equalize(data, labels)
	test("10s, equalized", eqdata, eqlabels)

def run_test_5s_equalized():
	data, labels = ds.data_5s()
	eqdata, eqlabels = ds.equalize(data, labels)
	test("5s, equalized", eqdata, eqlabels)
	
def run_test_2s_equalized():
	data, labels = ds.data_2s()
	eqdata, eqlabels = ds.equalize(data, labels)
	test("2s, equalized", eqdata, eqlabels)
	
def run_test_1s_equalized():
	data, labels = ds.data_1s()
	eqdata, eqlabels = ds.equalize(data, labels)
	test("1s, equalized", eqdata, eqlabels)
	
run_test_10s_equalized()
run_test_5s_equalized()
run_test_2s_equalized()
run_test_1s_equalized()