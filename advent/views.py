from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from advent.forms import UserForm
from advent.models import *
import advent.generate
import datetime

class FrontPage(View):
	def get(self, request):
		return render(request, "advent/login.html", {"form": UserForm()})
	def post(self, request):
		user = User.objects.filter(username = request.POST['username'])
		if(user):
			user = user[0]
			return redirect('advent:calendar', name=user.username)
		else:
			current_user = User(username = request.POST['username'], password = request.POST['password'])
			current_user.save()
			advent.generate.gifts(advent.generate.surprises(), current_user)
			return HttpResponse('new acct generated')

class CalendarView(View):
	def get(self, request, name):
		now = datetime.datetime.now()
		today = datetime.date(now.year, now.month, now.day)
		if(today < datetime.date(2014, 12, 25)):
			gift = Calendar.objects.get(date = today)
		else:
			gift = Calendar.objects.last()
		return render(request, "advent/present.html", {"name": name.upper(), "gift": gift, "date": "{month} / {day}".format(month = now.month, day = now.day)})
	
	def post(self, request, name):
		now = datetime.datetime.now()
		gift = Calendar.objects.get(date = datetime.date(now.year, now.month, now.day))
		if(gift.opened == False):
			gift.opened = True
			gift.save()
		return JsonResponse({'gift': gift.gift, 'opened': gift.opened})
