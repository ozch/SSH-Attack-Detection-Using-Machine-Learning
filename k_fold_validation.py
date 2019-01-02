from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import KFold

class KFoldValidation():
    def GetAverageScore(self,n,features,label,model,X_train):
        kf = KFold(n_splits=n, random_state=None, shuffle=True)
        X = features
        y = label

        train_acc = 0.0
        test_acc = 0.0
        for train_i, test_i in kf.split(X_train):
            # print("TRAIN:", train_i, "TEST:", test_i)
            xtrain, xtest = X[train_i], X[test_i]
            ytrain, ytest = y[train_i], y[test_i]
            model.fit(xtrain, ytrain)
            train_acc = train_acc + model.score(xtrain, ytrain)
            test_acc = test_acc + model.score(xtest, ytest)
            print("Train Accuracy : " + str(model.score(xtrain, ytrain)))
            print("Test Accuracy : " + str(model.score(xtest, ytest)))

        print("Average Train Accuracy : " + str(train_acc / 10))
        print("Average Test Accuracy : " + str(test_acc / 10))