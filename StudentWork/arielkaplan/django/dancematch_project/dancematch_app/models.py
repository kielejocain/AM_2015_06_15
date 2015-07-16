from django.db import models

class Dancer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    bio = models.TextField()
    date_joined = models.DateField('date joined')
    active_member = models.BooleanField()
    # photo = ImageField() https://docs.djangoproject.com/en/1.8/ref/models/fields/

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Dance(models.Model):
    name = models.CharField(default='', max_length=200)
    description = models.TextField(default='')
    dance_community = models.ManyToManyField(
        Dancer,
        through='DancePrefs',
        through_fields=('dance', 'dancer')
    )

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class DancePrefs(models.Model):
    dance = models.ForeignKey(Dance)
    dancer = models.ForeignKey(Dancer)

    BRAND_NEW = 'New'
    BEGINNER = 'Beginner'
    BEYOND_BEGINNING = 'Beyond Beginning'
    INTERMEDIATE = 'Intermediate'
    ADVANCED = 'Advanced'
    EXPERT = 'Expert'
    LEVEL_CHOICES = (
        (BRAND_NEW, 'Brand New'),
        (BEGINNER, 'Beginner'),
        (BEYOND_BEGINNING, 'Beyond Beginning'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced'),
        (EXPERT, 'Expert')
    )

    DANCE_BUDDY = "Social Dance Buddy"
    CLASS_BUDDY = "Class Buddy"
    SOCIAL = "Social Dancing"
    COMP_ROUTINE = "Competition Routine"
    COMP_STRICTLY = "Competition Strictly"
    COMP_OTHER = "Other Competition"
    DANCE_GOALS = (
        (DANCE_BUDDY, 'Social Dance Buddy'),
        (CLASS_BUDDY, 'Class Buddy'),
        (SOCIAL, 'Social Dancing'),
        (COMP_ROUTINE, 'Competition Routine'),
        (COMP_STRICTLY, 'Competition Strictly'),
        (COMP_OTHER, 'Other Competition')
    )

    ACTIVE = "Active"
    CASUAL = "Casual"
    INACTIVE = "Inactive"
    DANCE_ACTIVITY = (
        (ACTIVE, 'Active'),
        (CASUAL, 'Casual'),
        (INACTIVE, 'Inactive')
    )

    lead = models.BooleanField()
    lead_level = models.CharField(max_length=200,
                                  choices=LEVEL_CHOICES,
                                  default=BRAND_NEW)
    follow = models.BooleanField()
    follow_level = models.CharField(max_length=200,
                                    choices=LEVEL_CHOICES,
                                    default=BRAND_NEW)
    goals = models.CharField(max_length=200,
                             choices=DANCE_GOALS,
                             default=SOCIAL)
    activity = models.CharField(max_length=200,
                                choices=DANCE_ACTIVITY,
                                default=ACTIVE)
    notes = models.TextField()

    def __str__(self):
        return str(self.dancer) + "'s " + str(self.dance) + ' prefs'

    def __unicode__(self):
        return str(self.dancer) + "'s " + str(self.dance) + ' prefs'

class Schedule(models.Model):
    pass

class Location(models.Model):
    pass