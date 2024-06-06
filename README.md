<h1 align="center">
<img src="https://www.mzlab.co.in/frontend/img/team/logo.svg" height="130">

ML-DiCE | Machine Learned Diffusion Coefficient Estimator
</h1>
<br>

[![DOI](https://zenodo.org/badge/DOI/update_soon.svg)](https://doi.org/to/be/updated)
[![PyPI](https://img.shields.io/pypi/v/mldice/0.2.0)](https://pypi.org/project/mldice/)

## Installation

```
pip install mldice
```
## Usage

Create a conda environment as 

```
conda create --name myEnv
```
Activate the environment created
```
conda activate myEnv
```
In the activated environment, run
```
mldice -options
```

`mldice` will featurize your alloy or impure metal and predict diffusion coefficient in m^2/s. The options can be set through following arguments

Use `-de` to specify diffusing element `-dm` to specify diffusion medium. Examples:

 * `-de Fe` would take iron as diffusing element.
 * `-dm Ni75.5Cu24Co0.5` select Ni75.5Cu24Co0.5 is the diffusion medium where constituent elements expressed as percentage 
 * `-t 500` would select the temperature (say, 500K in this case) of diffusion process in Kelvin.
 * `-m self` select self diffusion mechanism. Mechanisms include self, impurity and chemical modes. 
 * `-e RF` would select Random Forest regression as prediction algorithm. DNN selects neural network based prediction.

Essentially, the run command shall be as follows:
```
mldice -de [diffusing element] -dm [diffusion medium] -t [temperature] -m [diffusion mechanism] -e [algorithm chosen for prediction]
```


## Output

All outputs can be found in the Prediction.md file. It contains the following information:

#### Predicted parameters
|  Property   |    Value    |
|:-----------:|:-----------:|
| Predicted D | --    m^2/s |
|    RMSE     | --    m^2/s |
|     MAE     | --    m^2/s |
| Uncertainty | --    m^2/s |



## Online Ressources

* https://arjun.skv.net/SI (Supporting Information)
* https://arjunskv.net/main (Main article)


## Citation

```
@software{mldice,
  author       = {Kulathuvayal Arjun S., Su Yanqing },
  title        = {{Elemental Diffusion Coefficient Prediction in Conventional Alloys using Machine Learning}},
  month        = june,
  year         = 2024,
  publisher    = {--},
  version      = {v0.0.1},
  doi          = {--},
  url          = {--}
}
```

### Under development

*Advanced featurization for alloys:* New featurization schemes are under developing

