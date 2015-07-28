from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext, loader
# Create your views here.
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
#from .models import ExercisePage
from .models import Exercise
from random import choice, sample, randint
import json

def index(request):
    return HttpResponse("New index page!")

def course_selection(request):
    #context = { "": , "":  }
    return render(request, 'ear_training_app/courses.html')
    #return HttpResponse("Course Selection Page")

def course(request, course_type):
    # view logic
    #
    return HttpResponse("Course Content Page")

def progress_page(request):
    return HttpResponse("Course Progress Page")

# def exercise_page(request, course_type, exercise_id):
#     return HttpResponse("Exercise Page")

def exercise_page(request):
    possible_answers = get_interval_set(request)
    num_intervals = 4
    #mark a random interval as the correct answer
    answer_index = randint(0, num_intervals - 1)
    answer = possible_answers[answer_index]
    answer["correct"] = "1"
    context = {"possible_answers": possible_answers, "answer": answer }
    return render(request, 'ear_training_app/interval_exercise.html', context)
    #return HttpResponse(get_interval_set(request))

#helper function for exercise_page
def get_interval_set(request):
    interval_list = Interval.objects.all()
    num_intervals = 4
    interval_set = sample(interval_list, num_intervals)
    interval_obj = [
        {
            "interval_name": interval.name.quality.lower(),
            "top_note": {
                "octave": interval.top_note.octave,
                "name": interval.top_note.name.lower()
            },
            "bottom_note": {
                "octave": interval.bottom_note.octave,
                "name": interval.bottom_note.name.lower()
            }

        } for interval in interval_set]
    #output = json.dumps(interval_obj)
    return interval_obj

    # name = interval.name.quality
    # top_name = interval.top_note.name
    # top_octave = interval.top_note.octave
    # bottom_name = interval.bottom_note.name
    # bottom_octave = interval.bottom_note.octave
    # data_item = {
    #     "interval_name": name,
    #     "top_note": {
    #     "name": top_name,
    #     "octave": top_octave
    #     },
    #     "bottom_note": {
    #     "name": bottom_name,
    #     "octave": bottom_octave
    #     }
    # }
    # output = json.dumps(data_item)
    # print "interval set:", interval_set
    # print "interval:", interval
    #return HttpResponse(output)

# def index(request):
#     note_list = Note.objects.order_by('-frequency')
#     template = loader.get_template('ear_training_app/index.html')
#     context = RequestContext(request, {
#         'note_list': note_list,
#     })
#     return HttpResponse(template.render(context))
#
# def note_list(request):
#     notes = Note.objects.all()
#     notes_data = [", ".join([x.name, str(x.frequency)]) for x in notes]
#     output = "\t".join(notes_data)
#     return HttpResponse(output)
#
# def detail(request, note_id):
#     note = get_object_or_404(Note, id=note_id)
#     context = { "note": note }
#     return render(request, 'ear_training_app/detail.html', context)
#
# def results(request, note_id):
#     note_list = Note.objects.order_by('-frequency')
#     chosen_note = Note.objects.filter(id=note_id)[0]
#     chosen_note.votes += 1
#     chosen_note.save()
#     context = { "note_list": note_list, "note": chosen_note }
#     return render(request, 'ear_training_app/results.html', context)
#
# def edit(request, note_id):
#     filtered_notes = Note.objects.filter(id=note_id)
#     if filtered_notes:
#         print "notes in edit"
#         note = filtered_notes[0]
#     else:
#         #note = Note()
#         print "NO NOTES!"
#     if request.POST:
#         print(request.POST)
#         note.name = request.POST["name"]
#         note.votes = request.POST["votes"]
#         note.save()
#         return HttpResponseRedirect("/")
#
#     context = { "note": note }
#     return render(request, 'ear_training_app/edit.html', context)
