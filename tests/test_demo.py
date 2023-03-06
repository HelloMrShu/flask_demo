import unittest
from src.services.user import UserService


def test_func(self):
    us = UserService()
    ret = us.get_user()

    assert ret == 200
