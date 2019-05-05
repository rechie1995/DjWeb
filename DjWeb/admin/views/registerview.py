from django.views.generic import TemplateView

# Create your views here.


class RegisterView(TemplateView):

    template_name = "admin/register.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
