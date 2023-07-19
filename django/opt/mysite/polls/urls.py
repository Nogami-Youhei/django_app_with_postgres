from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("create_question/", views.create_question, name="create_question"),
    path("post_question/", views.post_question, name="post_question"),
    path("<int:question_id>/delete_question/", views.delete_question, name="delete_question")
]