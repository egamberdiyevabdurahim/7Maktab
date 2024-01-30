from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.views import View

from .models import User
from .forms import UserForm, SignInForm
from News.models import LikeNews, News


class SignUp(View):
	def get(self, request):
		return render(request, 'signup.html')

	def post(self, request):
		username = request.POST.get('username')
		password = request.POST.get('password')
		if username and password:
			user = User.objects.create(
				username=username,
				password=password
			)
			user.set_password(password)
			user.save()
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
			return redirect('home')
		return render(request, 'signup.html')


class SignIn(View):
	def get(self, request):
		return render(request, 'indexx.html')

	def post(self, request):
		username=request.POST.get('username')
		password=request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		return render(request, 'indexx.html')


class LogOut(View):
	def get(self, request):
		logout(request)
		return redirect('home')


class Like(View):
	def post(self, request, slug):
		news = News.objects.get(slug=slug)
		if LikeNews.objects.filter(news=news):
			like = LikeNews.objects.filter(news=news).first()
			if request.user in like.user.all():
				like.user.remove(request.user)
				return redirect('home')
			like.user.add(request.user)
			return redirect('home')
		like = LikeNews.objects.create(
				news=news
			)
		like.user.add(request.user)
		return redirect('home')

