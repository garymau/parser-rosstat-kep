# -*- coding: utf-8 -*-
import pytest
import datetime as dt

from config import DataFolder
from config import LocalCSV
# Hayk
#from config import PathHelper, DateHelper


@pytest.mark.skip()
def test_md(folder):
    assert False

@pytest.mark.skip()
def test_md(folder):
    assert False


# skipping

@pytest.mark.skip(reason="not testing maintenance scripts yet")
def test_copy_latest():
    assert False


# Hayk: Remove the tests for the PathHelper: no such a module anymore
#class Test_PathHelper:

#    def test_locate_csv_on_year_month_path_esists(self):
#        assert PathHelper.locate_csv(2017, 5).exists() is True

#    def test_get_processed_folder_returns_existing_folder(self):
#        assert PathHelper.get_processed_folder(2017, 5).exists() is True

#    def test_get_processed_folder_will_not_work_without_arguments(self):
#        with pytest.raises(TypeError):
#            PathHelper.get_processed_folder()


# Hayk: Remove the tests for the DateHelper: no such a module anymore
#class Test_DateHelper:

#    def test_validate_passes(self):
#        DateHelper.validate(2015, 6)

#    def test_validate_failes(self):
#        with pytest.raises(ValueError):
#            DateHelper.validate(2030, 1)

#    def test_get_latest_date(self):
#        year, month = DateHelper.get_latest_date()
#        assert year >= 2017
#        assert month >= 1
#        assert month <= 12

#    def test_get_supported_dates_starts_in_2009_4(self):
#        assert DateHelper.get_supported_dates()[0] == (2009, 4)

#    def test_get_supported_dates_ends_with_latest_date(self):
#        prev_month_date = dt.datetime.today().replace(day=1) - dt.timedelta(days=1)
#        assert DateHelper.get_supported_dates()[-1] == (prev_month_date.year,
#                                                        prev_month_date.month)

#    def test_get_supported_dates_excludes_2013_11(self):
#        assert (2013, 11) not in DateHelper.get_supported_dates()


@pytest.mark.skip(reason="not testing maintenance scripts yet")
def test_init_dirs():
    assert False

#HS: tests for the property methods added, instead of get_ functions
class Test_DataFolder():
    
    # we assume a typical state of repo for (2015, 5)      
    
    def test_repr(self):
        assert repr(DataFolder(2015, 5))

    def test_get_raw_property_method_returns_existing_folder(self):
        assert DataFolder(2015, 5).raw.exists()
    
    def test_get_interim_property_method_returns_existing_folder(self):
        assert DataFolder(2015, 5).interim.exists()
    
    def test_get_processed_property_method_returns_existing_folder(self):
        assert DataFolder(2015, 5).processed.exists()

    def test_out_of_range_year_does_raises_error(self):
        with pytest.raises(ValueError):
            DataFolder(2030, 1)

class Test_LocalCSV():
    def test_get_interim_property_method_returns_existing_file(self):
        assert LocalCSV(2015, 5).interim.exists()


# skipping
@pytest.mark.skip(reason="not testing maintenance scripts")
def test_copy_latest():
    assert False

# Hayk: Remove the tests for the PathHelper: no such a module anymore
#class Test_PathHelper:

#    def test_locate_csv_on_year_month_path_esists(self):
#        assert PathHelper.locate_csv(2017, 5).exists() is True

#    def test_get_processed_folder_returns_existing_folder(self):
#        assert PathHelper.get_processed_folder(2017, 5).exists() is True

#    def test_get_processed_folder_will_not_work_without_arguments(self):
#        with pytest.raises(TypeError):
#            PathHelper.get_processed_folder()


# Hayk: Remove the tests for the DateHelper: no such a module anymore
#class Test_DateHelper:

#    def test_validate_passes(self):
#        DateHelper.validate(2015, 6)

#    def test_validate_failes(self):
#        with pytest.raises(ValueError):
#            DateHelper.validate(2030, 1)

#    def test_get_latest_date(self):
#        year, month = DateHelper.get_latest_date()
#        assert year >= 2017
#        assert month >= 1
#        assert month <= 12

#    def test_get_supported_dates_starts_in_2009_4(self):
#        assert DateHelper.get_supported_dates()[0] == (2009, 4)


#    def test_get_supported_dates_excludes_2013_11(self):
#        assert (2013, 11) not in DateHelper.get_supported_dates()


@pytest.mark.skip(reason="not testing maintenance scripts yet")
def test_init_dirs():
    assert False


if __name__ == "__main__":
    pytest.main([__file__])
