# Author: Arjun S Kulathuvayal. Intellectual property. Copyright strictly restricted
import pkg_resources

#from .featurization import initial_processing
from .validation import validator
from .training import rf_training, dnn_traning
from .utils import argCheck, clr
from importlib.metadata import version

#__version__ = pkg_resources.require("vaspgibbs")[0].version
__version__ = "0.0.1"