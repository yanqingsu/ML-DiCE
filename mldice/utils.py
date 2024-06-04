# Author: Arjun S Kulathuvayal. Intellectual property. Copyright strictly restricted
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.covariance import EmpiricalCovariance
from sklearn.preprocessing import StandardScaler
import bz2
import _pickle as cPickle
font = {'family': 'serif',
        'weight': 'normal',
        'size': 12}
plt.rc('font', **font)
plt.rcParams["figure.figsize"] = [8, 6]



def decompress(file):
  data = bz2.BZ2File(file, 'rb')
  data = cPickle.load(data)
  return data


def correlationHeatmap(df, title="", label=False):
    X = df.drop(['D', 'Temperature'], axis=1)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    covariance_estimator = EmpiricalCovariance()
    covariance_estimator.fit(X_scaled)
    correlation_matrix = covariance_estimator.covariance_
    # print(correlation_matrix)
    cor_mat = np.array(correlation_matrix)
    # correlation_matrix.to_csv('basic_features_correlation_matrix.csv', columns=df.columns.tolist(), index=df.columns.tolist())

    if label is True:
        sns.heatmap(cor_mat, annot=True, cmap='coolwarm', vmin=-1, vmax=1, xticklabels=X.columns, yticklabels=X.columns)
    else:
        sns.heatmap(cor_mat, annot=False, cmap='coolwarm', vmin=-1, vmax=1, xticklabels=range(1, len(X.columns)+1), yticklabels=X.columns.str.replace('_', ' '))
    plt.title(f'Correlation Heatmap of {title}', fontsize=14)
    plt.tick_params(direction="in")
    plt.tight_layout()
    plt.savefig(f'Corr_Heatmap_{title}.pdf')
    plt.savefig(f'Corr_Heatmap_{title}.png', dpi=150)
    plt.close()


if __name__ == "__main__":
    pass
