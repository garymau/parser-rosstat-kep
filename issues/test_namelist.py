import pytest

from namelist import make_namelist

patterns = [['GOV_REVENUE', 'GOV_SURPLUS'], ['GOV*'], ['CPI_SERVICES_rog']]
results = [
    [
        "GOV_REVENUE_CONSOLIDATED_bln_rub",
        "GOV_REVENUE_FEDERAL_bln_rub",
        "GOV_REVENUE_SUBFEDERAL_bln_rub",
        "GOV_SURPLUS_FEDERAL_bln_rub",
        "GOV_SURPLUS_SUBFEDERAL_bln_rub",
    ],
    [
        "GOV_EXPENSE_CONSOLIDATED_bln_rub",
        "GOV_EXPENSE_FEDERAL_bln_rub",
        "GOV_EXPENSE_SUBFEDERAL_bln_rub",
        "GOV_REVENUE_CONSOLIDATED_bln_rub",
        "GOV_REVENUE_FEDERAL_bln_rub",
        "GOV_REVENUE_SUBFEDERAL_bln_rub",
        "GOV_SURPLUS_FEDERAL_bln_rub",
        "GOV_SURPLUS_SUBFEDERAL_bln_rub",
    ],
    ['CPI_SERVICES_rog'],

]


def test_make_namelist_on_search_patterns_return_list_of_names_matching_patterns():
    for test_i in range(len(patterns)):
        assert set(make_namelist(patterns[test_i])) == set(results[test_i])


if __name__ == "__main__":
    pytest.main([__file__])
