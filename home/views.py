from django.http import HttpResponse
from django.template import loader
from home.models import Blog, Subscriber
from django.http import HttpResponseRedirect


def index(request):
    blog = Blog.objects.all().values().order_by('?')
    context = {
        'blog': blog,
    }
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context, request))


def blog(request, slug):
    blogPost = Blog.objects.filter(slug=slug).first()
    context = {
        'blogPost': blogPost,
    }
    template = loader.get_template('blog.html')
    return HttpResponse(template.render(context, request))


def search(request):
    if request.method == "GET":
        query = request.GET['query']
        if len(query) > 75:
            blogPost = Blog.objects.none()
        else:
            allBlogTitle = Blog.objects.filter(title__icontains=query)
            allBlogContent = Blog.objects.filter(content__icontains=query)
            blogPost = allBlogContent.union(allBlogTitle)
        context = {
            'blogPost': blogPost,
            'query': query,
        }
        template = loader.get_template('search.html')
        return HttpResponse(template.render(context, request))


def subscribe(request):
    if request.method == "POST":
        email = request.POST['email']
        subscribe = Subscriber(email=email)
        subscribe.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def page_not_found_view(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(template.render())
