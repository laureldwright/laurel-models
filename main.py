import pandas as pd
import molvs
from RDKit_2D import *
##adapted from: https://drzinph.com/rdkit_2d-descriptors-in-python-part-4/

def main(file_path, smiles_col):

    df = pd.read_csv(file_path, sep="\t")
    df[smiles_col] = df[smiles_col].fillna('')

    smiles = []
    for i in df[smiles_col].values:
      try:
          mol = molvs.standardize_smiles(i)
      except Exception as e:
          if e == "AtomValenceException":
              pass
      smiles.append(mol)

    RDKit_descriptor = RDKit_2D(smiles)        # create your RDKit_2D object and provide smiles
    RDKit_descriptor.compute_2Drdkit('output.csv') #compute RDKit_2D abd export



    ## Compute RDKit_2D Fingerprints and export a csv file.
    RDKit_descriptor = RDKit_2D(smiles)        # create your RDKit_2D object and provide smiles
    RDKit_descriptor.compute_2Drdkit(file_path) # compute RDKit_2D and provide the name of your desired output file. you can use the same name as the input file because the RDKit_2D class will ensure to add "_RDKit_2D.csv" as part of the output file.

if __name__ == '__main__':
    main()
