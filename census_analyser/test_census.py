import pytest
from stateCensusAnalyser import CSVStateCensus, SortData, Mapping
from custom_exceptions import ( FileIsNotCSVTypeException, 
                                EmptyFileException, 
                                InvalidDelimiterException)


sort_ref = SortData()
map_ref  = Mapping()

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
    
    def test_file_is_csv_but_header_is_invalid_will_return_InvalidHeader_UC1_TC5(self):
        obj = CSVStateCensus("csv_with_invalid_header.csv")
        assert obj.load_CSV == "InvalidHeader"

    def test_State_code_records_to_match_number_of_records_UC2_TC1(self):
        obj = CSVStateCensus("StateCode.csv")
        total_records = obj.number_of_records(obj.load_CSV)
        assert total_records == 36
    
    def test_IndiaStateCensus_first_state_after_sorting_in_JSON_will_be_Andhra_Pradesh_UC3(self):
        data_frame = sort_ref._SortData__sort_InidaCensusData_in_alphabetical_order_in_JSON()
        assert data_frame[0]["State"] == 'Andhra Pradesh'
    
    def test_IndiaStateCensus_last_state_after_sorting_in_JSON_will_be_West_Bengal_UC3(self):
        data_frame = sort_ref._SortData__sort_InidaCensusData_in_alphabetical_order_in_JSON()
        assert data_frame[28]["State"] == 'West Bengal'

    def test_StateCode_first_stateCode_after_sorting_in_JSON_will_be_AD_UC4(self):
        data_frame = sort_ref._SortData__sort_StateCode_in_stateCode_order_in_JSON()
        assert data_frame[0]["StateCode"] == 'AD'

    def test_StateCode_last_stateCode_after_sorting_in_JSON_will_be_WB_UC4(self):
        data_frame = sort_ref._SortData__sort_StateCode_in_stateCode_order_in_JSON()
        assert data_frame.pop()["StateCode"] == 'WB'

    def test_after_sort_according_to_population_check_first_record_will_be_Sikkim_UC5(self):
        data = sort_ref._SortData__sort_InidaCensusData_in_asc_population_order_in_JSON()
        assert data[0]["State"] == "Sikkim"

    def test_after_sort_according_to_population_check_last_record_will_be_Uttar_Pradesh_UC5(self):
        data = sort_ref._SortData__sort_InidaCensusData_in_asc_population_order_in_JSON()
        assert data.pop()["State"] == "Uttar Pradesh"

    def test_after_sort_according_to_populationDensity_check_first_record_will_be_Arunachal_Pradesh_UC6(self):
        data = sort_ref._SortData__sort_InidaCensusData_in_asc_population_density_order_in_JSON()
        assert data[0]["State"] == "Arunachal Pradesh"

    def test_after_sort_according_to_populationDensity_check_last_record_will_be_Bihar_UC6(self):
        data = sort_ref._SortData__sort_InidaCensusData_in_asc_population_density_order_in_JSON()
        assert data.pop()["State"] == "Bihar"
    
    def test_mapping_by_checking_first_record_will_be_AP_REFACTOR6(self):
        data = map_ref._Mapping__map_state_census_with_state_code_according_to_code()
        assert data[0]["StateCode"] == 'AP'

    def test_mapping_by_checking_last_record_will_be_WB_REFACTOR6(self):
        data = map_ref._Mapping__map_state_census_with_state_code_according_to_code()
        assert data.pop()["StateCode"] == 'WB'

    def test_first_state_from_census_data_after_sorting_in_desc_area_order_will_return_Rajasthan_UC7(self):
        data = sort_ref._SortData__sort_InidaCensusData_in_desc_area_order_in_JSON()
        assert data[0]["State"] == "Rajasthan"

    def test_last_state_from_census_data_after_sorting_in_desc_area_order_will_return_Goa_UC7(self):
        data = sort_ref._SortData__sort_InidaCensusData_in_desc_area_order_in_JSON()
        assert data.pop()["State"] == "Goa"