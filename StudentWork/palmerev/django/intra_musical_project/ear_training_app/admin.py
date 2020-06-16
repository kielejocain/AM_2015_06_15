from django.contrib import admin
from .models import Note
from .models import Interval
from .models import IntervalType
from .models import Scale
from .models import ScaleType
from .models import Chord
from .models import ChordType
from .models import CourseSelection
from .models import CourseContents
from .models import CourseProgress
from .models import ExercisePage
from .models import Exercise

# Register your models here.
admin.site.register(Note)
admin.site.register(Interval)
admin.site.register(IntervalType)
admin.site.register(Scale)
admin.site.register(ScaleType)
admin.site.register(Chord)
admin.site.register(ChordType)
admin.site.register(CourseSelection)
admin.site.register(CourseContents)
admin.site.register(CourseProgress)
admin.site.register(ExercisePage)
admin.site.register(Exercise)
