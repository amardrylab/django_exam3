import re
from .models import Qbank, QuestionPaper

def loadquestion(filename):
	f = open(filename)
	text = f.read()
	reg = re.compile(r'.*\no\).*\no\).*\no\).*\no\).*\n\d')
	fragments = reg.findall(text)
	for elt in fragments:
		question=Qbank()
		smallreg=re.compile(r'(.*)\no\)(.*)\no\)(.*)\no\)(.*)\no\)(.*)\n(\d)')
		smallfrag = smallreg.search(elt)
		question.statement = smallfrag.group(1)
		question.option1 = smallfrag.group(2)
		question.option2 = smallfrag.group(3)
		question.option3 = smallfrag.group(4)
		question.option4 = smallfrag.group(5)
		question.correctoption=smallfrag.group(6)
		question.save()

def buildquestionpaper(title, list=[*range(1,11)]):
	qp=QuestionPaper(title=title)
	qp.save()
	for element in list:
		question=Qbank.objects.get(pk=element)
		question.questionpaper.add(qp)
		question.save()

