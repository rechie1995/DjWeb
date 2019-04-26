from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class ViewTests(TestCase):
    # 视图测试

    def test_login_view_status_code(self):
        url = reverse('admin:login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_logout_view_status_code(self):
        url = reverse('admin:logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)