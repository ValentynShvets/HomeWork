# from django.db.migrations import loader
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Choice, Question


#
#
# def index(request):
#     questions = Question.objects.all()
#     # res = ""
#     # for q in questions:
#     #     res += str(q.id) + ". " + q.question + "<br>"
#     print(questions)
#     return render(request, "polls/index.html", {'question': questions})
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


#
# def detail(request, question_id):
#     questions = get_object_or_404(Question, pk=question_id)
#     # rez = "<H3>" + question.question + "<H3>: <br>"
#     # for answer in question.choice_set.all():
#     #     rez += answer.choice_text + " vote: " + str(answer.votes) + "<br>"
#     return render(request, "polls/details.html", {'questions': questions})
def detail(request, question_id):
    # question = Question.objects.get(pk=question_id)
    choice_list = Choice.objects.filter(question_id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    prev = question_id - 1
    nexts = question_id + 1
    last_question_id = len(Question.objects.filter())
    if question_id != last_question_id:
        next_question = Question.objects.filter(id=nexts)
        for i in next_question:
            next_questions = i
    else:
        next_questions = 0

    if question_id > 1:
        prev_question = Question.objects.filter(id=prev)
        for i in prev_question:
            prev_questions = i
    else:
        prev_questions = 0


    return render(request, 'polls/details.html',
                  {'question': question, 'choice': choice_list,
                   'prev': prev, 'next': nexts, 'last': last_question_id,
                   'prev_q': prev_questions, 'next_q': next_questions})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.POST.get('choice'):
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:details', args=(question.id,)))

    elif request.POST.get('minus'):
        selected_choice = question.choice_set.get(pk=request.POST['minus'])
        selected_choice.votes -= 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:details', args=(question.id,)))
