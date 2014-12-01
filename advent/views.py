from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from advent.forms import UserForm

class FrontPage(View):
	def get(self, request):
		return render(request, "advent/login.html", {"form": UserForm()})
	def post(self, request):
		pass
