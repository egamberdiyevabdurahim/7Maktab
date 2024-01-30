from django.db import models
from django.utils.text import slugify


from User.models import User


class Photo(models.Model):
    photo = models.ImageField(upload_to='news_photo/', null=False, blank=False)


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='news_photos/', null=True)
    video = models.FileField(upload_to='news_video', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news_user')
    viewed_list = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def sum_of_likes(self):
        return self.likenews_news.user.count()

    def sum_of_vieved_list(self, *args, **kwargs):
        self.viewed_list = self.viewed_list+1
        super(News, self).save(*args, **kwargs)
    
    class Meta:
        ordering = [ '-id' ]



class LikeNews(models.Model):
    news = models.OneToOneField(News, on_delete=models.CASCADE, related_name='likenews_news')
    user = models.ManyToManyField(User, related_name='likenews_user')


class Haqida(models.Model):
    content = models.TextField()