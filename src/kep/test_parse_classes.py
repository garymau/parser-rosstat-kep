# -*- coding: utf-8 -*-
"""
"""
import pytest



import parse

# standalone tests for classes:
#    Row
#    Header

# not covered:
#    RowStack    
#    TODO: list other classes

@pytest.fixture
def rows_for_header():
    csv_rows = [['Объем ВВП', '', '', '', ''],
                ['(уточненная оценка)', '', '', '', ''],
                ['млрд.рублей', '', '', '', '']]
    return [parse.Row(row) for row in csv_rows]

class Test_Row:
    
    def setup_method(self):
        pass
    
    def test_equals_dict_method(self):
        row = parse.Row(['Объем ВВП', 'a', 'b', 'c', '10'])
        d =  {'name': 'Объем ВВП', 'data': ['a', 'b', 'c', '10']}
        assert row.equals_dict(d) is True
                              
    def test_Row_matches_returns_bool(self):
        assert parse.Row(["Объем ВВП текущего года"]).matches("Объем ВВП") is True
        assert parse.Row(["1.1 Объем ВВП"]).matches("Объем ВВП") is False

    # TODO: more testing for methods single instance

    def test_str_method_returns_representation_string(self, rows_for_header):
        strs = [r.__str__() for r in rows_for_header]
        assert strs[0] == "Row <Объем ВВП>"
        assert strs[1] == "Row <(уточненная оценка)>"
        assert strs[2] == "Row <млрд.рублей>"   

    def test_name_property_returns_string(self, rows_for_header):
        assert rows_for_header[0].name == "Объем ВВП"
        assert rows_for_header[1].name == "(уточненная оценка)"
        assert rows_for_header[2].name == "млрд.рублей"

# testing RowStack class

ROWS = [{'name': 'Объем ВВП', 'data': ['', '', '', '']},
 {'name': '(уточненная оценка)', 'data': []},
 {'name': 'млрд.рублей', 'data': ['', '', '', '']},
 {'name': '1991 1)', 'data': ['100', '20', '30', '40', '10']},
 {'name': 'Индекс промышленного производства', 'data': []},
 {'name': 'в % к соответствующему периоду предыдущего года', 'data': []},
 {'name': '1991', 'data': ['102,7', '101,1', '102,2', '103,3', '104,3', '101,1', '101,1', '101,1', '102,2', '102,2', '102,2', '103,3', '103,3', '103,3', '104,3', '104,3', '104,3']}]

def to_row(d):
    elements = [d['name']] + d['data']
    return parse.Row(elements)
    
@pytest.fixture
def row_stack():    
    rows = [to_row(d) for d in ROWS]
    return parse.RowStack(rows)

class RowStack():
    def test_row_stack_fixture_self_test(row_stack):
        for s, r in zip(row_stack.rows, ROWS):
            assert s.name == r['name']
            assert s.data == r['data']


from cfg import Definition
class Test_RowStack_stable_on_definition_with_None_markers:
    
    def setup_method(self):
        # pdef_with_two_None_markers
        self.pdef1 = Definition("MAIN")
        self.pdef1.add_marker(None, None)

        # pdef_with_one_None_markers
        self.pdef2 = Definition("MAIN")
        self.pdef2.add_marker(None, "endline")
    
    def test_pop_returns_segment(self, row_stack):
        csv_segment = row_stack.pop(self.pdef1)
        assert len(csv_segment) == 7

    def test_pop_raises_ValueError_on_unsupported_def(self, row_stack):
        with pytest.raises(ValueError):
            row_stack.pop(self.pdef2)
    
    def test_is_found_raises_error(self, row_stack):
        with pytest.raises(AttributeError):
            # error found in Rows
            row_stack.is_found(None)


@pytest.fixture
def header():
    return parse.Header(rows_for_header())

@pytest.fixture
def _pdef():
    from cfg import Definition
    # WONTFIX: name MAIN is rather useless for Definition instance
    pdef = Definition("MAIN")
    pdef.add_header("Объем ВВП", "GDP")
    # WONTFIX: not testing boundaries here
    pdef.add_marker(None, None)
    pdef.require("GDP", "bln_rub")
    pdef.add_header("Индекс промышленного производства", "IND_PROD")
    pdef.require("IND_PROD", "yoy")
    return pdef

@pytest.fixture
def _units():
    # IDEA: may use explicit hardcoded constant with less units
    from cfg import UNITS
    return UNITS

class Test_Header:
    
    def test_KNOWN_UNKNOWN_sanity(self):
        # actual error before class constants were introduced
        assert parse.Header.KNOWN != parse.Header.UNKNOWN
    
    # on creation
    
    def test_on_creation_varname_and_unit_is_none(self, header):
        assert header.varname is None
        assert header.unit is None
        
    def test_on_creation_textlines_is_list_of_strings(self, header):
        # IDEA: why to we still need .textlines? can access them from .processed
        assert header.textlines == ['Объем ВВП',
                             '(уточненная оценка)', 
                             'млрд.рублей']

    def test_on_creation_processed_is_unknown(self, header):
        assert header.processed['Объем ВВП'] == parse.Header.UNKNOWN 
        assert header.processed['млрд.рублей'] == parse.Header.UNKNOWN 

    def test_on_creation_has_unknown_lines(self, header):
        assert header.has_unknown_lines() is True

    def test_on_creation_str(self, header):
        assert header.__str__() == 'varname: None, unit: None\n- <Объем ВВП>\n- <(уточненная оценка)>\n- <млрд.рублей>'

    # after parsing 
        
    def test_set_varname_results_in_GDP(self, header, _pdef, _units):
        header.set_varname(pdef=_pdef, units=_units)
        # IDEA: isolate work with units in set_varname() method 
        assert header.varname == 'GDP'        
        assert header.processed['Объем ВВП'] == parse.Header.KNOWN  
     
    def test_set_unit_results_in_bln_rub(self, header, _units):
        header.set_unit(units=_units)
        assert header.unit == 'bln_rub' 
        assert header.processed['млрд.рублей'] == parse.Header.KNOWN  

    def test_after_parsing_has_unknown_lines(self, header, _pdef, _units):
        header.set_unit(units=_units)
        header.set_varname(pdef=_pdef, units=_units)
        assert header.has_unknown_lines() is True

    def test_after_parsing_str(self, header):
        assert header.__str__() == ('varname: None, unit: None\n'
                                    '- <Объем ВВП>\n'
                                    '- <(уточненная оценка)>\n'
                                    '- <млрд.рублей>')
    
if __name__ == "__main__":
    pytest.main(["test_header.py"])      