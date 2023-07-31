import json
import re

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from polls.models import Choice, Question


@api_view(['POST'])
def register_choice(request):

    try:
        req = request.POST
        question_id = int(req.get('questionId'))
        choice_text = req.get('choiceText')

        only_space_pattern = "^[\s|　]+$"

        if (choice_text == "") or (choice_text is None) or (
            re.match(only_space_pattern, choice_text) ):
            raise Exception('空白では登録できません。')

        parent_question = Question.objects.get(pk=question_id)
        new_choice = parent_question.choice_set.create(
            choice_text = choice_text,
            votes = 0)

        res = {
            "status": "success",
            "body" :{
                "choiceId": new_choice.id
            }}
        return Response(res)
    except Exception as e:
        res = {
            "status" : "error",
            "error_message" : f"{e}"
        }
        return Response(res)