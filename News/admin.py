from django.contrib import admin


from .models import News, LikeNews, Haqida, Photo


class NewsAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('title',)}

	class Meta:
		model = News


admin.site.register(News, NewsAdmin)
admin.site.register(LikeNews)
admin.site.register(Haqida)
admin.site.register(Photo)