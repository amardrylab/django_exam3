from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from .forms import AnsForm
from .models import Script
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_text
from django.contrib.auth import login, logout

# Create your views here.

def exam(request, scriptid64=None, token=None):
	try:
		scriptid=force_text(urlsafe_base64_decode(scriptid64))
		script=Script.objects.get(pk=scriptid)
		user=script.userid
	except Script.DoesNotExist:
		script=None
	if script and default_token_generator.check_token(user, token):
		questions=script.question_set.all()
		if request.method=='POST':
			form=AnsForm(request.POST, instance=script)
			if form.is_valid():
                                temp=form.save(commit=False)
                                temp.received_script=True
                                temp.save()
                                login(request, user)
                                logout(request)
                                return HttpResponse('<h1>Your form is saved</h1>')
		else:
			form=AnsForm()
		return render(request, 'question.html', {'form':form, 'questions':questions})
	else:
		return HttpResponse("<h1>Your time has expired</h1>")
