# Author: Arjun S Kulathuvayal. Intellectual property. Copyright strictly restricted
import pandas as pd
import bz2
from .predicting import Predictor
from .utils import clr
from matminer.featurizers import composition as compo
from matminer.featurizers.base import MultipleFeaturizer
from matminer.featurizers.conversions import StrToComposition
import re

def get_elements_in_in(dm):
    cleaned_string = re.sub(r'[0-9.]+', '', str(dm))
    elements = []
    i = 0
    while i < len(cleaned_string):
        if i + 1 < len(cleaned_string) and cleaned_string[i + 1].islower():
            elements.append(cleaned_string[i:i + 2])
            i += 2
        else:
            elements.append(cleaned_string[i])
            i += 1
    return elements


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
        if i == 0:
            featurized_data.rename(columns=lambda x: 'DE' + x, inplace=True)
            featurized_data = featurized_data.rename(columns=lambda x: x.replace("MagpieData", ''))
            featurized_data.columns = featurized_data.columns.str.replace(' ', '_')
        else:
            featurized_data.rename(columns=lambda x: 'DM' + x, inplace=True)
            featurized_data = featurized_data.rename(columns=lambda x: x.replace("MagpieData", ''))
            featurized_data.columns = featurized_data.columns.str.replace(' ', '_')
        train_data.append(featurized_data)

    return train_data[0], train_data[1]



class ModelTester:
    def __init__(self, input_params, root):
        self.de = input_params.DE
        self.dm = input_params.DM
        self.temp = input_params.temperature
        self.mech = input_params.mechanism
        self.esti = input_params.estimator
        self.root = root

    def process(self):
        type_of_medium = get_elements_in_in(self.dm)
        de_features, dm_features = featurize(self.de, self.dm)
        if self.esti == "RF":
            predict = Predictor(de_features, dm_features, self.mech, type_of_medium, self.temp, self.root)
            return predict.RF_pred()
        elif self.esti == "DNN":
            predict = Predictor(de_features, dm_features, self.mech, type_of_medium, self.temp, self.root)
            return predict.DNN_pred()
        else:
            print(clr.RED + "Error!!!" + clr.GREEN + "Invalid model type provided." + clr.END)
