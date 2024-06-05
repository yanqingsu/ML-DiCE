# Author: Arjun S Kulathuvayal. Intellectual property. Copyright strictly restricted
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os, re
from matminer.featurizers import composition as cf
from matminer.featurizers.base import MultipleFeaturizer
from matminer.featurizers.conversions import StrToComposition



class Featurization:
    def __init__(self):

        self.DE =3




