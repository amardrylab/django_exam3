from .script import Qp
from .models import Question, Script
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.encoding import force_text
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.urls import reverse


def set(title, users):
	qp=Qp(title)
	template_name="qheader.html"
	for user in users:
		script=Script()
		script.title=title
		script.userid=user
		script.save()
		
		qp.olotpalot()
		for frag in qp.fullset:
			attempt=Question()
			attempt.statement=frag.question
			attempt.option1 = frag.options[0].choice
			attempt.option2 = frag.options[1].choice
			attempt.option3 = frag.options[2].choice
			attempt.option4 = frag.options[3].choice
			count=1
			for answer in frag.options:
				if answer.ans:
					attempt.correct_ans=count
				count+=1
			attempt.script = script
			attempt.save()

def sendotlforexam(title):
	papers=Script.objects.filter(send_otl_script=False).filter(title=title)
	text_content="Your one time link Email"
	subject="Examination Script for " + title
	template_name="otl.html"
	from_email=settings.EMAIL_HOST_USER
	for paper in papers:
		recipients=[paper.userid.email]

		kwargs = {
			"scriptid64"  :  urlsafe_base64_encode(force_bytes(paper.id)),
			"token"  : default_token_generator.make_token(paper.userid)
		}
		the_url = reverse("exam_request", kwargs=kwargs)
		otl_url = "{0}://{1}{2}".format("http", "www.drylab.in:8000", the_url)

		context = {
			'user': paper.userid,
			'otl_url': otl_url,
		}
		html_content = render_to_string(template_name, context)
		email = EmailMultiAlternatives(subject, text_content, from_email, recipients)
		email.attach_alternative(html_content, "text/html")
		email.send()
		paper.send_otl_script=True
		paper.save()
		print("Mail has been sent to {0}\n".format(paper.userid.email))

def evaluate(title):
	papers=Script.objects.filter(received_script=True).filter(title=title)
	for paper in papers:
		paper.number_scored = 0
		ref=paper.question_set.all()
		if paper.user_ans0 == ref[0].correct_ans:
			paper.number_scored += 1
		if paper.user_ans1 == ref[1].correct_ans:
			paper.number_scored += 1
		if paper.user_ans2 == ref[2].correct_ans:
			paper.number_scored += 1
		if paper.user_ans3 == ref[3].correct_ans:
			paper.number_scored += 1
		if paper.user_ans4 == ref[4].correct_ans:
			paper.number_scored += 1
		if paper.user_ans5 == ref[5].correct_ans:
			paper.number_scored += 1
		if paper.user_ans6 == ref[6].correct_ans:
			paper.number_scored += 1
		if paper.user_ans7 == ref[7].correct_ans:
			paper.number_scored += 1
		if paper.user_ans8 == ref[8].correct_ans:
			paper.number_scored += 1
		if paper.user_ans9 == ref[9].correct_ans:
			paper.number_scored += 1
		paper.save()
			
	

def sendresult(title):
	papers=Script.objects.filter(received_script=True).filter(send_result=False).filter(title=title)
	text_content="Your result for exam in " + title
	subject="Examination result for " + title
	template_name="result.html"
	from_email=settings.EMAIL_HOST_USER
	for paper in papers:
		recipients = [paper.userid.email]
		context = {
			'script' : paper,
			'questions' : paper.question_set.all()
		}
		html_content = render_to_string(template_name, context)
		email = EmailMultiAlternatives(subject, text_content, from_email, recipients)
		email.attach_alternative(html_content, "text/html")
		email.send()
		paper.send_result=True
		print("Mail has been sent to {0}\n".format(paper.userid.email))
