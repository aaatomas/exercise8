from django.test import TestCase
from django.urls import reverse

class IndexViewTest(TestCase):
    def test_index_view_status_code(self):
        response = self.client.get(reverse('app_hello:index'))
        self.assertEqual(response.status_code, 200)