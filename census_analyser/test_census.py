import pytest
from . stateCensusAnalyser import CSVStateCensus
from . custom_exceptions import FileIsNotCSVTypeException

class TestCensus:

    def test_State_census_records_to_match_number_of_records_UC1_TC1(self):
        obj = CSVStateCensus("IndiaStateCensusData.csv")
        total_records = obj.number_of_records(obj.df)
        assert total_records == 28

    def test_file_not_in_csv_format_will_raise_FileIsNotCSVTypeException_UC1_TC2(self):
        with pytest.raises(FileIsNotCSVTypeException):
            CSVStateCensus("abc.txt")