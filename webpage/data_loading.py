#### Module : Data Loading from Computer File
""" data file format 
     1. csv file format, 
     2. file only have 2 column 
     3. 1st column is text contain
     4. 2nd column is suicide or non-suicide class contain
"""
     
     
## libraries
import pandas as pd

def load_data(path):
    dataset = pd.read_csv(path)
    return dataset