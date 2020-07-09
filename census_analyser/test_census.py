import pytest
from . stateCensusAnalyser import CSVStateCensus

class TestCensus:

    def test_State_census_records_to_match_number_of_records_UC1_TC1(self):
        obj = CSVStateCensus("IndiaStateCensusData.csv")
        total_records = obj.number_of_records(obj.df)
        assert total_records == 28