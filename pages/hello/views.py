from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'index.html'


class AboutPageView(TemplateView):  # new
    template_name = 'about.html'
