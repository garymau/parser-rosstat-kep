import pytest

from namelist import make_namelist

test_samples = {
    ('GOV_REVENUE', 'GOV_SURPLUS'): ("GOV_REVENUE_CONSOLIDATED_bln_rub",
                                     "GOV_REVENUE_FEDERAL_bln_rub",
                                     "GOV_REVENUE_SUBFEDERAL_bln_rub",
                                     "GOV_SURPLUS_FEDERAL_bln_rub",
                                     "GOV_SURPLUS_SUBFEDERAL_bln_rub",),
    ('GOV*',): ("GOV_EXPENSE_CONSOLIDATED_bln_rub",
                "GOV_EXPENSE_FEDERAL_bln_rub",
                "GOV_EXPENSE_SUBFEDERAL_bln_rub",
                "GOV_REVENUE_CONSOLIDATED_bln_rub",
                "GOV_REVENUE_FEDERAL_bln_rub",
                "GOV_REVENUE_SUBFEDERAL_bln_rub",
                "GOV_SURPLUS_FEDERAL_bln_rub",
                "GOV_SURPLUS_SUBFEDERAL_bln_rub",),
    ('CPI_SERVICES',): ('CPI_SERVICES_rog',)
}


def test_make_namelist_on_search_patterns_return_list_of_names_matching_patterns():
    samples = test_samples.keys()
    for sample in samples:
        assert set(make_namelist(sample)) == set(test_samples[sample])


if __name__ == "__main__":
    pytest.main([__file__])
