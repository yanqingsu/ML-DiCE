from setuptools import setup, find_packages

with open("README.md", "r") as fh:
      description = fh.read()

setup(name='mldice',
      version='0.1.3',
      description='Machine Learned Diffusion Coefficent Estimator - ML-DiCE is an ML framework that can predict five modes of elemental diffusion in alloys ',
      url='https://github.com/yanqingsu/ML-DiCE',
      author='Arjun S Kulathuvayal',
      author_email='skvarjun@gmail.com',
      license='MIT',
      packages=find_packages(),
      python_requires='>=3',
      install_requires=['numpy==1.24.4', 'scikit-learn==1.3.0'],
      long_description=description,
      long_description_content_type="text/markdown",
      entry_points={'console_scripts': [
            'mldice = mldice:MLDiCE'
            ]},
      )