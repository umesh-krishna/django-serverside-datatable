import pytest
from django_serverside_datatable.datatable import DataTablesServer

@pytest.mark.django_db
def test_filtering_and_sorting(mock_request, sample_queryset):
    columns = ['username', 'email']
    request = mock_request
    request.GET = {
        'sSearch': 'David',
        'bSearchable_0': 'true',
        'bSearchable_1': 'true',
        'iDisplayStart': '0',
        'iDisplayLength': '10',
        'iSortCol_0': '0',
        'sSortDir_0': 'asc',
        'iSortingCols': '1',
        'sEcho': '1',
    }
    datatable = DataTablesServer(request, columns, sample_queryset)
    result = datatable.output_result()
    assert result['iTotalDisplayRecords'] == '2'
    assert result['aaData'] == [['David Beckham', 'david.beckham@example.com'], ['David Warner', 'david.warner@example.com']]

@pytest.mark.django_db
def test_without_search(mock_request, sample_queryset):
    columns = ['username', 'email']
    request = mock_request
    request.GET = {
        # 'sSearch': '',
        'bSearchable_0': 'true',
        'bSearchable_1': 'true',
        'iDisplayStart': '0',
        'iDisplayLength': '10',
        'iSortCol_0': '0',
        'sSortDir_0': 'asc',
        'iSortingCols': '1',
        'sEcho': '1',
    }
    datatable = DataTablesServer(request, columns, sample_queryset)
    result = datatable.output_result()
    assert len(result['aaData']) == 5