import pytest
from django.contrib.auth import get_user_model

@pytest.mark.django_db
def test_create_user():
    User = get_user_model()
    user = User.objects.create_user(
        username='testuser',
        email='testuser@example.com',
        password='testpass123'
    )
    assert User.objects.count() == 1
    assert user.username == 'testuser'
    assert user.email == 'testuser@example.com'
    assert user.check_password('testpass123')