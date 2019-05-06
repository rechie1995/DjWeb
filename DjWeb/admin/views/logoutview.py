from django.views.generic import TemplateView

# Create your views here.


class LogoutView(TemplateView):

    template_name = "admin/logout.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
