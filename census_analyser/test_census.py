import pytest
from stateCensusAnalyser import CSVStateCensus
from custom_exceptions import ( FileIsNotCSVTypeException, 
                                EmptyFileException, 
                                InvalidDelimiterException)

class TestCensus:

    def test_State_census_records_to_match_number_of_records_UC1_TC1(self):
        obj = CSVStateCensus("IndiaStateCensusData.csv")
        total_records = obj.number_of_records(obj.load_CSV)
        assert total_records == 28

    def test_file_not_in_csv_format_will_raise_FileIsNotCSVTypeException_UC1_TC2(self):
        with pytest.raises(FileIsNotCSVTypeException):
            obj = CSVStateCensus("demo_empty.txt")
            obj.load_CSV
    
    def test_file_is_csv_but_empty_will_raise_EmptyFileException_UC1_TC3(self):
        with pytest.raises(EmptyFileException):
            obj = CSVStateCensus("demo_empty.csv")
            obj.load_CSV

    def test_file_is_csv_but_delimiter_is_invalid_will_raise_InvalidDelimiterException_UC1_TC4(self):
        with pytest.raises(InvalidDelimiterException):
            obj = CSVStateCensus('csv_with_invalid_delimiter.csv')
            obj.load_CSV