from django import forms


from .models import News, LikeNews


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'photo']
