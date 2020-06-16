from django.db import models

# Create your models here.
class Note(models.Model):
    name = models.CharField(max_length=3, blank=True)
    #frequency = models.FloatField(default=0.0, null=True, blank=True)
    octave = models.PositiveSmallIntegerField(default=0)

    def __unicode__(self): #__str__ in python3
        return str(self.name) + str(self.octave)

    def __str__(self): #__str__ in python3
        return str(self.name) + str(self.octave)

class IntervalType(models.Model):
    '''A list of predefined interval types / qualities'''
    quality = models.CharField(max_length=20, null=True, blank=True)

    def __unicode__(self): #__str__ in python3
        return "quality: " + str(self.quality)

    def __str__(self): #__str__ in python3
        return "quality: " + str(self.quality)

class Interval(models.Model):
    '''Two notes a specific distance (interval) apart.'''
    #TODO: make function to generate name based on top_note and bottom_note values
    name = models.ForeignKey(IntervalType, null=True, blank=True)
    top_note = models.ForeignKey(Note, related_name="top_note", null=True, blank=True)
    bottom_note = models.ForeignKey(Note, related_name="bottom_note", null=True, blank=True)

    def __unicode__(self): #__str__ in python3
        return "interval: " + str(self.name) + ", top: " + str(self.top_note) + ", bottom: " + str(self.bottom_note)

    def __str__(self): #__str__ in python3
        return "interval: " + str(self.name) + ", top: " + str(self.top_note) + ", bottom: " + str(self.bottom_note)

class ScaleType(models.Model):
    '''A list of scale types / qualities'''
    quality = models.CharField(max_length=25, null=True, blank=True)

    def __unicode__(self): #__str__ in python3
        return "(quality: " + str(self.quality) + ")"

    def __str__(self): #__str__ in python3
        return "(quality: " + str(self.quality) + ")"

class Scale(models.Model):
    '''A collection of notes organized by frequency.'''
    name = models.CharField(max_length=50, blank=True)
    tonic = models.ForeignKey(Note, null=True)
    #quality = models.PositiveSmallIntegerField(default=1) #major, minor, other
    quality = models.ForeignKey(ScaleType, null=True)
    ascending = models.BooleanField(default=True)

    def __unicode__(self): #__str__ in python3
        return "scale: " + str(self.name) + ", " + "quality: " + str(self.quality) + ", " + "ascending: " + str(self.ascending)

    def __str__(self): #__str__ in python3
        return "scale: " + str(self.name) + ", " + "quality: " + str(self.quality) + ", " + "ascending: " + str(self.ascending)

class ChordType(models.Model):
    '''A list of chord types / qualities'''
    quality = models.CharField(max_length=20, null=True, blank=True)

    def __unicode__(self): #__str__ in python3
        return "(quality: " + str(self.quality) + ")"

    def __str__(self): #__str__ in python3
        return "(quality: " + str(self.quality) + ")"

class Chord(models.Model):
    '''A set of at least three notes.'''
    root = models.ForeignKey(Note, null=True)
    quality = models.ForeignKey(ChordType, null=True)

    def __unicode__(self): #__str__ in python3
        return "(root: " + str(self.root) + ", " + "quality: " + str(self.quality) + ")"

    def __str__(self): #__str__ in python3
        return "(root: " + str(self.root) + ", " + "quality: " + str(self.quality) + ")"

class CourseSelection(models.Model):
    ''' Page containing all courses '''
    pass

class CourseProgress(models.Model):
    ''' Page where users can see their progress, exercises they've completed, learning stats, etc. '''
    pass

class CourseContents(models.Model):
    ''' Page showing a list of all exercises in a course. '''
    pass

class Exercise(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    interval_answer = models.ForeignKey(Interval, null=True, blank=True)
    scale_answer = models.ForeignKey(Scale, null=True, blank=True)
    chord_answer = models.ForeignKey(Chord, null=True, blank=True)

    def __unicode__(self): #__str__ in python3
        return str(self.name)

    def __str__(self): #__str__ in python3
        return str(self.name)


class ExercisePage(models.Model):
    exercise = models.ForeignKey(Exercise, null=True, blank=True)

    def __unicode__(self): #__str__ in python3
        return str(self.exercise)

    def __str__(self): #__str__ in python3
        return str(self.exercise)
