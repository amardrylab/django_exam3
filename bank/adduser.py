from django.contrib.auth.models import User
import csv

def fromcsv(csvfile):
	f=open(csvfile,"r")
	entries=csv.reader(f)
	for entry in entries:
		User.objects.create_user(entry[0], entry[1], "GoponKatha")
	f.close()
