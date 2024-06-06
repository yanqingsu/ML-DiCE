import os
import argparse
from .featurization import ModelTester
from .validation import validator, entry_err
from .utils import argCheck, clr
import pkg_resources
version = pkg_resources.require("mldice")[0].version

def read_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("-de", "--diffusingElement",dest="DE",type=str, default="", help="Atomic symbol of diffusing element")
    parser.add_argument("-dm", "--diffusionMedium",dest="DM",type=str, default="", help="Diffusion medium with composition as percentages")
    parser.add_argument("-t", "--temperature",dest="temperature",type=float, default="5", help="Temperature of the diffusion process")
    parser.add_argument("-m", "--mechanism", dest="mechanism", type=str, default="", help="mechanism of diffusion")
    parser.add_argument("-e", "--estimator",dest="estimator",type=str, default='RF', help="Testing estimator: 'RF' or 'DNN'")
    parser.add_argument("-v", "--version", dest="version",action="store_true", default=False, help="Display the version of ML-DiCE and stop")
    args = parser.parse_args()
    return args


def MLDiCE():
    project_root = os.path.dirname(os.path.abspath(__file__))
    vgout = open("Prediction.md", "w")
    print("# ML-DiCE | Machine Learned Diffusion Coefficient Estimator\n", file=vgout)

    args = read_options()
    if args.version:
        print("ML-DiCE", version)
        exit()

    if argCheck(args):
        if args.estimator is None or args.estimator == "RF":
            print(clr.BLUE + "Info!" + clr.GREEN +" Random Forest is chosen as the default estimator. This can be changed to MLPRegressor as '-e' or '--estimator'" + clr.END)

        if validator(args):
            trainer = ModelTester(args, project_root)
            predicted_D = trainer.process()
        else:
            print(f"* {entry_err(args)}", file=vgout)
            return False
    else:
        print(f"* {entry_err(args)}", file=vgout)
        return False

    print("## Input Parameters:", file=vgout)
    print("|  Input Parameters   |    Value    |", file=vgout)
    print("|:-----------:|:-----------:|", file=vgout)
    for arg in vars(args):
        print(" | ", arg, "|", vars(args)[arg], " | ", file=vgout)
    if predicted_D:
        print("## Predicted Parameters:", file=vgout)
        print("|  Predicted Parameters   |    Value    |", file=vgout)
        print("|:-----------:|:-----------:|", file=vgout)
        print(" | ", f"Predicted {args.mechanism} diffusion coefficient" , "|", f"{predicted_D:.4e} m^2/s", " | ", file=vgout)
        print(" | ", "Mean squared error", "|", f"{0} m^2/s", " | ", file=vgout)

    print(file=vgout, flush=True)

    print(clr.BLUE + "RESULTS!!!" + clr.GREEN + f" Predicted {args.mechanism} diffusion coefficient of {args.DE} in {args.DM} is {predicted_D:.4e} m^2/s with MSE of " + clr.END)


MLDiCE()
