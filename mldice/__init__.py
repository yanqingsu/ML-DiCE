# Author: Arjun S Kulathuvayal. Intellectual property. Copyright strictly restricted
import pkg_resources

from .featurization import featurize_de, featurize_de
from .training import rf_training, dnn_traning
from importlib.metadata import version

#__version__ = pkg_resources.require("vaspgibbs")[0].version
__version__ = "0.0.1"