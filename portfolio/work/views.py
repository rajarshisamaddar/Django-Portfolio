from django.http import HttpResponse
from django.template import loader


def work(request):
    template = loader.get_template('work.html')
    return HttpResponse(template.render())
