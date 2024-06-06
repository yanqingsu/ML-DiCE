# Author: Arjun S Kulathuvayal. Intellectual property. Copyright strictly restricted
import numpy as np
import pandas as pd
import warnings
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


class clr:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'


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


def argCheck(input_params):
    try:
        if input_params.DE is None:
            raise ValueError(clr.RED + "Error!!!" + clr.GREEN + " Enter diffusing element as '-de' or '--diffusingElement' | required and cannot be empty." + clr.END)
        elif input_params.DM is None or input_params.DM == "A50B25C15D10":
            raise ValueError(clr.RED + "Error!!!" + clr.GREEN + " Enter diffusion medium as '-dm' or '--diffusionMedium' | required and cannot be empty." + clr.END)
        elif input_params.temperature is None:
            raise ValueError(clr.RED + "Error!!" + clr.GREEN + " Enter Temperature as '-t' or '--Temperature' | required and cannot be empty." + clr.END)
        elif input_params.temperature > 2000 or input_params.temperature < 500:
            print(clr.YELLOW + "Warning!!" + clr.GREEN + " Model performs optimally for the temperature range of 500 to 2000 K" + clr.END)
        elif input_params.estimator is None:
            raise ValueError(clr.RED + "Error!!!" + clr.GREEN + " Enter mechanism of diffusion as '-m' or '--mechanism' | required and cannot be empty." + clr.END)
        return True
    except ValueError as err:
        print(err)
    except UserWarning as wa:
        print(wa)
    return False

