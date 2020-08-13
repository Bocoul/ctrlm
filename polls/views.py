from django.shortcuts import render, get_object_or_404
from django.urls import reverse
# Create your views here.
from django.http import HttpResponse,  Http404, HttpResponseRedirect
from django.template import loader

from .models import Question, Choice


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
    question = get_object_or_404(Question, pk=question_id)
    return render(req, 'polls/results.html', {'question': question})


# def vote(req, question_id):
    # return HttpResponse("You' re voting on question %s." % question_id)
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
