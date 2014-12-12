from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from advent.forms import UserForm
from advent.models import *
import advent.generate
import datetime

class FrontPage(View):
	def get(self, request):
		print("I'm here!")
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
	today = datetime.date.today()
	def get(self, request, name):
		if(self.today < datetime.date(2014, 12, 25)):
			gift = Calendar.objects.get(name = name, date = self.today)
		else:
			gift = Calendar.objects.last()
		return render(request, "advent/present.html", {"name": name.capitalize(), "route_name": name, "gift": gift, "date": "{month} / {day}".format(month = self.today.month, day = self.today.day)})

	def post(self, request, name):
		gift = Calendar.objects.get(name = name, date = self.today)
		if(gift.opened == False):
			gift.opened = True
			gift.save()
		return JsonResponse({'gift': gift.gift, 'opened': gift.opened, 'gift_type': gift.gift_type})

class AllView(View):
	today = datetime.date.today()
	def get(self, request, name):
		gifts = Calendar.objects.filter(name = name).order_by('date')
		return render(request, 'advent/all.html', {'gifts':gifts, 'name': name, 'today':self.today})

	def post(self, request, name):
		gift = Calendar.objects.get(id=request.POST['gift'])
		if(gift.opened == False and self.today >= gift.date):
			gift.opened = True
			gift.save()
			return JsonResponse({'gift': gift.gift, 'date': gift.date})
		else:
			return JsonResponse({'fail': 1})
