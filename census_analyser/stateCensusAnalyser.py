import pandas as pd
from custom_exceptions import (FileIsNotCSVTypeException, 
                               EmptyFileException, 
                               InvalidDelimiterException)
from abc import ABC, abstractmethod
import json

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
        self.stateName = 'StateName'
        self.tin       = 'TIN'
        self.stateCode = 'StateCode'

    def __repr__(self):
        return self.srNo +','+ self.stateName +','+ self.tin +','+ self.stateCode

'''
CSVStateCensus class will inherit StateCensusAnalyser and CSVState to load data from csv file.
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
        df_list = [list(row) for row in dataframe.values]
        return df_list
        
    def number_of_records(self, dataframe): #Return Number of rows in csv or records
        return len(dataframe) - 1



'''
SortData class will have all method according to all sorting method and save data into json
'''
class SortData(CSVStateCensus):
    def __init__(self):
        self.code_data_frame = CSVStateCensus("StateCode.csv").load_CSV
        self.census_data_frame = CSVStateCensus("IndiaStateCensusData.csv").load_CSV


    def __sorting_function(self,dataframe,col_name,ascending=True):  #Sorting functtion
        return dataframe.sort_values([col_name],ascending=ascending)


    def __sort_InidaCensusData_in_alphabetical_order_in_JSON(self): #sort and returns stateCensus data according to state
            sorted_df = self.__sorting_function(self.census_data_frame,"State")
            sorted_df.to_json(r'IndiStateCensusData.json', orient='records')
            with open('IndiStateCensusData.json','r') as json_file:
                census = json.load(json_file)
                return census
    
    def __sort_StateCode_in_stateCode_order_in_JSON(self): #sort and returns stateCode data according to Code
            sorted_df = self.__sorting_function(self.code_data_frame,'StateCode')
            sorted_df.to_json(r'StateCode.json', orient='records')
            with open('StateCode.json','r') as json_file:
                census = json.load(json_file)
                return census
    
    def __sort_InidaCensusData_in_asc_population_order_in_JSON(self): #sort and returns stateCensus data according to population
            sorted_df = self.__sorting_function(self.census_data_frame,'Population')
            sorted_df.to_json(r'IndiStateCensusData_asc_population.json', orient='records')
            with open('IndiStateCensusData_asc_population.json','r') as json_file:
                census = json.load(json_file)
                return census

    def __sort_InidaCensusData_in_asc_population_density_order_in_JSON(self): #sort and returns stateCensus data according to populationSensity
            sorted_df = self.__sorting_function(self.census_data_frame,"DensityPerSqKm")
            sorted_df.to_json(r'IndiStateCensusData_asc_populationDensity.json', orient='records')
            with open('IndiStateCensusData_asc_populationDensity.json','r') as json_file:
                census = json.load(json_file)
                return census

    def __sort_InidaCensusData_in_desc_area_order_in_JSON(self): #sort and returns stateCensus data according to descending area Area
        sorted_df = self.__sorting_function(self.census_data_frame,"AreaInSqKm",ascending=False)
        sorted_df.to_json(r'IndiStateCensusData_desc_area.json', orient='records')
        with open('IndiStateCensusData_desc_area.json','r') as json_file:
            census = json.load(json_file)
            return census


'''
Mapping class inherits SortData class and map state census with state code. 
'''
class Mapping(SortData):

    def __map_state_census_with_state_code_according_to_code(self):
        merge_inner = pd.merge(left=self.code_data_frame, right=self.census_data_frame,left_on='StateName',right_on='State')
        merged_data = merge_inner.drop(['SrNo'], axis=1)
        sort_state_code = merged_data.sort_values('StateCode')
        sort_state_code.to_json(r'Mapped_data_acc_to_stateCode.json', orient='records')
        with open('Mapped_data_acc_to_stateCode.json','r') as map_file:
            map_data = json.load(map_file) 
            return map_data
       



# file_name = "IndiaStateCensusData.csv"
# invalid_header_file = "csv_with_invalid_header.csv"
# invalid_delimiter_file = "csv_with_invalid_delimiter.csv"
# demo_empty_csv = "demo_empty.csv"
# demo_txt    = "demo_empty.txt"
# code_csv = 'StateCode.csv'
# obj = CSVStateCensus(file_name)
# df = obj.load_CSV
# d = df.sort_values(['State'])
# print(d)
# s = sort_ref.sort_InidaCensusData_in_asc_population_density_order_in_JSON(df)
# print(s)
# print(sorted_df)
# print(df)
# df_list = obj.iterate_df(df)
# print(df_list)

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

# s = SortData()
# d = s._SortData__sort_InidaCensusData_in_asc_population_density_order_in_JSON()
# print(d)
# for data in d:
#     print(data['State'])

# m = Mapping()
# c = m._Mapping__map_state_census_with_state_code_according_to_code()
# print(c)

