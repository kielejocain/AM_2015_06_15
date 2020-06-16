from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Question, Choice
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

import json
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([p.question_text for p in latest_question_list])
#     return HttpResponse(output)


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return HttpResponse(template.render(context))


# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html', {'question': question})


@csrf_exempt
def api_save_question(request):
    print(request.POST)
    question = Question()
    question.question_text = request.POST["text"]
    question.pub_date = datetime.now()
    question.save()
    return HttpResponse('{"id":' + str(question.id) + '}')


def save_question(request, question):
    question.question_text = request.POST["question_text"]

    pub_date_string = request.POST["pub_date"]
    pub_date = datetime.strptime(pub_date_string, '%Y-%m-%d')
    question.pub_date = pub_date

    question.save()


def edit(request, question_id):
    # question = Question.objects.get(pk=question_id)
    # question = get_object_or_404(Question, pk=question_id)
    # question = Question.objects.filter(id=question_id)[0]
    filtered_question_list = Question.objects.filter(id=question_id)

    if len(filtered_question_list) > 0:
        print("FOUND")
        question = filtered_question_list[0]
    else:
        print("NEW")
        question = Question()

    if request.POST:
        save_question(request, question)
        return HttpResponseRedirect("/polls/")

    return render(request, 'polls/edit.html', {'question': question})


#
# def add(request):
#     question = Question()
#
#     if request.POST:
#         save_question(request, question)
#         return HttpResponseRedirect("/polls/")
#
#     return render(request, 'polls/edit.html', {'question': question})


def ajax_form(request):
    return render(request, 'polls/ajax_form.html')


# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


# def edit_shirt(request, camper_id, attend_id):
#     if request.POST:
#         shirt_id = request.POST["shirt_id"]
#         order = ShirtOrder()
#         order.camper = Camper.objects.get(pk=camper_id)
#         order.attend = Camper.objects.get(pk=attend_id)
#         order.shirt = Shirt.objects.get(pk=shirt_id)
#         order.save()

def api_questions(request):
    question_list = Question.objects.all()
    output = []
    for q in question_list:
        qdata = {}
        qdata["id"] = q.id
        qdata["text"] = q.question_text
        output.append(qdata)
    return HttpResponse(json.dumps(output))


def api_get_question_name(request, question_id):
    question = Question.objects.filter(id=question_id)[0]
    return HttpResponse(json.dumps({"text": question.question_text}))


def api_choices(request, question_id):
    question = Question.objects.filter(id=question_id)[0]
    output = []
    for c in Choice.objects.filter(question=question):
        output.append({"text": c.choice_text, "id": c.id})
    return HttpResponse(json.dumps(output))


def data(request):
    question_list = Question.objects.all()
    json_data = "[]"
    if len(question_list) > 0:

        output = []
        for q in question_list:
            qdata = {}
            qdata["id"] = q.id
            qdata["text"] = q.question_text
            qdata["choices"] = []
            for c in Choice.objects.filter(question=q):
                cdata = {}
                cdata["id"] = c.id
                cdata["text"] = c.choice_text
                cdata["votes"] = c.votes
                qdata["choices"].append(cdata)
            output.append(qdata)
        json_data = json.dumps(output, indent=4)
    return HttpResponse(json_data, content_type='application/json')


def api_vote(request):
    votes = "undefined"
    if request.POST:
        question_id = request.POST["question_id"]
        p = get_object_or_404(Question, pk=question_id)
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
        selected_choice.votes += 1
        selected_choice.save()
        votes = selected_choice.votes
    return HttpResponse('{"votes":' + votes + '}', content_type='application/json')
