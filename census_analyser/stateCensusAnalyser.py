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
ValidateFile(ABC) is a abstract base class which have all abstract methods and these methods are used 
to validate csv file.
'''
class ValidateFile(ABC):
    
    @abstractmethod
    def check_file_format(self, file_name):  #abstract method to check file format is .csv or not
        pass
    
    @abstractmethod
    def check_delimiter(self, data_frame): #abstract method to check delimiter is correct or not
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
        except ValueError:
            return "InvalidHeader"

    def iterate_df(self, dataframe):        #Iterate dataframe into touples
        for row in dataframe.itertuples():
            print(row)
        
    def number_of_records(self, dataframe): #Return Number of rows in csv or records
        return len(dataframe) - 1

    def check_file_format(self, file_name): #overrided method to check file format will returns True if its not .csv
        return file_name[-4:] != '.csv'

    def check_delimiter(self, data_frame): #if there is nan in file or empty data will return True
        return data_frame.isnull().values.any()
    

file_name = "IndiaStateCensusData.csv"
invalid_header_file = "csv_with_invalid_header.csv"
invalid_delimiter_file = "csv_with_invalid_delimiter.csv"
demo_empty_csv = "demo_empty.csv"
demo_txt    = "demo_empty.txt"
obj = CSVStateCensus(invalid_header_file)
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

    



