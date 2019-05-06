from django.views.generic import TemplateView
from ..forms import LoginForm
# Create your views here.


class LoginView(TemplateView):

    template_name = "admin/login.html"

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        kwargs['form'] = form
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        return {'username': username, 'password': password}
