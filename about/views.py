from django.http import HttpResponse
from django.template import loader
from .models import About, AboutParagraph, AboutSkill


def about(request):
    about = About.objects.all().values()
    aboutparagraph = AboutParagraph.objects.all().values()
    aboutskill = AboutSkill.objects.all().values()
    template = loader.get_template('about.html')
    context = {
        'about': about,
        'aboutparagraph': aboutparagraph,
        'aboutskill': aboutskill,
    }
    return HttpResponse(template.render(context, request))
