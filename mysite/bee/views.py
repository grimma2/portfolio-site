from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .utils import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.views.generic import ListView, DetailView, CreateView, View
from django.contrib.auth.views import LoginView
from django.db.models import *


def main(request):

	info = Info.objects.all()
	marafons = Marafon.objects.all()
	faq = Faq.objects.all()
	sponsors = Sponsor.objects.all()

	return render(request, 'bee/mainpage.html', {'info': info, 'marafons': marafons, 'faq': faq, 'sponsors': sponsors, 'title': 'Ешь и худей'})

def addplace(request, **kwargs):
	marafon_slug = kwargs.get('marafon_slug')
	Marafon.objects.get(slug=marafon_slug)-1

	return HttpResponseRedirect('/redirect/')



class Register(CreateView):
	form_class = UserRegister
	template_name = 'bee/register.html'
	success_url = reverse_lazy('login')

	def form_valid(self, form):
		user = form.save()
		login(self.request, user)
		return redirect('main')

class Login(LoginView):
	form_class = UserAuthentication
	template_name = 'bee/login.html'


def logout_user(request):
	logout(request)
	return redirect('main')


class MarafonDetail(DetailView):
	model = Marafon
	template_name = 'bee/marafondetail.html'
	context_object_name = 'marafon'
	slug_url_kwarg = 'marafon_slug'


