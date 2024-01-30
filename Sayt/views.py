from django.shortcuts import render
from django.core.paginator import Paginator
from django.views import View


from News.models import News


class Home(View):
	def get(self, request):
		news = News.objects.order_by( '-id' )
		page = Paginator(news, 4)
		number = request.GET.get('page', 1)
		pages = page.page(number)
		find = request.GET.get('find', None)
		if find:
			pages = News.objects.filter(title__icontains=find).order_by( '-id' )
			# pages = News.objects.filter(content__icontains=find).order_by( '-id' ) 
		return render(request, 'index.html', {'news':pages})
