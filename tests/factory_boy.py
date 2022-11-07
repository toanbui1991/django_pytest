import pytest
import factory
from faker import Faker
fake = Faker()

from django.contrib.auth.models import User
from core.app1 import models
from pytest_factoryboy import register


"""
Note about pytest-factoryboy:
    - factory boy is class approach of fixture
    - it is use to test model definition

"""

def test_product(db, product_factory):
    product = product_factory.create()
    print(product.description)
    assert True