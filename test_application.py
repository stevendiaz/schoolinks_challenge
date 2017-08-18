import unittest
import json
from run import app
from app import create_app
from app.models import MasterSchedule, Student
from app.main.forms import SchoolForm
import urllib

class ApplicationTests(unittest.TestCase):

    def setUp(self):
        self.created_app = create_app('default')
        self.app_context = self.created_app.app_context()
        self.app_context.push()
        self.app = self.created_app.test_client()
        self.app.testing = True

    def tearDown(self):
        self.app_context.pop()

    def test_register_page_returns_200(self):
        result = self.app.get('/register/texas')
        self.assertEqual(result.status_code, 200)

    def test_landing_page_returns_200(self):
        query = urllib.urlencode({'science': 9, 'math': 10, 'history': 11, 'elective': 12, 'english': 13})
        result = self.app.get('/landing/texas', query_string=query)
        self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
    unittest.main()
