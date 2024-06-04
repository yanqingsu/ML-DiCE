# Author: Arjun S Kulathuvayal. Intellectual property. Copyright strictly restricted
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os, re
from matminer.featurizers import composition as cf
from matminer.featurizers.base import MultipleFeaturizer
from matminer.featurizers.conversions import StrToComposition
import mendeleev

class Featurization:
    def __init__(self):

        self.DE =3


def is_valid_atomic_symbol(symbol):
    try:
        element = mendeleev.element(symbol)
        return True
    except ValueError:
        return False