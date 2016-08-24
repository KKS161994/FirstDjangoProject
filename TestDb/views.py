from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Questions, Choice
from django.http import Http404
from django.shortcuts import render


def index(request):
    latest_question_list = Questions.objects.order_by('-pub_date')[:5]

    context = {
        'latest_question_list': latest_question_list,
    }
    return render(render,'test/index.html',context)


def detail(request, question_id):
    try:
        question= Questions.objects.get(pk=question_id)
    except Questions.DoesNotExist:
        raise Http404("Question does not exist")
        question = get_object_or_404(Question, pk=question_id)
    return render(request, 'test/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    question = get_object_or_404(Questions,pk=question_id)
    return render(request,'test/results.html',{'question':question})


class IndexView(generic.ListView):
    template_name = 'test/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Questions.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Questions
    template_name = 'test/detail.html'


class ResultView(generic.DetailView):
    model = Questions
    template_name = 'test/results.html'


def vote(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    print("Came here")
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'test/detail.html', {'question': question,'error_message': "You didn't select a choice.",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('test:results', args=(question.id,)))