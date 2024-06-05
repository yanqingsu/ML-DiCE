# Author: Arjun S Kulathuvayal. Intellectual property. Copyright strictly restricted
import pandas as pd
import bz2
import _pickle as cPickle
from .utils import clr
from matminer.featurizers import composition as compo
from matminer.featurizers.base import MultipleFeaturizer
from matminer.featurizers.conversions import StrToComposition


def featurize(de, dm):
    train_data = []
    for i, chemSpecies in enumerate([de, dm]):
        print(clr.BLUE + "Info!" + clr.GREEN + f" Featurizing {'Diffusing element' if i == 0 else 'Diffusion Medium' if i == 1 else 'Other'}" + clr.END)
        data = pd.DataFrame(data=[chemSpecies], columns=['chemical_species'])
        data = StrToComposition(target_col_id='target_chem_species').featurize_dataframe(data, 'chemical_species')
        feature_calculators = MultipleFeaturizer(
            [compo.Stoichiometry(), compo.ElementProperty.from_preset("magpie"), compo.ValenceOrbital(props=['avg']),
             compo.IonProperty(fast=True)])
        featurized_data = feature_calculators.featurize_dataframe(data, col_id='target_chem_species', ignore_errors=True)
        featurized_data = featurized_data.drop(columns=['target_chem_species'])
        train_data.append(featurized_data)
    return train_data[0], train_data[1]


def RF_test(de_ftrs, dm_ftrs, d_mode):
    print("Training with Random Forest...")


def DNN_test(de_ftrs, dm_ftrs, d_mode):
    print("Training with Deep Neural Network...")


def decompress(file):
  data = bz2.BZ2File(file, 'rb')
  data = cPickle.load(data)
  return data

class ModelTrainer:
    def __init__(self, input_params):
        self.de = input_params.DE
        self.dm = input_params.DM
        self.temp = input_params.temperature
        self.mech = input_params.mechanism
        self.esti = input_params.estimator

    def process(self):
        de_features, dm_features = featurize(self.de, self.dm)
        if self.esti == "RF":
            RF_test(de_features, dm_features, self.mech)
        elif self.esti == "DNN":
            DNN_test(de_features, dm_features, self.mech)
        else:
            print(clr.RED + "Error!!!" + clr.GREEN + "Invalid model type provided." + clr.END)
