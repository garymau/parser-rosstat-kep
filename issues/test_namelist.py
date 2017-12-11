import pytest

from namelist import NAMES, make_namelist, find_missing_concepts

from collections import OrderedDict


def test_make_namelist_on_asterisk_retuRns_expected_list_of_strings():
    result = make_namelist(patterns=['WAGE_*'], names=NAMES)
    assert result == ['WAGE_NOMINAL_rub', 'WAGE_REAL_rog', 'WAGE_REAL_yoy']


def test_make_namelist_returns_sorted_list():
    names = ['WAGE_Z', 'WAGE_A']
    result = make_namelist(patterns=['WAGE_*'], names=names)
    assert result == ['WAGE_A', 'WAGE_Z']


def test_make_namelist_on_string_returns_expected_list_of_names():
    result = make_namelist(patterns=['UNEMPL'], names=NAMES)
    assert result == ['UNEMPL_pct']


def test_make_namelist_misses_name_in_the_middle():
    result = make_namelist(patterns=['WAGE_*'], names=['UNNECESSARY_WAGE_1'])
    assert result == []


def test_make_namelist_misses_missing_string():
    result = make_namelist(patterns="ABC", names=['DEF', 'XYZ'])
    assert result == []


def test_make_namelist_ignores_lowercase_pattern():
    result = make_namelist(patterns="def", names=['DEF', 'XYZ'])
    assert result == []


def test_make_namelist_ignores_lowercase_name():
    result = make_namelist(patterns="def", names=['def', 'XYZ'])
    assert result == []


def test_find_missing_concepts_on_concepts_odict_returns_extra_concept_names_set():
    concepts = OrderedDict()
    concepts.update({'GDP': ['GDP*']})
    concepts.update({'Output': ['IND*', 'TRANSPORT_FREIGHT']})
    concepts.update({'Prices': ['CPI*']})
    concepts.update({'Retail trade': ['RETAIL*']})
    concepts.update({'Government - revenue': ['GOV_REVENUE*']})
    concepts.update({'Government - spending': ['GOV_EXPENSE*']})
    concepts.update({'Government - surplus': ['GOV_SURPLUS*']})
    concepts.update({'Labour': ['WAGE_*', 'UNEMPL']})
    concepts.update({'Exchange rate': ['USDRUR*']})
    concepts.update({'Global': ['UST*', 'BRENT']})

    result = find_missing_concepts(concepts, NAMES)

    assert result == {'EXPORT_GOODS_bln_usd', 'INVESTMENT_rog', 'INVESTMENT_bln_rub',
                      'IMPORT_GOODS_bln_usd', 'INVESTMENT_yoy'}


if __name__ == '__main__':
    pytest.main([__file__])
