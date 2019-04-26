from django.views.generic import TemplateView

# Create your views here.

class LoginView(TemplateView):

    template_name = "admin/login.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)