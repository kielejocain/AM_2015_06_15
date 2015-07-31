from django.db import models
from django.contrib.auth.models import User


class UserProfiles(models.Model):
    uppath = 'user_logo/'
    user = models.ForeignKey(User, unique=True)
    user_logo = models.ImageField(upload_to=uppath, blank=True, null=True)
    join_date = models.DateTimeField('date joined')

    def __str__(self):
        return self.join_date

    def __unicode__(self):
        return self.first_name
        return self.last_name
        return self.username
        return self.password
        return self.join_date


class Blog(models.Model):
    user_profile = models.ForeignKey(UserProfiles, null=True)
    name_text = models.CharField(max_length=20)
    title_text = models.CharField(max_length=200)
    blog_text = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.blog_text
        return self.title_text
        return self.name_text

    def __unicode__(self):
        return self.blog_text
        return self.title_text
        return self.name_text

    def published(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Comment(models.Model):
    blog = models.ForeignKey(Blog)
    cmt_text = models.TextField()
    cmtr_name = models.CharField(max_length=20)
    pub_time = models.DateTimeField('time_published')

    def __str__(self):
        return self.cmt_text
        return self.cmtr_name
        return self.blog
        return self.pub_time

    def __unicode__(self):
        return self.cmt_text
        return self.cmtr_name
        return self.blog
        return self.pub_time
