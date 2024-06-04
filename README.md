<h1 align="center">
<img src="https://raw.githubusercontent.com/skvarjun/ML-DiCE/art/logo.svg" height="130">

ML-DiCE
</h1>
<br>

[![DOI](https://zenodo.org/badge/DOI/update_soon.svg)](https://doi.org/to/be/updated)
[![PyPI](https://img.shields.io/pypi/v/mldice)](https://pypi.org/project/VaspGibbs/)

## Installation

```
pip install ML-DiCE
```
## Usage

In a terminal , run
```
ML-DiCE -options
```

`ML-DiCE` will featurize your alloy and predict diffusion coefficient in m^2/s. The options can be set through following arguments

Use `-de` to specify diffusing element `-dm` to specify diffusion medium. Examples:

 * `-de Fe` would take iron as diffusing element.
 * `-dm Ni75.5Cu24Co0.5` select Ni75.5Cu24Co0.5 is the diffusion medium where constituent elements expressed as percentage 
 * `-T 500` would select the temperature of diffusion process in Kelvin.
 * `-estimator RF` would select Random Forest regression as prediction algorithm.

Essentially, the run command would be as follows:
```
ML-DiCE -de [diffusing element] -dm [diffusion medium] -T [temperature] -estimator [prediction algorithm]
```


### Output

All outputs can be found in the ML-DiCE.md file. It contains the following information:

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
@software{therrien2023vaspgibbs,
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

## Under development

*Advanced featurization for alloys:* New featurization schemes are under developing

