from django.test import TestCase
from django.urls import reverse
# Create your tests here.
# TODO: 添加数据，表单测试


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

    def test_register_view_status_code(self):
        url = reverse('admin:register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
