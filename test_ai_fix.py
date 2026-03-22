import pytest
from your_module import get_forecast  # replace 'your_module' with actual module name

def test_get_forecast_missing_error_handling():
    result = get_forecast(['list'])
    assert result['success'] == False
    assert result['error'] == "'list'"
    assert result['type'] == 'KeyError'

def test_get_forecast_missing_error_handling_success():
    result = get_forecast(['list'])
    assert result['success'] == True
    assert result['error'] is None
    assert result['type'] == None