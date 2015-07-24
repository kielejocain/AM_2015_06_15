from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from django.core.urlresolvers import reverse

from django.shortcuts import get_object_or_404, render

from .models import Registrant, Camper, Rate

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    registrants_list = Registrant.objects.order_by("-last_name")[:]

    template = loader.get_template('seabeck_draft/index.html')
    context = RequestContext(request, {'registrants_list': registrants_list})

    return HttpResponse(template.render(context))


def detail(request, registrant_id):
    registrant = get_object_or_404(Registrant, pk=registrant_id)
    return render(request, 'seabeck_draft/detail.html', {'registrant': registrant})


def edit(request, registrant_id):

    # filtered_question_list = Question.objects.filter(id=question_id)
    #
    # if len(filtered_question_list) > 0:
    #     print("FOUND")
    #     question = filtered_question_list[0]
    # else:
    #     print("NEW")
    #     question = Question()
    #
    # if request.POST:
    #     save_question(request, question)
    #     return HttpResponseRedirect("/polls/")
    #
    # return render(request, 'polls/edit.html', {'question': question})

    registrant = get_object_or_404(Registrant, pk=registrant_id)

    filtered_registrant_list = Registrant.objects.filter(id=registrant_id)

    if len(filtered_registrant_list) > 0:
        registrant = filtered_registrant_list[0]
    else:
        registrant = Registrant()

    if request.POST:
        print(request.POST)
        registrant.first_name = request.POST["first_name"]
        registrant.last_name = request.POST["last_name"]
        registrant.email = request.POST["email"]
        registrant.phone = request.POST["phone"]
        registrant.save()
        return HttpResponseRedirect("/")

    return render(request, 'seabeck_draft/edit.html', {'registrant': registrant})


def add_camper(request, registrant_id):


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
#
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#
# def vote(request, question_id):
#     p = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = p.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': p,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
#
