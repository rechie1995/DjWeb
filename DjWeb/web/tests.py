from django.test import Client, TestCase
from django.urls import reverse

# Create your tests here.
class ViewTests(TestCase):
    # 视图测试

    def test_index_view_status_code(self):
        url = reverse('web:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)