# Django Serverside Datatable
[![build][build-image]][build-url]
[![pypi][pypi-image]][pypi-url]
[![Downloads](https://pepy.tech/badge/django-serverside-datatable)](https://pepy.tech/project/django-serverside-datatable)


[build-image]: https://github.com/umesh-krishna/django-serverside-datatable/workflows/Tests/badge.svg
[build-url]: https://github.com/umesh-krishna/django-serverside-datatable/actions
[pypi-image]: https://img.shields.io/pypi/v/django-serverside-datatable.svg?style=flat
[pypi-url]: https://pypi.org/project/django-serverside-datatable/

This is a simple package that let you use Server-side Datatable in your Django Project

Supports datatable features such as Pagination, Search, etc...

## Install

```
pip install django-serverside-datatable
```


## How to use

Create a django View that inherits from  **ServerSideDatatableView**.
Example (backend):

```python
# views.py

from django_serverside_datatable.views import ServerSideDatatableView


class ItemListView(ServerSideDatatableView):
	queryset = models.Item.objects.all()
	columns = ['name', 'code', 'description']


# urls.py
# add the following line to urlpatterns

path('data/', views.ItemListView.as_view()), 

```

Example (frontend):

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<link rel="stylesheet" href="https://cdn.datatables.net/1.10.19/css/jquery.dataTables.min.css">
	</head>
	<body>
		<h1>Items</h1>
		<hr>
		<table id="items-table">
			<thead>
				<tr>
					<th>Name</th>
					<th>Code</th>
					<th>Description</th>
				</tr>
			</thead>
			<tbody></tbody>
		</table>

		<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
		<script src="https://cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js"></script>
		<script language="javascript">
			$(document).ready(function () {
				$('#items-table').dataTable({
					serverSide: true,
					sAjaxSource: "http://127.0.0.1:8000/data/",  // new url
                                        columns: [
                                            {name: "name", data: 0},
                                            {name: "code", data: 1},
                                            {name: "description", data: 2},
                                        ],
				});
			});
		</script>
	</body>
</html>
```

For further customization of Datatable, you may refer the Datatable official documentation.
