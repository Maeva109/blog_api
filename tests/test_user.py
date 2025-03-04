from django.test import TestCase

# Create your tests here.
import pytest
from blog_api.users.models import User

def test_user_model_with_valid_name_and_email():
    user = User(nom="John Doe", email="john.doe@example.com")
    assert user.nom == "John Doe"
    assert user.email == "john.doe@example.com"
    assert str(user) == "John Doe"