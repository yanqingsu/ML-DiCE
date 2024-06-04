from setuptools import setup

setup(name='ML-DiCE',
      version='0.0.1',
      description='Machine Learned Diffusion Coefficent estimator is an ML framework that can predict five modes of elemental diffusion in alloys ',
      url='https://github.com/skvarjun/ML-DiCE',
      author='Arjun S Kulathuvayal',
      author_email='skvarjun@gmail.com',
      license='MIT',
      packages=['mldice'],
      python_requires='>=3',
      install_requires=[
          'numpy',
          'scikit-learn',
      ],
      scripts=['ml_dice'],)