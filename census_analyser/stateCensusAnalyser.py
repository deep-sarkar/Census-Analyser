import pandas as pd
from custom_exceptions import FileIsNotCSVTypeException, EmptyFileException, InvalidDelimiterException
from abc import ABC, abstractmethod
# import numpy as np

class StateCensusAnalyser:

    def __init__(self):
        self.state = 'State'
        self.population = 'Population'
        self.areaInSqKm = 'AreaInSqKm'
        self.densityPerSqKm = 'DensityPerSqKm'

    def __repr__(self):
        return self.state +','+ self.population +','+ self.areaInSqKm +','+ self.densityPerSqKm

class ValidateFile(ABC):
    
    @abstractmethod
    def check_file_format(self, file_name):
        pass
    
    @abstractmethod
    def check_delimiter(self, data_frame):
        pass
            
class CSVStateCensus(StateCensusAnalyser, ValidateFile):

    def __init__(self, file_name):
        self.file_name = file_name
        self.col_list = repr(StateCensusAnalyser()).split(",")
    
    @property
    def load_CSV(self):
        if self.check_file_format(self.file_name):
            raise FileIsNotCSVTypeException
        try:
            df = pd.read_csv(self.file_name, usecols=self.col_list)
            if self.check_delimiter(df):
                raise InvalidDelimiterException
            return df
        except pd.errors.EmptyDataError:
            raise EmptyFileException

    def iterate_df(self, dataframe):
        for row in dataframe.itertuples():
            print(row)
        
    def number_of_records(self, dataframe):
        return len(dataframe) - 1

    def check_file_format(self, file_name):
        return file_name[-4:] != '.csv'

    def check_delimiter(self, data_frame):
        return data_frame.isnull().values.any()
    

file_name = "IndiaStateCensusData.csv"
invalid_header_file = "csv_with_invalid_header.csv"
invalid_delimiter_file = "csv_with_invalid_delimiter.csv"
obj = CSVStateCensus(file_name)
df = obj.load_CSV

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

    



