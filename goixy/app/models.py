from django.db import models
from django.utils import timezone
# Create your models here.
class Question(models.Model):
	question = models.CharField(max_length=60)
	image = models.ImageField(upload_to='image',default="image/default.jpg")
	link = models.CharField(max_length=60,blank=True,null=True)
	def __str__(self):
		return self.question
class Answer(models.Model):
	user = models.IntegerField(default=1)
	question = models.ForeignKey(Question,on_delete=models.CASCADE)
	answer = models.IntegerField()
	def __str__(self):
		return self.question.question
class Good(models.Model):
	question = models.ForeignKey(Question,on_delete=models.CASCADE)
	text = models.CharField(max_length=60)
	def __str__(self):
		return self.question.question
class Bad(models.Model):
	question = models.ForeignKey(Question,on_delete=models.CASCADE)
	text = models.CharField(max_length=60)
	def __str__(self):
		return self.question.question
