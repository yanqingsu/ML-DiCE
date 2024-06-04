import os
import argparse
import numpy as np
from mldice import __version__


def read_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("-de","--diffusingElement",dest="Diffusing Element",type=str, default='He', help="Atomic symbol of diffusing element")
    parser.add_argument("-dm","--diffusionMedium",dest="Diffusion Medium",type=str, default="Ni50Fe50", help="Diffusion medium with composition as percentages")
    parser.add_argument("-T","--temperature",dest="Temperature",type=float, default="500", help="Temperature of the diffusion process")
    parser.add_argument("-e","--estimator",dest="Estimator",type=str, default='RF', help="Testing estimator: 'RF' or 'DNN'")
    parser.add_argument("--version",dest="version",action="store_true", default=False, help="Display the version of ML-DiCE and stop")
    args = parser.parse_args()
    return args

def print_results():
    pass


def main():
    args = read_options()

    if args.version:
        print("ML-DiCE", __version__)
        return

    vgout = open("Prediction.md", "w")

    print("# ML-DiCE | Machine Learned Diffusion Coefficient Estimator\n", file=vgout)
    print("## Input Parameters:", file=vgout)
    print("|  Input Parameters   |    Value    |", file=vgout)
    print("|:-----------:|:-----------:|", file=vgout)
    for arg in vars(args):
        print(" | ", arg, "|", vars(args)[arg], " | ", file=vgout)
    print(file=vgout, flush=True)


main()
