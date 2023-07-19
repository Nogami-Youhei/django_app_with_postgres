
from django import forms
from .models import Question

class QuestionForm(forms.Form):

    form_question_text = forms.CharField(
        initial="",
        widget=forms.TextInput(
            attrs={'class':'question-text-input-form'}),
        min_length=5,
        error_messages={"required": "入力必須の箇所です。"}
        )

    class Meta:
        model = Question
        field=['form_question_text',]