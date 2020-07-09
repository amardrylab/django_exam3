from django.db import models

# Create your models here.

class QuestionPaper(models.Model):
	title=models.CharField(max_length=20)

	class Meta:
		ordering=['title']

	def __str__(self):
		return self.title

class Qbank(models.Model):
	statement=models.CharField(max_length=500)
	option1=models.CharField(max_length=100, blank=True)
	option2=models.CharField(max_length=100, blank=True)
	option3=models.CharField(max_length=100, blank=True)
	option4=models.CharField(max_length=100, blank=True)
	correctoption=models.IntegerField()
	questionpaper=models.ManyToManyField(QuestionPaper)

