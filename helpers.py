# Copyright 2022 by Laurel Wright
# All rights reserved.


import os
import pandas as pd


def read_files(directory, file_ext, **kwargs):
    """
    Reads in txt, tsv or csv files from a specified local directory as panda dataframes.
    Returns a dictionary of dataframes where the key is the file name and the values are the dataframes.
    
    Args:
        directory(str): Directory name. Include slashes. Eg: 'data/mydir/'
        file_ext(str): File extension. E.g.,: '.csv'
        **kwargs: Keyword arguments to pandas.read_csv
        
    Returns: Dictionary where keys are filnames and values are pd.DataFrames.  
     """

    files = [x for x in os.listdir(directory) if x.endswith(file_ext)]
    filenames = [os.path.splitext(os.path.basename(x))[0] for x in files]

    d = {}
    for i in range(len(filenames)):
        d[filenames[i]] = pd.read_csv(directory + f'{files[i]}', **kwargs)

    return d


def data_qual(data_dict):
    """
    Summarizes data quality information in a table. Reports if there are 0 values, missing values (nulls), or duplicated data.
  
    Args:
        data_dict(dict): Dictionary where keys are filnames and values are pd.DataFrames.  
        
    Returns: pd.DataFrame. 
    """
    
    data_qual_dict = {}

    final_df = pd.DataFrame()

    for k, v in data_dict.items():
        data_qual_dict["Filename"] = [k]

        if False in v.all().unique():
            data_qual_dict["0 values_present"] = [True]
        else:
            data_qual_dict["0 values_present"] = [False]

        if False in v.isnull().values.any():
            data_qual_dict["Null values present"] = [False]
        else:
            data_qual_dict["Null values present"] = [True]

        dup_rows = v.duplicated().sum()
        data_qual_dict["Duplicate rows"] = [dup_rows]

        final_df = final_df.append(pd.DataFrame.from_dict(data_qual_dict))

    return final_df


def process_data(data_dict):
    """"Wrapper function for concatenating data into a single dataframe and adding columns of interest

    Args:
        data_dict(dict): Dictionary where keys are filnames and values are pd.DataFrames.  
        
    Returns: pd.DataFrame. 
    """
    
    df = concatenate_experiments(data_dict)
    df = add_columns(df)
    
    return df


def concatenate_experiments(data_dict):
    """
    Returns single dataframe containing data from multiple experimental files, and adds a column containing the filename
   
    Args:
        data_dict(dict): Dictionary where keys are filnames and values are pd.DataFrames.  
        
    Returns: pd.DataFrame. 
    """

    df = pd.DataFrame()

    for k, v in sorted(data_dict.items()):
        v["filename"] = k
        df = df.append(v)

    return df


def add_columns(df):

    """
    TODO
    Adds additional columns to data dataframe. 
    
    Args:
        df(pd.Dataframe)- Input data
        
    Returns: pd.DataFrame. 
    """
    
    return df


def define_groups(df):
    """
    Divides observations into four dataframes of the following treatment groups:
    1. Controls (positive and negative)
    2. Positive control
    3. Negative control
    4. Experimental (non-control)
    
    Args:
        df(pd.Dataframe)- Processed input data
        
    Returns: Tuple of pd.DataFrames. 
    """

    controls = df.query("(name == @POSITIVE) | (name == @NEGATIVE)").reset_index()
    positive = controls.query("(name == @POSITIVE)")
    negative = controls.query("(name == @NEGATIVE)")
    experimental = df.loc[~df["name"].isin([POSITIVE, NEGATIVE])]

    return controls, positive, negative, experimental


def summary_stats(df, plate_col=None, exp_col=None):

    """
    Calculates average number of observations per plate and experiment. 
    
    Args:
        df(pd.Dataframe)- Processed input data
        plate_col(str)- Plate identifier column. Default is none.
        exp_col(str)- Experiment identifier column. Default is none. 

    """

    if plate_col: 
        m1 = int(df.groupby(plate_col).count().mean()[0])
        print(f"Average number of observations per plate: {m1}")
    
    if exp_col: 
        m2 = int(df.groupby(exp_col).count().mean()[0])
        print(f"Average number of observations per experiment: {m2}")

    
def value_counts_of_process_variables(df, cols_of_interest):
    """
    Value counts of process variables of interest that are included in the data.

    Args:
        df(pd.Dataframe)- Processed input data
        cols_of_interest- list of strings containing columns headers of interest
    """

    print("Number of observations per process variable group:")
    print()

    for col in cols_of_interest:
        print(col)
        display(df[col].value_counts())
        print()


def plot_plate_location_effects(df, plate_col, response_col, process_col, title, **kwargs):
    """
    Displays an interactive chart highlighting potential process effects related to plate layout (such as row or column).

    Args:
        df(pd.Dataframe)- Processed input data
        plate_col(str)- Plate identifier column
        response_col(str)- Response column
        process_col(str)- Column to color by. Example: columns. 
        title(str)- Plot title
        **kwargs- Chart kwargs
        
    Returns: altair Chart
    """
    chart = (
        alt.Chart(df)
        .mark_point(filled=True, size=60)
        .encode(
            x=plate_col,
            y=response_col,
            color=col,
            **kwargs,
        )
        .interactive()
        .properties(title=title, width=300, height=300)
    )
    return chart