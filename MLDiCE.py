import os
import argparse
import numpy as np
from mldice import __version__, argCheck, clr, validator



def read_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("-de", "--diffusingElement",dest="DE",type=str, default='X', help="Atomic symbol of diffusing element")
    parser.add_argument("-dm", "--diffusionMedium",dest="DM",type=str, default="A50B25C15D10", help="Diffusion medium with composition as percentages")
    parser.add_argument("-T", "--temperature",dest="temperature",type=float, default=500, help="Temperature of the diffusion process")
    parser.add_argument("-m", "--mechanism", dest="mechanism", type=str, default='self', help="mechanism of diffusion")
    parser.add_argument("-e", "--estimator",dest="estimator",type=str, default='RF', help="Testing estimator: 'RF' or 'DNN'")
    parser.add_argument("-v", "--version", dest="version",action="store_true", default=False, help="Display the version of ML-DiCE and stop")
    args = parser.parse_args()
    return args


def main():
    args = read_options()

    if args.version:
        print("ML-DiCE", __version__)
        return

    if argCheck(args):
        if args.estimator is None or args.estimator == "RF":
            print(clr.BLUE + "Info!" + clr.GREEN +" Random Forest is chosen as the default estimator. This can be changed to MLPRegressor as '-e' or '--estimator'" + clr.END)
        validator(args)
    else:
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
