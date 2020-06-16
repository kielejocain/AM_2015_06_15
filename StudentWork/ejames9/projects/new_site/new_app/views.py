from django.shortcuts import render
from .models import Blog, Comment
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse

def register(request):
    if request.POST:
        user = User()
        user.username = request.POST['username']
        user.set_password(request.POST['password'])
        user.save()
        return HttpResponseRedirect('/')

    return render(request, 'new_app/register.html', {})

def login_view(request):

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        print user
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')

    return render(request, 'new_app/login.html', {})


@login_required(login_url='/login/')
def index(request):
    blog_list = Blog.objects.all()
    template = loader.get_template('new_app/index.html')
    context = RequestContext(request, {
        'blog_list': blog_list,
    })

    return HttpResponse(template.render(context))

@csrf_exempt
def details(request, id):
    blog = Blog.objects.filter(id=id)[0]
    comment_list = Comment.objects.filter(blog=blog)

    template = loader.get_template('new_app/details.html')
    context = RequestContext(request, {'blog': blog, 'comment_list': comment_list})

    if request.POST:
        print(request.POST)
        if "action" in request.POST:
            if request.POST["action"] == "Bye Bye":
                blog.delete()
                return HttpResponseRedirect("/")
        elif "submit" in request.POST:
            if request.POST["submit"] == "Submit Edit":
                blog.blog_text = request.POST["blog_text"]
                blog.name_text = request.POST["name_text"]
                blog.title_text = request.POST["title_text"]
                if "image" in request.FILES:
                    if request.FILES["image"] != '':
                        blog.image = request.FILES["image"]
                blog.save()
                print blog.image
                return HttpResponseRedirect("/")

    return HttpResponse(template.render(context))

def edit(request, id):
    blog = Blog.objects.filter(id=id)[0]
    comment_list = Comment.objects.filter(blog=blog)

    if request.POST:
        print(request.POST)
        blog.blog_text = request.POST["blog_text"]
        blog.name_text = request.POST["name_text"]
        blog.title_text = request.POST["title_text"]
        blog.save()
        return HttpResponseRedirect("/")

    return render(request, 'new_app/edit.html', {'blog': blog, 'comment_list': comment_list})

def create2(request, id):
    blog = Blog()

    if request.POST:
        save_blog(request, blog)
        return HttpResponseRedirect("/")

    return render(request, 'new_app/create2.html', {'blog': blog})

def save_blog(request, blog):
    blog.blog_text = request.POST["blog_text"]
    blog.title_text = request.POST["title_text"]
    blog.name_text = request.POST["name_text"]
    blog.pub_date = datetime.now()
    # pub_date_string = request.POST["pub_date"]
    # pub_date = datetime.strptime(pub_date_string, '%Y-%m-%d')
    # blog.pub_date = pub_date

    blog.save()

@csrf_exempt
def api_delete_comment(request):
    if request.POST:
        print request.POST
        text = request.POST["text"]
        print text
        del_comment = Comment.objects.get(cmt_text__exact=text)
        del_comment.delete()
    return HttpResponse(str(text))

@csrf_exempt
def api_add_comment(request):

    if request.POST:
        print request.POST
        comment = Comment()
        blog_id = request.POST["blog_id"]
        comment.blog = Blog.objects.filter(id=blog_id)[0]
        comment.cmtr_name = request.POST["cmtr_name"]
        comment.cmt_text = request.POST["cmt_text"]
        comment.pub_time = datetime.now()
        comment.save()
        print comment

        pub_time = str(comment.pub_time)
        print pub_time
    return HttpResponse(pub_time)
