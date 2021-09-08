from django.test import TestCase
from django.contrib.auth.models import User
from business.models import Businesses
# Create your tests here.

import pytest


@pytest.mark.django_db
def test_create_business():
    user = {
        "username": "user1",
        "password": "123",
        "email": "test@test.com"
    }
    data = {
        "name": "business1",
        "address": "address 123",
        "employee_size": 20
    }
    user_obj = User(**user)
    business_obj = Businesses(owner=user_obj, **data)
    assert business_obj.name == data["name"]
    assert business_obj.owner == user_obj
    assert business_obj.employee_size == data["employee_size"]
    assert business_obj.address == data["address"]
