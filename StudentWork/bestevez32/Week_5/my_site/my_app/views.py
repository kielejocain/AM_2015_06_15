from django.shortcuts import render
from .models import Character
# Create your views here.
def index(request):
    object_list = Character.objects.all()
    template = loader.get_template('my_app/index.html')
    context = RequestContext(request, {
        'object_list': object_list,
    })
    return HttpResponse(template.render(context))