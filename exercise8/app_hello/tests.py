from django.test import TestCase
from django.urls import reverse

class IndexViewTest(TestCase):
    def test_index_view_status_code(self):
        response = self.client.get(reverse('app_hello:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_contains_correct_text(self):
        response = self.client.get(reverse('app_hello:index'))
        self.assertContains(response, "Hello, world. You're at the 'app_hello' index...")

    def test_index_view_returns_correct_template(self):
        response = self.client.get(reverse('app_hello:index'))
        self.assertTemplateUsed(response, 'app_hello/index.html')
