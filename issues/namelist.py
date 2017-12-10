# part of issue https://github.com/mini-kep/db/blob/master/doc/listing.md

import itertools
import fnmatch

NAMES = [
    "BRENT",
    "CPI_ALCOHOL_rog",
    "CPI_FOOD_rog",
    "CPI_NONFOOD_rog",
    "CPI_rog",
    "CPI_SERVICES_rog",
    "EXPORT_GOODS_bln_usd",
    "GDP_bln_rub",
    "GDP_yoy",
    "GOV_EXPENSE_CONSOLIDATED_bln_rub",
    "GOV_EXPENSE_FEDERAL_bln_rub",
    "GOV_EXPENSE_SUBFEDERAL_bln_rub",
    "GOV_REVENUE_CONSOLIDATED_bln_rub",
    "GOV_REVENUE_FEDERAL_bln_rub",
    "GOV_REVENUE_SUBFEDERAL_bln_rub",
    "GOV_SURPLUS_FEDERAL_bln_rub",
    "GOV_SURPLUS_SUBFEDERAL_bln_rub",
    "IMPORT_GOODS_bln_usd",
    "INDPRO_rog",
    "INDPRO_yoy",
    "INVESTMENT_bln_rub",
    "INVESTMENT_rog",
    "INVESTMENT_yoy",
    "RETAIL_SALES_bln_rub",
    "RETAIL_SALES_FOOD_bln_rub",
    "RETAIL_SALES_FOOD_rog",
    "RETAIL_SALES_FOOD_yoy",
    "RETAIL_SALES_NONFOOD_bln_rub",
    "RETAIL_SALES_NONFOOD_rog",
    "RETAIL_SALES_NONFOOD_yoy",
    "RETAIL_SALES_rog",
    "RETAIL_SALES_yoy",
    "TRANSPORT_FREIGHT_bln_tkm",
    "UNEMPL_pct",
    "USDRUR_CB",
    "UST_10YEAR",
    "UST_1MONTH",
    "UST_1YEAR",
    "UST_20YEAR",
    "UST_2YEAR",
    "UST_30YEAR",
    "UST_3MONTH",
    "UST_3YEAR",
    "UST_5YEAR",
    "UST_6MONTH",
    "UST_7YEAR",
    "WAGE_NOMINAL_rub",
    "WAGE_REAL_rog",
    "WAGE_REAL_yoy"
]


def extract_varname(label):
    words = label.split('_')
    return '_'.join(itertools.takewhile(lambda word: word.isupper(), words))


def is_matched(name, pat):
    varhead = extract_varname(name)
    return fnmatch.fnmatch(varhead, pat)


def make_namelist(patterns, names):
    return sorted([name for pat in patterns for name in names
                   if is_matched(name, pat)])


def find_missing_concepts(_concepts, names):
    concept_names = make_namelist([p for patterns in _concepts.values() for p in patterns], names)
    return set(NAMES) - set(concept_names)


if __name__ == '__main__':
    # https://github.com/mini-kep/db/blob/master/doc/listing.md
    from collections import OrderedDict

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
    print(concepts)
    print(find_missing_concepts(concepts, NAMES))
