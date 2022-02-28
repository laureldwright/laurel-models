# laurel-models
Data analysis and modeling


## Pip environment setup

I use `venv` and `pip` to manage an environment for running all notebooks EXCEPT for generating 2d descriptors for chemoinformatics. See the instructions below for generating descriptors.

I'm using `Python 3.8.2`.

Instructions:

* Create the environment: `python3 -m venv /path/to/new/virtual/environment`
* Activate the environment: `source /path/to/new/virtual/environment/activate`
* Pip install requirements: `pip install -r requirements.txt`

## Generating 2d Descriptors

For generating 2d descriptors from SMILES, you will need to generate a miniconda environment. The package rdkit, which generates 2d descriptors, cannot be pip installed.

Instructions:
* Install Miniconda. Follow these instructions for installation on a mac: https://deeplearning.lipingyang.org/2018/12/24/install-miniconda-on-mac/
* Create the environment and install rdkit: `conda create -c rdkit -n my-rdkit-env rdkit`
* Activate the environment: `conda activate my-rdkit-env`
* Install molvs: `conda install -c conda-forge molvs`
* Install pandas: `conda install -c conda-forge pandas`\
*  In the terminal, generate a csv containing 2d descriptors from a local csv, where the input csv contains a column with SMILES: 
```
python
import main
main.main(<file_path>, <SMILES column)
```
