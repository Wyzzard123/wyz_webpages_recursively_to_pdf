To install Numpy and Pandas on their Mac M1s if you ever get to it, you'll need to do the following steps:

1. In your virtual environment, install cython: ```pip install cython```
2. Git clone numpy (Note: See [releases](https://github.com/numpy/numpy/releases) if you want to get a particular version): ```git clone https://github.com/numpy/numpy.git```
3. cd into the numpy directory: ```cd numpy```
4. Pip install numpy with the following command:```pip install . --no-binary :all: --no-use-pep517```
5. Git clone pandas (Note: See [releases](https://github.com/pandas-dev/pandas/releases) if you want a particular version): ```git clone --depth 1 https://github.com/pandas-dev/pandas.git```
6. cd into 'pandas' directory: ```cd pandas```
7. Run the setup.py: ```python setup.py install```

See: 
https://stackoverflow.com/questions/65336789/numpy-build-fail-in-m1-big-sur-11-1
https://stackoverflow.com/questions/65084318/trouble-installing-pandas-on-new-macbook-air-m1/66048187#66048187