import unittest
from flask_sqlalchemy import SQLAlchemy
from src.services.user import UserService

db = SQLAlchemy()


class TestCase(unittest.TestCase):
    def test_db(self):
        bind = db.metadata.bind
        assert bind == None

    def test_func(self):
        us = UserService()
        ret = us.get_user()

        assert ret == 200


if __name__ == '__main__':
    unittest.main()
