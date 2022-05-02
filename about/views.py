from django.http import HttpResponse
from django.template import loader
from .models import About


def about(request):
    about = About.objects.all().values()
    template = loader.get_template('about.html')
    context = {
        'about': about,
    }
    return HttpResponse(template.render(context, request))
