from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse,  Http404
from django.template import loader

from .models import Question


def index(req):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # template = loader.get_template('polls/index.html')
    context = {
        # 'latest_question_list': latest_question_list
        'lists': latest_question_list
    }
    return render(req, 'polls/index.html', context)
    # return HttpResponse(template.render(context, req))


def detail(req, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.doesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk = question_id)
    return render(req, 'polls/detail.html', {'question': question})
    # return HttpResponse("You' re looking at question %s." % question_id)


def results(req, question_id):
    return HttpResponse("You' re looking at the results of question %s." % question_id)


def vote(req, question_id):
    return HttpResponse("You' re voting on question %s." % question_id)
