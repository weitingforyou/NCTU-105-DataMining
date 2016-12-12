from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.regression import LinearRegressionWithSGD
from pyspark.mllib.tree import DecisionTree
import numpy as np
import math
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext

conf = SparkConf().setAppName("building a decision tree")
sc = SparkContext(conf=conf)

# read training file
train_raw_data = sc.textFile("train_character-deaths.csv")
train_num_data = train_raw_data.count()
train_records = train_raw_data.map(lambda x: x.split(","))
print train_num_data

# read testing file
test_raw_data = sc.textFile("test_character-deaths.csv")
test_num_data = test_raw_data.count()
test_records = test_raw_data.map(lambda x: x.split(","))
print test_num_data

# extract label and feature
# labels
def extract_label(record):
    return int(float(record[0]))
# features
def extract_features_dt(record):
    return np.array(map(int, record[1:28]))

train_data_dt = train_records.map(lambda r: LabeledPoint(extract_label(r), extract_features_dt(r)))
test_data_dt = test_records.map(lambda r: LabeledPoint(extract_label(r), extract_features_dt(r)))
train_first_point_dt = train_data_dt.first()
test_first_point_dt = test_data_dt.first()
print "Decision Tree training data feature vector length: " + str(len(train_first_point_dt.features))
print "Decision Tree testing data feature vector length: " + str(len(test_first_point_dt.features))


# Training Decision Tree
dt_model = DecisionTree.trainRegressor(train_data_dt, {})
print "Decision Tree depth: " + str(dt_model.depth())
print "Decision Tree number of nodes: " + str(dt_model.numNodes())

# predict
preds = dt_model.predict(test_data_dt.map(lambda p: p.features))
preds = preds.map(round, preds)
actuals = test_records.map(lambda r: extract_label(r))

pred = []
actual = []
for i in xrange(0, test_num_data):
    pred.append(preds.take(test_num_data)[i])
    actual.append(actuals.take(test_num_data)[i])

print "Decision Tree predictions: ", pred

# Precision Rate, Recall Rate, Accuracy
ConfusionMatrix = np.zeros(4, dtype=float)

# (TP, FP, FN, TN)
for i in xrange (0, len(pred)):
    if actual[i]==1 and pred[i]==1:
        ConfusionMatrix[0] = ConfusionMatrix[0] + 1
    elif actual[i]==0 and pred[i]==1:
        ConfusionMatrix[1] = ConfusionMatrix[1] + 1
    elif actual[i]==1 and pred[i]==0:
        ConfusionMatrix[2] = ConfusionMatrix[2] + 1
    else:
        ConfusionMatrix[3] = ConfusionMatrix[3] + 1

PrecisionRate = ConfusionMatrix[0] / (ConfusionMatrix[0] + ConfusionMatrix[1])
RecallRate = ConfusionMatrix[0] / (ConfusionMatrix[0] + ConfusionMatrix[2])
Accuracy = (ConfusionMatrix[0] + ConfusionMatrix[3]) / len(pred)

print 'Precision Rate:', PrecisionRate
print 'Recall Rate:', RecallRate
print 'Accuracy:', Accuracy

