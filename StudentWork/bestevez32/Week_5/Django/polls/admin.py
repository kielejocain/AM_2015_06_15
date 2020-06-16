from django.contrib import admin

# register your models here
from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)


