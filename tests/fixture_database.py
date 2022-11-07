import pytest
from django.contrib.auth.models import User

"""
"""
@pytest.fixture()
def user_1(db): #this fixture connect with database therefore, we need to take in db special object
    return User.objects.create_user("test-user")

@pytest.mark.django_db
def test_set_check_password(user_1):
    user_1.set_password("new-password")
    assert user_1.check_password("new-password") is True
#note: user_1 fixture is come from the same test file
def test_set_check_password1(user_1):
    print('check-user1')
    assert user_1.username == "test-user"

def test_set_check_password2(user_1):
    print('check-user2')
    assert user_1.username == "test-user"

#note: new_user and new_user2 come from file conftest.py
def test_new_user(new_user):
    print(new_user.first_name)
    assert new_user.first_name == "MyName"

def test_new_user(new_user2):
    print(new_user2.is_staff)
    assert new_user2.is_staff