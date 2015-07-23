from django.shortcuts import render
from .models import Blog
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    blog_list = Blog.objects.all()
    template = loader.get_template('new_app/index.html')
    context = RequestContext(request, {
        'blog_list': blog_list,
    })
    return HttpResponse(template.render(context))

def details(request, id):
    blog = Blog.objects.filter(id=id)[0]
    template = loader.get_template('new_app/details.html')
    context = RequestContext(request, {
        'blog': blog,
    })
    return HttpResponse(template.render(context))

def edit(request, id):
    blog = Blog.objects.filter(id=id)[0]

    if request.POST:
        print(request.POST)
        object.blog_text = request.POST["blog_text"]
        object.name_text = request.POST["name_text"]
        object.title_text = request.POST["title_text"]
        blog.save()
        return HttpResponseRedirect("/")

    return render(request, 'new_app/edit.html', {'blog': blog})
