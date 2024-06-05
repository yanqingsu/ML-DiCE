import re
import mendeleev
from sqlalchemy.exc import NoResultFound
from .utils import clr

class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass


class InputValidator:
    def __init__(self, de, dm, temp, mode, esti):
        self.de = de
        self.dm = dm
        self.temp = temp
        self.mode = mode
        self.esti = esti

    def validate_de(self):
        """Validate de: should be a non-empty string."""
        if not isinstance(self.de, str) or not self.de:
            raise ValidationError("Enter diffusing element as '-de' or '--diffusingMedium'")
        elif is_valid_atomic_symbol(self.de):
            pass
        else:
            raise ValidationError("Diffusion element must be represented by its atomic symbol")


    def validate_dm(self):
        """Validate dm: should be like Ni60Fe20Co40."""
        if self.dm.isdigit():
            raise ValidationError("Diffusion medium must be properly entered. Example: Ni60Fe20Co40")
        else:
            non_atomic_symbols = element_test(self.dm)
            if non_atomic_symbols:
                raise ValidationError(f"Non-atomic symbols found in diffusion medium: {non_atomic_symbols}")


    def validate_temp(self):
        """Validate temp: should be a float greater than 0."""
        if not isinstance(self.temp, float) or 10000 > self.temp < 0:
            print(self.temp)
            raise ValidationError("Temperature must be a float between 0 and 10000")

    def validate_mode(self):
        """Validate mode: should be self, impurity or chemical"""
        if not self.mode in ['self', 'impurity', 'chemical']:
            raise ValidationError("Diffusion mechanism must be any of the following: self, impurity or chemical")

    def validate_esti(self):
        """Validate esti: should be a list with at least one element."""
        if not self.esti in ['RF', 'DNN']:
            raise ValidationError("Choise of regressor be any of the following: RF or DNN")

    def validate_all(self):
        """Run all validations."""
        self.validate_de()
        self.validate_dm()
        self.validate_temp()
        self.validate_mode()
        self.validate_esti()


def is_valid_atomic_symbol(symbol):
    try:
        element = mendeleev.element(symbol)
        return True
    except NoResultFound:
        return False


def element_test(species):
    cleaned_string = re.sub(r'[0-9.]+', '', str(species))
    elements = []
    i = 0
    while i < len(cleaned_string):
        if i + 1 < len(cleaned_string) and cleaned_string[i + 1].islower():
            elements.append(cleaned_string[i:i + 2])
            i += 2
        else:
            elements.append(cleaned_string[i])
            i += 1
    all_elements = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar',
                    'K', 'Ca',
                    'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb',
                    'Sr', 'Y',
                    'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba',
                    'La',
                    'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W',
                    'Re',
                    'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U',
                    'Np',
                    'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt',
                    'Ds', 'Rg',
                    'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']
    non_atomic_symbols = [element for element in elements if element not in all_elements]
    return non_atomic_symbols


def validator(input_params):
    test_cases = [(input_params.DE, input_params.DM, input_params.temperature, input_params.mechanism, input_params.estimator)]
    for i, params in enumerate(test_cases):
        print(clr.BLUE + "Info! " + clr.GREEN + f"Validating input parameters DE: {params[0]}, DM: {params[1]}, Temperature: {params[2]}, Diffusion mechanism: {params[3]}, Regression algorithm {params[4]}" + clr.END)
        try:
            validator = InputValidator(*params)
            validator.validate_all()
            print(clr.BLUE + "Info! " + clr.GREEN + "Input parameters are successfully validated" + clr.END)
            return True
        except ValidationError as e:
            print(clr.RED + "Validation failed!!! " + clr.GREEN + str(e))


def namespace_to_list(namespace):
    args_list, args_val = [], []
    for arg, value in vars(namespace).items():
        if isinstance(value, bool):
            if value:
                args_list.append(f"--{arg}")
        else:
            args_val.append(f"--{arg}")
            args_list.append(str(value))

    return dict(zip(args_val, args_list))


def entry_err(input_data):
    if type == 0 or 1:
        x = namespace_to_list(input_data)
        empty_keys = []
        for key, value in x.items():
            if not value:
                empty_keys.append(key)
        statement = f"Input parameter {', '.join(map(str, empty_keys))} are not provided."
        return statement

