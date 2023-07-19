from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Choice, Question
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import QuestionForm
from django.utils import timezone

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:4]
    context = {
        "latest_question_list": latest_question_list
    }
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def result(request, question_id):
    q_in_result = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": q_in_result})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "ラジオボタンが選択できていませんでした。"
            }
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))


def create_question(request):
    create_question_form = QuestionForm()
    context = {'create_question_form': create_question_form}
    return render(request, "polls/create_question.html", context)

def post_question(request):
    try:
        question = Question(
        question_text = request.POST["question_text"],
        pub_date = timezone.now()
        )
        question.save()
        return HttpResponseRedirect(reverse("polls:detail", args=(question.id,)))
    except Exception as e:
        return render(
            request,
            "polls/create_question.html",
            {"error_message": f"質問登録ができませんでした。入力内容を確認してください。error message {e}"}
        )

def delete_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        question.delete()
        return HttpResponseRedirect(reverse("polls:index"))
    except Exception as e:
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": f"削除に失敗しました。詳細：{e}",
             }
        )
