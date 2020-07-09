import pandas as pd
class StateCensusAnalyser:

    def __init__(self):
        self.state = 'State'
        self.population = 'Population'
        self.areaInSqKm = 'AreaInSqKm'
        self.densityPerSqKm = 'DensityPerSqKm'

    def __repr__(self):
        return self.state +','+ self.population +','+ self.areaInSqKm +','+ self.densityPerSqKm


class CSVStateCensus(StateCensusAnalyser):

    def __init__(self):
        self.file_name = "IndiaStateCensusData.csv"
        self.col_list = repr(StateCensusAnalyser()).split(",")
        self.df = pd.read_csv(self.file_name, usecols=self.col_list)

# obj = CSVStateCensus()
# df = obj.df
# df_goa = df.loc[df["State"]=="Goa"]
# print(df_goa['Population'])
# print(obj.df.iloc["Goa"])
# if obj.df["State"] == "Goa":
#     print(obj.df['Population'])


