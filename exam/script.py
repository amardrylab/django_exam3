from bank.models import QuestionPaper
import random

class Option:
	def __init__(self, choice, ans):
		self.choice = choice
		self.ans = ans


class Mcq:
	def __init__(self, q):
		self.question = q.statement
		self.options = []
		opts = [q.option1, q.option2, q.option3, q.option4]
		correctoption = q.correctoption
		count = 1
		for opt in opts:
			myoption = Option(opt, correctoption == count)
			self.options.append(myoption)
			count +=1

class Qp:
	def __init__(self, title):
		set = QuestionPaper.objects.get(title=title).qbank_set.all()
		self.fullset = []
		for question in set:
			mymcq= Mcq(question)
			self.fullset.append(mymcq)

	def olotpalot(self):
		random.shuffle(self.fullset)
		for elt in self.fullset:
			random.shuffle(elt.options)

	def setuserlist(self, users):
		self.users=users
