from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def index(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

# def resume(request):
#     pdf_folder = '/home/galander/Desktop/Projekty/django-pdf-generator/django-pdf/generator/static/pdfs'
#     response = HttpResponse(pdf_folder, content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="nowy.pdf"'
#     return HttpResponse(template.render())

def page_not_found_view(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(template.render())
