from setuptools import setup, find_packages

with open("README.md", "r") as fh:
      description = fh.read()

setup(name='mldice',
      version='0.1.9',
      description='Machine Learned Diffusion Coefficient Estimator - ML-DiCE is an ML framework that can predict five modes of elemental diffusion in alloys ',
      url='https://github.com/yanqingsu/ML-DiCE',
      author='Arjun S Kulathuvayal',
      author_email='skvarjun@gmail.com',
      license='MIT',
      packages=find_packages(),
      python_requires='>=3',
      install_requires=['numpy==1.24.4', 'scikit-learn==1.3.0', 'mendeleev', 'seaborn'],
      data_files=[('mldice', ['mldice/models/DNN/MCA_chemical/DNN_model',
                              'mldice/models/DNN/MCA_impurity/DNN_model',
                              'mldice/models/DNN/MCA_self/DNN_model',
                              'mldice/models/DNN/IM_self/DNN_model',
                              'mldice/models/DNN/IM_impurity/DNN_model',
                              'mldice/models/DNN/featureSpace.csv',
                              'mldice/models/RF/MCA_chemical/RF_model',
                              'mldice/models/RF/IM_impurity/RF_model',
                              'mldice/models/RF/IM_self/RF_model',
                              'mldice/models/RF/featureSpace.csv',
                              ])],
      include_package_data=True,
      long_description=description,
      long_description_content_type="text/markdown",
      entry_points={'console_scripts': [
            'mldice = mldice:MLDiCE'
            ]},
      )