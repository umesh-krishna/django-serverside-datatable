import os
from django.conf import settings
from django.core import mail
import django
import pytest


@pytest.fixture(scope='session', autouse=True)
def django_settings():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tests.settings')
    django.setup()
    
@pytest.fixture(autouse=True)
def _dj_autoclear_mailbox():
    if not settings.configured:
        return

    if hasattr(mail, 'outbox'):
        del mail.outbox[:]

@pytest.fixture
def mock_request():
    from django.test import RequestFactory
    from django.contrib.auth.models import User
    request = RequestFactory().get('/fake-url')
    return request

@pytest.fixture
def sample_queryset():
    from django.contrib.auth.models import User
    User.objects.create(username="Alice", email="alice@example.com")
    User.objects.create(username="Bob", email="bob@example.com")
    User.objects.create(username="Charlie", email="charlie@example.com")
    User.objects.create(username="David Beckham", email="david.beckham@example.com")
    User.objects.create(username="David Warner", email="david.warner@example.com")
    return User.objects.all()
