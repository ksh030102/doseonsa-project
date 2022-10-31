
from django import forms
from webzine.models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        # labels 코드 추가하기
        labels = {
            'subject' : '제목',
            'content' : '내용',
        }