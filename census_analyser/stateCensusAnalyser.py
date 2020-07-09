import pandas as pd
from custom_exceptions import FileIsNotCSVTypeException
from abc import ABC, abstractmethod

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

            
class CSVStateCensus(StateCensusAnalyser, ValidateFile):

    def __init__(self, file_name):
        self.file_name = file_name
        self.col_list = repr(StateCensusAnalyser()).split(",")
        if self.check_file_format(file_name):
            raise FileIsNotCSVTypeException
        self.df = pd.read_csv(self.file_name, usecols=self.col_list)


    def iterate_df(self, dataframe):
        for row in df.itertuples():
            print(row)
        
    def number_of_records(self, dataframe):
        return len(dataframe) - 1

    def check_file_format(self, file_name):
        return file_name[-4:] != '.csv'


file_name = "IndiaStateCensusData.csv"
obj = CSVStateCensus(file_name)
df = obj.df
# total_records = obj.number_of_records(df)
# print(total_records)
# print(len(df))
# obj.iterate_df(df)
# df_goa = df.loc[df["State"]=="Goa"]
# print(df_goa)
# print(df_goa['Population'])

    
  
# for ind in df.index:
#     print(df['State'][ind])

    



