from django import forms
from .models import Question,Answer,Good,Bad

class QuestionForm(forms.ModelForm):

	class Meta:
		model = Question
		fields = ('question','image','link')
class AnswerForm(forms.ModelForm):

	class Meta:
		model = Answer
		fields = ('answer',)
class GoodForm(forms.ModelForm):

	class Meta:
		model = Good
		fields = ('text',)
class BadForm(forms.ModelForm):

	class Meta:
		model = Bad
		fields = ('text',)