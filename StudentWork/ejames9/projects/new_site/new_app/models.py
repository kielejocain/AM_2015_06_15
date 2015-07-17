from django.db import models


##class Account(models.Model):

##class Person(models.Model)

class Blog(models.Model):
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

    def __unicode__(self):
        return self.cmt_text
        return self.cmtr_name
