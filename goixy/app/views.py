from django.shortcuts import render, get_object_or_404,redirect
from app.forms import QuestionForm,AnswerForm,GoodForm,BadForm
from app.models import Question,Answer,Good,Bad
import random
# Create your views here.
def index(request):
	request.session['user'] = random.randint(1,999999999)
	return render(request,'app/index.html')
def ask(request,pk):
	question = Question.objects.get(pk = pk)
	key = str(int(pk)+1)
	if request.method == "POST":
		form = AnswerForm(request.POST,request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.question = question
			post.user = request.session['user']
			post.save()
			context = {
				'pk':pk,
				'key':key,
			}
			return render(request,'app/select.html',context)
	else:
		form = AnswerForm()
		context={
		'form':form,
		'question':question,
		'key':key
				}
		return render(request,'app/ask.html',context)
def select(request,pk):
	return render(request,'app/select.html',{'pk':pk})
def apply(request):
	if request.method == "POST":
		form = QuestionForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('app:index')
	else:
		form = QuestionForm()
		return render(request,'app/apply.html',{'form':form})
def good(request,pk):
    pk = pk
    good = Good.objects.filter(pk=pk)
    context = {
        'pk' : pk,
        'good':good,
    }
    return render(request,'app/good.html',context)
def bad(request,pk):
    pk = pk
    bad = Bad.objects.filter(pk=pk)
    context = {
        'pk' : pk,
        'bad':bad
    }
    return render(request,'app/bad.html',context)
def test(request):
	if request.method == "POST":
		context = {
				'pk':request.example,
			}
		return render(request,'app/test.html',context)
	else:
		form = AnswerForm()
		context={
				}
		return render(request,'app/test.html',context)
