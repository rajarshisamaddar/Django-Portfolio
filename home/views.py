from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from home.models import Subscriber
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect


def index(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


@csrf_exempt
def subscribe(request):
    if request.method == "POST":
        email = request.POST['email']
        subscribe = Subscriber(email=email)
        subscribe.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def page_not_found_view(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(template.render())
