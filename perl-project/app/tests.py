import unittest
from django.test import Client

class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_train_search(self):
        # Issue a GET request.
        response = self.client.get('/train/search/?origin=MUM&destination=DEL')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/train/search/?origin=MUM&destination=')
        self.assertEqual(response.status_code, 400)

        response = self.client.get('/train/search/?origin=&destination=DEL')
        self.assertEqual(response.status_code, 400)

