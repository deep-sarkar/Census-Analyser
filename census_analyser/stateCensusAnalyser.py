import pandas as pd
from custom_exceptions import (FileIsNotCSVTypeException, 
                               EmptyFileException, 
                               InvalidDelimiterException)
from abc import ABC, abstractmethod
# import numpy as np

'''
StatusCensusAnalyser class will load StateCensus data
'''
class StateCensusAnalyser:

    def __init__(self):
        self.state = 'State'
        self.population = 'Population'
        self.areaInSqKm = 'AreaInSqKm'
        self.densityPerSqKm = 'DensityPerSqKm'

    def __repr__(self):
        return self.state +','+ self.population +','+ self.areaInSqKm +','+ self.densityPerSqKm

'''
CSVState class will load data from state code csv file
'''
class CSVState:

    def __init__(self):
        self.srNo      = 'SrNo'
        self.stateName     = 'StateName'
        self.tin       = 'TIN'
        self.stateCode = 'StateCode'

    def __repr__(self):
        return self.srNo +','+ self.stateName +','+ self.tin +','+ self.stateCode

'''
ValidateFile(ABC) is a abstract base class which have all abstract methods and these methods are used 
to validate csv file.
'''           
class CSVStateCensus(StateCensusAnalyser, CSVState): 

    def __init__(self, file_name):
        self.file_name = file_name
        
    @property
    def col_list(self):
        if self.file_name == 'StateCode.csv':
            col_list = repr(CSVState()).split(",")
        else:
            col_list = repr(StateCensusAnalyser()).split(",")
        return col_list

    @property
    def load_CSV(self):
        if self.file_name[-4:] != '.csv':
            raise FileIsNotCSVTypeException
        try:
            df = pd.read_csv(self.file_name, usecols=self.col_list)
            if df.isnull().values.any():
                raise InvalidDelimiterException
            return df
        except pd.errors.EmptyDataError:
            raise EmptyFileException
        except ValueError:
            return "InvalidHeader"

    def iterate_df(self, dataframe):        #Iterate dataframe into touples
        for row in dataframe.itertuples():
            print(row)
        
    def number_of_records(self, dataframe): #Return Number of rows in csv or records
        return len(dataframe) - 1



    

file_name = "IndiaStateCensusData.csv"
# invalid_header_file = "csv_with_invalid_header.csv"
# invalid_delimiter_file = "csv_with_invalid_delimiter.csv"
# demo_empty_csv = "demo_empty.csv"
# demo_txt    = "demo_empty.txt"
code_csv = 'StateCode.csv'
obj = CSVStateCensus(file_name)
df = obj.load_CSV
print(df)

# if df.isnull().values.any():
#     print("yes")
# for index in df.index:
#     print(df['DensityPerSqKm'][index])
#     if df['DensityPerSqKm'][index] == None:
#         print("Invalid")
# print(df)
# print(df._engine.data.dialect.delimiter)
# total_records = obj.number_of_records(df)
# print(total_records)
# print(len(df))
# obj.iterate_df(df)
# df_goa = df.loc[df["State"]=="Goa"]
# print(df_goa)
# print(df_goa['Population'])

    
  
# for ind in df.index:
#     print(df['State'][ind])

    



