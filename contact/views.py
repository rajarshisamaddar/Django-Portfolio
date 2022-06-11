from tabnanny import check
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from .models import Contact, ContactFindMe, ContactParagraph
import random

check = 0
operation = ""
number_one = 0
number_two = 0


def error(request):
    template = loader.get_template('error_page.html')
    return HttpResponse(template.render())


def contact(request):
    contactparagraph = ContactParagraph.objects.all().values()
    contactfindme = ContactFindMe.objects.all().values()
    op_type = round(random.random())
    number_one = random.randint(8, 14)
    number_two = random.randint(1, 7)
    global check
    if(op_type == 0):
        operation = "-"
        check = number_one - number_two
    else:
        operation = "+"
        check = number_one + number_two
    context = {
        'contactparagraph': contactparagraph,
        'contactfindme': contactfindme,
        'number_one': number_one,
        'number_two': number_two,
        'operation': operation,
    }
    template = loader.get_template('contact.html')
    return HttpResponse(template.render(context, request))


@csrf_exempt
def message(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phoneNumber = request.POST['phoneNumber']
        subject = request.POST['subject']
        messageR = request.POST['message']
        messageR = request.POST['message']
        captcha = request.POST['captcha']
        if(int(captcha) == check):
            contact = Contact(
                name=name, email=email, phone=phoneNumber, subject=subject, message=messageR)
            contact.save()
            return redirect('/contact/')
        else:
            return redirect('error')
