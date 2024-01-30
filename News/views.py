from django.shortcuts import render, redirect
from django.views import View


from .forms import NewsForm
from .models import News, LikeNews, Haqida, Photo
from User.models import User


# class OpenNews(View):
# 	def get(self, request, id):
# 		news = News.objects.get(id=id)
# 		return render(request, 'opennews.html', {'news':news})


class Haqida(View):
	def get(self, request):
		# haqida = Haqida.objects.all()
		return render(request, 'about.html')


class CreateNews(View):
	def get(self, request):
		return render(request, 'create.html')

	def post(self, request):
		photo_list = request.FILES.getlist('photo', [])
		title=request.POST.get('title')
		content=request.POST.get('content')
		# photo = request.FILES.get('photo')
		if title:
			news = News.objects.create(
				title=title,
				content=content,
			)
			for x in photo_list:
				p = Photo.objects.create(photo=x)
				news.photo.add(p)
			return redirect('home')
		return render(request, 'create.html')


class OpenNews(View):
	def get(self, request, slug):
		news = News.objects.get(slug=slug)
		news.viewed_list = news.viewed_list+0
		news.sum_of_vieved_list()
            
		return render(request, 'course-details.html', {'news':news})


class EditNews(View):
	def get(self, request, id):
		news = News.objects.get(id=id)
		return render(request, 'create.html', {'form':news})

	def post(self, request, id):
		news = News.objects.get(id=id)
		title=request.POST.get('title')
		content=request.POST.get('content')
		photo = request.FILES.get('photo')
		if title.exsists():
			News.objects.create(
				title=title,
				content=content,
				photo=photo
			)
			return redirect('home')
		return render(request, 'create.html', {'form':news})


class DeleteNews(View):
	def get(self, request, id):
		news = News.objects.get(id=id)
		news.delete()
		return redirect('home')
