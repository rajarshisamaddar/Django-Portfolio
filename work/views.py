from django.http import HttpResponse
from django.template import loader
from .models import Work


def work(request):
    works = Work.objects.all().values()
    template = loader.get_template('work.html')
    context = {
        'works': works,
    }
    return HttpResponse(template.render(context, request))
