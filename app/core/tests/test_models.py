"""
Test Models
"""

from django.test import TestCase
from django.contrib.auth import get_user_model # noqa


class ModelTests(TestCase):
    """Test models"""

    def test_create_user_with_email_successful(self):
        """Test creating user with email successfully"""
