# Author: Arjun S Kulathuvayal. Intellectual property. Copyright strictly restricted
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os, re
from sklearn.preprocessing import StandardScaler
from .utils import clr
font = {'family': 'serif',
        'weight': 'normal',
        'size': 12}
plt.rc('font', **font)
plt.rcParams["figure.figsize"] = [8, 6]
import _pickle as cPickle


class Predictor:
    def __init__(self, de_features, dm_features, mech, type_of_medium, temp, root):
        self.de_ftrs = de_features
        self.dm_ftrs = dm_features
        self.d_mode = mech
        self.medium_type = type_of_medium
        self.temp= temp
        self.root = root
        pass


    def RF_pred(self):
        if len(self.medium_type) == 1:
            if self.d_mode == 'impurity':
                medium_type = "IM"
                predict_df = feature_processing(medium_type, self.root, self.d_mode, self.temp, self.de_ftrs, self.dm_ftrs)
                model = decompress(self.root, self.d_mode, medium_type, algorithm='RF')
                preds = model.predict(predict_df.to_numpy())
                return np.exp(-preds)[0]
            elif self.d_mode == 'self':
                medium_type = "IM"
                predict_df = feature_processing(medium_type, self.root, self.d_mode, self.temp, self.de_ftrs, self.dm_ftrs)
                model = decompress(self.root, self.d_mode, medium_type, algorithm='RF')
                preds = model.predict(predict_df.to_numpy())
                return np.exp(-preds)[0]
            else:
                print(clr.YELLOW + "Warning!!" + clr.GREEN + "For impure metalic medium, presently we have trained impurity and self diffusion mechanism models. MOre diffusion mechanisms will be available in future")
                return False
        else:
            if self.d_mode == 'impurity' or self.d_mode == 'self':
                print(clr.YELLOW + "Warning!!" + clr.GREEN + " For impure metalic medium, training has done with MLPregressor")
                print(clr.YELLOW + "Warning!!" + clr.GREEN + " Redirecting to predicting with neural network model")
                result = self.DNN_pred()
                return result
            elif self.d_mode == 'chemical':
                medium_type = "MCA"
                predict_df = feature_processing(medium_type, self.root, self.d_mode, self.temp, self.de_ftrs, self.dm_ftrs)
                model = decompress(self.root, self.d_mode, medium_type, algorithm='RF')
                preds = model.predict(predict_df.to_numpy())
                return np.exp(-preds)[0]
            else:
                print(clr.YELLOW + "Error!!" + clr.GREEN + "For impure metalic medium, presently we have trained impurity, self, amd chemical diffusion mechanism models. MOre diffusion mechanisms will be available in future")
                return False

    def DNN_pred(self):
        if len(self.medium_type) == 1:
            if self.d_mode == 'impurity':
                medium_type = "IM"
                predict_df = feature_processing(medium_type, self.root, self.d_mode, self.temp, self.de_ftrs, self.dm_ftrs)
                predict_df = predict_df.to_numpy()
                scaled_pr_df = StandardScaler().fit_transform(predict_df)
                model = decompress(self.root, self.d_mode, medium_type, algorithm='DNN')
                preds = model.predict(scaled_pr_df)
                return np.exp(-preds)[0]
            elif self.d_mode == 'self':
                medium_type = "IM"
                predict_df = feature_processing(medium_type, self.root, self.d_mode, self.temp, self.de_ftrs, self.dm_ftrs)
                predict_df = predict_df.to_numpy()
                scaled_pr_df = StandardScaler().fit_transform(predict_df)
                model = decompress(self.root, self.d_mode, medium_type, algorithm='DNN')
                preds = model.predict(scaled_pr_df)
                return np.exp(-preds)[0]
            else:
                print(clr.YELLOW + "Warning!!" + clr.GREEN + "For impure metalic medium, presently we have trained impurity and self diffusion mechanism models. More diffusion mechanisms will be available in future")
                return False
        else:
            if self.d_mode == 'impurity':
                medium_type = "MCA"
                predict_df = feature_processing(medium_type, self.root, self.d_mode, self.temp, self.de_ftrs, self.dm_ftrs)
                predict_df = predict_df.to_numpy()
                scaled_pr_df = StandardScaler().fit_transform(predict_df)
                model = decompress(self.root, self.d_mode, medium_type, algorithm='DNN')
                preds = model.predict(scaled_pr_df)
                return np.exp(-preds)[0]
            elif self.d_mode == 'self':
                medium_type = "MCA"
                predict_df = feature_processing(medium_type, self.root, self.d_mode, self.temp, self.de_ftrs, self.dm_ftrs)
                predict_df = predict_df.to_numpy()
                scaled_pr_df = StandardScaler().fit_transform(predict_df)
                model = decompress(self.root, self.d_mode, medium_type, algorithm='DNN')
                preds = model.predict(scaled_pr_df)
                return np.exp(-preds)[0]
            elif self.d_mode == 'chemical':
                medium_type = "MCA"
                predict_df = feature_processing(medium_type, self.root, self.d_mode, self.temp, self.de_ftrs, self.dm_ftrs)
                model = decompress(self.root, self.d_mode, medium_type, algorithm='DNN')
                predict_df = predict_df.to_numpy()
                scaled_pr_df = StandardScaler().fit_transform(predict_df)
                preds = model.predict(scaled_pr_df)
                return np.exp(-preds)[0]
            else:
                print(clr.YELLOW + "Error!!" + clr.GREEN + "For impure metalic medium, presently we have trained impurity, self, amd chemical diffusion mechanism models. More diffusion mechanisms will be available in future")
                return False


def feature_processing(medium_type, root, d_mode, temp, de_ftrs, dm_ftrs):
    featureSpace = pd.read_csv(f'{root}/models/RF/featureSpace.csv', usecols=[f'{medium_type}_{d_mode}']).dropna() #change if models of RF and DNN have trained with different kind of feature spaces
    de_df = featureSpace[featureSpace[f'{medium_type}_{d_mode}'].str.startswith('DE')]
    dm_df = featureSpace[featureSpace[f'{medium_type}_{d_mode}'].str.startswith('DM')]
    de_trained_features = de_df[f'{medium_type}_{d_mode}'].to_list()
    dm_trained_features = dm_df[f'{medium_type}_{d_mode}'].to_list()

    de_ftrs = de_ftrs[de_trained_features]
    dm_ftrs = dm_ftrs[dm_trained_features]
    temp_df = pd.DataFrame(data=[temp], columns=['Temperature'])
    test_df = pd.concat([de_ftrs, dm_ftrs, temp_df], axis=1)

    return test_df


def decompress(root, d_mode, medium_type, algorithm):
    with open(f'{root}/models/{algorithm}/{medium_type}_{d_mode}/{algorithm}_model', 'rb') as f:
        model = cPickle.load(f)
    return model


if __name__ == "__main__":
    pass
