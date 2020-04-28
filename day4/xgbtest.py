# coding=utf-8
from numpy import loadtxt
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score
from xgboost import plot_importance
from matplotlib import pyplot

dataset = loadtxt('C:\\Users\cheyiwang\Desktop\part-00000', delimiter=",")
print(dataset)
X = dataset[:, 0:7]
Y = dataset[:, 7]

seed = 7
test_size = 0.33
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)

# 不可视化数据集loss
# model = XGBClassifier()
# model.fit(X_train, y_train)

##可视化测试集的loss
model = XGBClassifier()
eval_set = [(X_test, y_test)]
model.fit(X_train, y_train, early_stopping_rounds=100, eval_metric="logloss", eval_set=eval_set, verbose=True)
# 改为True就能可视化loss
model.save_model("00001.model")

model.fit(X, Y)
plot_importance(model)
pyplot.show()

y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]

accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))
##Accuracy: 77.56%

test_auc2 = roc_auc_score(y_test,y_pred)#验证集上的auc值
print ("xgb_muliclass_auc:",test_auc2)


