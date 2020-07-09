from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Script(models.Model):
	opts = (('1', '1'),
		('2', '2'),
		('3', '3'),
		('4', '4'))
	user_ans0 = models.CharField(max_length=1, choices=opts)
	user_ans1 = models.CharField(max_length=1, choices=opts)
	user_ans2 = models.CharField(max_length=1, choices=opts)
	user_ans3 = models.CharField(max_length=1, choices=opts)
	user_ans4 = models.CharField(max_length=1, choices=opts)
	user_ans5 = models.CharField(max_length=1, choices=opts)
	user_ans6 = models.CharField(max_length=1, choices=opts)
	user_ans7 = models.CharField(max_length=1, choices=opts)
	user_ans8 = models.CharField(max_length=1, choices=opts)
	user_ans9 = models.CharField(max_length=1, choices=opts)
	title=models.CharField(max_length=20, default='Chemistry')
	userid=models.ForeignKey(User, on_delete=models.CASCADE)
	send_otl_script= models.BooleanField(default=False)
	received_script=models.BooleanField(default=False)
	send_result = models.BooleanField(default=False)
	number_scored=models.IntegerField(default=0)

class Question(models.Model):
	opts = (('1', '1'),
		('2', '2'),
		('3', '3'),
		('4', '4'))
	statement = models.CharField(max_length=500)
	option1 = models.CharField(max_length=100)
	option2 = models.CharField(max_length=100)
	option3 = models.CharField(max_length=100)
	option4 = models.CharField(max_length=100)
	correct_ans = models.CharField(max_length=1, choices=opts)
	script = models.ForeignKey(Script, on_delete=models.CASCADE)
