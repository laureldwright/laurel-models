# laurel-models
Data analysis and modeling


## Pip environment setup

I use `venv` and `pip` to manage an environment for running all notebooks EXCEPT `2. Generate descriptors.ipynb`. 

I'm using `Python 3.8.2`.

Instructions:

* Create the environment: `python3 -m venv /path/to/new/virtual/environment`
* Activate the environment: `source /path/to/new/virtual/environment/activate`
* Pip install requirements: `pip install -r requirements.txt`

## Miniconda environment setup for RDKIT

For running notebook `2. Generate descriptors.ipynb`, you will need to use miniconda. The package rdkit, which generates 2d descriptors, cannot be pip installed. 

Instructions: 
* Install Miniconda. Follow these instructions for installation on a mac: https://deeplearning.lipingyang.org/2018/12/24/install-miniconda-on-mac/
* Create the environment and install rdkit: `conda create -c rdkit -n my-rdkit-env rdkit`
* Activate the environment: `conda activate my-rdkit-env`
* Make Jupyter accessible by installing the `nb_conda_kernels_extension`: `conda install -n my-rdkit-env nb_conda_kernels`
* Launch Jupyter: `jupyter notebook`
