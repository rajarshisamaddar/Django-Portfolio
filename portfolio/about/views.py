from django.http import HttpResponse
from django.template import loader


def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())
