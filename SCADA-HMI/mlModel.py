import pandas as pd
import sklearn.model_selection
import xgboost as xgb
import numpy as np
import sklearn as skl

pdDf = pd.read_csv('learningDataNew.csv')
pdDf.head()


def splitDataFromCSV(dataFromCSV="learningDataNew.csv"):
    boost = np.loadtxt(dataFromCSV,delimiter=',',skiprows=1)

    X = boost[: , 0:6]
    Y = boost[: , 6:9]
    #6 i 9 su se najbolje pokazali
    # 9 daje najvecu preciznost 84
    # 6 daje malo manju 82
    # da li se isplati imati stablo dubine 9 ?
    model = xgb.XGBClassifier(random_state=42, max_depth=9, tree_method="hist", multi_strategy="multi_output_tree",n_estimators=100,nthread=5,learning_rate=0.32)
    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X,Y,test_size=0.35,random_state=39)

    model.fit(X_train,y_train)
    pred = model.predict(X_test)
    sci_pred = [value for value in pred]
    print(sci_pred)
    acc = sklearn.metrics.accuracy_score(y_test, sci_pred)
    print("Acc: %.2f%%" % (acc * 100.0))
    print(skl.metrics.mean_squared_error(y_test, pred))
    model.save_model('xgbNew.json')


def loadModel(data='xgb.json'):
    newModel = xgb.XGBClassifier()
    newModel.load_model(data)
    return newModel

splitDataFromCSV()



