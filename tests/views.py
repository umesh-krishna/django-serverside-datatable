import pytest
from django import get_version
from django.test import override_settings
from django_serverside_datatable.views import ServerSideDatatableView
from django.urls import reverse

DJANGO_VERSION = get_version()
urlpatterns = None

class ServerSideDatatableTestView(ServerSideDatatableView):
    columns = ['username', 'email']


if DJANGO_VERSION >= '2.0':
    from django.urls import path
    urlpatterns = [
        path('test-view/', ServerSideDatatableTestView.as_view(), name='test-view'),
    ]
else:
    from django.conf.urls import url
    urlpatterns = [
        url('test-view/', ServerSideDatatableTestView.as_view(), name='test-view')
    ]


@pytest.mark.django_db
def test_serverside_datatable_view(client, sample_queryset):
    ServerSideDatatableTestView.queryset = sample_queryset

    with override_settings(ROOT_URLCONF=__name__):
        _url = reverse('test-view')
        response = client.get(f"{_url}?iDisplayStart=0&iDisplayLength=10&iSortCol_0=0&sSortDir_0=asc&sEcho=1&iSortingCols=1")
        assert response.status_code == 200
        data = response.json()
        assert 'aaData' in data
        assert len(data['aaData']) == 5
        assert data['iTotalDisplayRecords'] == '5'
        assert data['iTotalRecords'] == '5'
        assert data['sEcho'] == '1'